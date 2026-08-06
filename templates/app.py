from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
import os

from models import db, User, Product, Order, OrderItem

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "lokale-dev-sleutel-niet-voor-productie")

# Database: op Render gebruiken we PostgreSQL (via DATABASE_URL),
# lokaal valt hij automatisch terug op een SQLite-bestand.
database_url = os.environ.get("DATABASE_URL")
if database_url:
    # Render geeft een URL die begint met "postgres://", maar SQLAlchemy
    # verwacht "postgresql://" — daarom deze correctie.
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///shop.db"

db.init_app(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message = "Log eerst in om verder te gaan."


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ---------- Hulpfuncties voor het winkelmandje (opgeslagen in de sessie) ----------

def get_cart():
    """Haalt het winkelmandje op uit de sessie, als dict {product_id: aantal}."""
    return session.get("cart", {})


def save_cart(cart):
    session["cart"] = cart
    session.modified = True


def get_cart_items():
    """Zet het sessie-mandje om in een lijst met echte productinfo + subtotaal."""
    cart = get_cart()
    items = []
    total = 0
    for product_id, qty in cart.items():
        product = db.session.get(Product, int(product_id))
        if product:
            subtotal = product.price * qty
            total += subtotal
            items.append({"product": product, "qty": qty, "subtotal": subtotal})
    return items, total


@app.context_processor
def inject_cart_count():
    cart = get_cart()
    count = sum(cart.values())
    return {"cart_count": count}


# ---------- Shop pagina's ----------

@app.route("/")
def home():
    products = Product.query.all()
    return render_template("index.html", products=products)


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = db.session.get(Product, product_id)
    if not product:
        flash("Product niet gevonden.")
        return redirect(url_for("home"))
    return render_template("product.html", product=product)


# ---------- Winkelmandje ----------

@app.route("/cart/add/<int:product_id>", methods=["POST"])
def cart_add(product_id):
    cart = get_cart()
    key = str(product_id)
    cart[key] = cart.get(key, 0) + 1
    save_cart(cart)
    flash("Product toegevoegd aan je winkelmandje.")
    return redirect(request.referrer or url_for("home"))


@app.route("/cart/remove/<int:product_id>", methods=["POST"])
def cart_remove(product_id):
    cart = get_cart()
    cart.pop(str(product_id), None)
    save_cart(cart)
    return redirect(url_for("cart_view"))


@app.route("/cart")
def cart_view():
    items, total = get_cart_items()
    return render_template("cart.html", items=items, total=total)


# ---------- Accounts ----------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not name or not email or not password:
            flash("Vul alle velden in.")
            return redirect(url_for("register"))

        existing = User.query.filter_by(email=email).first()
        if existing:
            flash("Er bestaat al een account met dit e-mailadres.")
            return redirect(url_for("register"))

        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(name=name, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Account aangemaakt! Welkom.")
        return redirect(url_for("home"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Je bent ingelogd.")
            next_page = request.args.get("next")
            return redirect(next_page or url_for("home"))

        flash("E-mailadres of wachtwoord klopt niet.")
        return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    save_cart({})  # mandje leegmaken zodat de teller klopt na uitloggen
    flash("Je bent uitgelogd.")
    return redirect(url_for("home"))


@app.route("/account")
@login_required
def account():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template("account.html", orders=orders)


# ---------- Checkout ----------

@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    items, total = get_cart_items()
    if not items:
        flash("Je winkelmandje is leeg.")
        return redirect(url_for("home"))

    if request.method == "POST":
        order = Order(
            user_id=current_user.id,
            total=total,
            shipping_name=request.form.get("shipping_name"),
            shipping_address=request.form.get("shipping_address"),
            shipping_city=request.form.get("shipping_city"),
            shipping_postal=request.form.get("shipping_postal"),
        )
        db.session.add(order)
        db.session.flush()  # zodat order.id al beschikbaar is

        for item in items:
            db.session.add(OrderItem(
                order_id=order.id,
                product_id=item["product"].id,
                product_name=item["product"].name,
                quantity=item["qty"],
                price_at_purchase=item["product"].price,
            ))

        db.session.commit()
        save_cart({})  # mandje leegmaken

        return redirect(url_for("order_success", order_id=order.id))

    return render_template("checkout.html", items=items, total=total)


@app.route("/order/<int:order_id>/success")
@login_required
def order_success(order_id):
    order = db.session.get(Order, order_id)
    if not order or order.user_id != current_user.id:
        return redirect(url_for("home"))
    return render_template("order_success.html", order=order)


@app.route("/over-ons")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # In deze versie versturen we nog geen echte e-mail — dat is de volgende stap.
        # Voorlopig loggen we het bericht gewoon en tonen we een bevestiging.
        name = request.form.get("name", "")
        print(f"[CONTACT] {name} - {request.form.get('email')}: {request.form.get('message')}")
        flash("Bedankt voor je bericht! We nemen zo snel mogelijk contact op.")
        return redirect(url_for("contact"))
    return render_template("contact.html")


def setup_database():
    """Maakt tabellen aan als ze nog niet bestaan, en vult de shop met
    startproducten als de database nog leeg is. Draait bij elke opstart,
    maar doet niets als alles er al staat."""
    db.create_all()
    if Product.query.count() == 0:
        from seed_data import STARTER_PRODUCTS
        db.session.add_all([Product(**p) for p in STARTER_PRODUCTS])
        db.session.commit()
        print("Startproducten toegevoegd aan de database.")


with app.app_context():
    setup_database()


if __name__ == "__main__":
    app.run(debug=True, port=5000)
