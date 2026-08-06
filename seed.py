"""
Handmatig script om de database aan te maken en te vullen.
Draai met: python seed.py

Let op: app.py doet dit tegenwoordig automatisch bij het opstarten,
dus dit script is vooral handig om lokaal even opnieuw te beginnen.
"""

from app import app
from models import db, Product
from seed_data import STARTER_PRODUCTS

with app.app_context():
    db.create_all()

    if Product.query.count() == 0:
        db.session.add_all([Product(**p) for p in STARTER_PRODUCTS])
        db.session.commit()
        print(f"{len(STARTER_PRODUCTS)} producten toegevoegd aan de database.")
    else:
        print("Er staan al producten in de database, er is niets toegevoegd.")
