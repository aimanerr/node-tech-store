from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """Een klant met een account."""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship("Order", backref="customer", lazy=True)


class Product(db.Model):
    """Een product in de shop."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False, default="")
    stock = db.Column(db.Integer, nullable=False, default=10)

    # Specs slaan we op als 4 losse label/waarde paren voor eenvoud
    spec1_label = db.Column(db.String(50), default="")
    spec1_value = db.Column(db.String(100), default="")
    spec2_label = db.Column(db.String(50), default="")
    spec2_value = db.Column(db.String(100), default="")
    spec3_label = db.Column(db.String(50), default="")
    spec3_value = db.Column(db.String(100), default="")
    spec4_label = db.Column(db.String(50), default="")
    spec4_value = db.Column(db.String(100), default="")

    @property
    def specs(self):
        pairs = [
            (self.spec1_label, self.spec1_value),
            (self.spec2_label, self.spec2_value),
            (self.spec3_label, self.spec3_value),
            (self.spec4_label, self.spec4_value),
        ]
        return [(l, v) for l, v in pairs if l]


class Order(db.Model):
    """Een geplaatste bestelling."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), default="Nieuw")
    total = db.Column(db.Float, nullable=False)

    # Verzendgegevens (simpel gehouden)
    shipping_name = db.Column(db.String(150))
    shipping_address = db.Column(db.String(250))
    shipping_city = db.Column(db.String(100))
    shipping_postal = db.Column(db.String(20))

    items = db.relationship("OrderItem", backref="order", lazy=True)


class OrderItem(db.Model):
    """Eén productregel binnen een bestelling."""
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    product_name = db.Column(db.String(150))  # bewaard als "snapshot" voor het geval het product later verandert
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_purchase = db.Column(db.Float, nullable=False)

    product = db.relationship("Product")
