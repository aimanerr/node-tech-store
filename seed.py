"""
Dit script maakt de database-tabellen aan en vult ze met wat startproducten.
Draai dit éénmalig met: python seed.py
Je kan het later opnieuw draaien om producten te resetten (bestaande producten
worden dan niet verwijderd, dit script voegt enkel toe als de tabel leeg is).
"""

from app import app
from models import db, Product

with app.app_context():
    db.create_all()

    if Product.query.count() == 0:
        products = [
            Product(
                name="Aria Buds Pro",
                category="Draadloze oordopjes",
                price=129.00,
                description="Compacte draadloze oordopjes met actieve ruisonderdrukking, "
                             "ideaal voor dagelijks gebruik onderweg of op kantoor.",
                stock=15,
                spec1_label="DRIVER", spec1_value="11mm dynamisch",
                spec2_label="ANC", spec2_value="-32dB",
                spec3_label="BATTERIJ", spec3_value="8u + 24u case",
                spec4_label="WATERDICHT", spec4_value="IPX4",
            ),
            Product(
                name="Loop Charger 65W",
                category="GaN-oplader, 3-poorts",
                price=49.00,
                description="Compacte snellader met GaN-technologie, laadt tot drie "
                             "apparaten tegelijk op zonder in te leveren op snelheid.",
                stock=30,
                spec1_label="VERMOGEN", spec1_value="65W GaN",
                spec2_label="POORTEN", spec2_value="2x USB-C, 1x USB-A",
                spec3_label="GEWICHT", spec3_value="112g",
                spec4_label="KABEL", spec4_value="inbegrepen, 1.5m",
            ),
            Product(
                name="Slate Keyboard 75",
                category="Mechanisch toetsenbord",
                price=159.00,
                description="Compact 75%-toetsenbord met tactiele switches en "
                             "draadloze connectiviteit, gebouwd voor dagelijks typewerk.",
                stock=10,
                spec1_label="SWITCH", spec1_value="Brown tactile",
                spec2_label="VERBINDING", spec2_value="Bluetooth + USB-C",
                spec3_label="BATTERIJ", spec3_value="4000mAh",
                spec4_label="LAYOUT", spec4_value="75%, BE/QWERTY",
            ),
            Product(
                name="Orbit Hub",
                category="USB-C dock, 7-in-1",
                price=79.00,
                description="Alles-in-één USB-C dock met HDMI, kaartlezer en "
                             "krachtige doorvoerlading voor je laptop.",
                stock=20,
                spec1_label="UITGANGEN", spec1_value="HDMI 4K, SD, 3x USB",
                spec2_label="PD", spec2_value="100W passthrough",
                spec3_label="MATERIAAL", spec3_value="Geanodiseerd aluminium",
                spec4_label="KABEL", spec4_value="20cm, gevlochten",
            ),
        ]
        db.session.add_all(products)
        db.session.commit()
        print(f"{len(products)} producten toegevoegd aan de database.")
    else:
        print("Er staan al producten in de database, er is niets toegevoegd.")
