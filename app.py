from flask import Flask, render_template

app = Flask(__name__)

# --- Data (in een echt project zou dit uit een database of Shopify API komen) ---

PRODUCTS = [
    {
        "name": "Aria Buds Pro",
        "category": "Draadloze oordopjes",
        "price": 129.00,
        "specs": [
            ("DRIVER", "11mm dynamisch"),
            ("ANC", "-32dB"),
            ("BATTERIJ", "8u + 24u case"),
            ("WATERDICHT", "IPX4"),
        ],
    },
    {
        "name": "Loop Charger 65W",
        "category": "GaN-oplader, 3-poorts",
        "price": 49.00,
        "specs": [
            ("VERMOGEN", "65W GaN"),
            ("POORTEN", "2x USB-C, 1x USB-A"),
            ("GEWICHT", "112g"),
            ("KABEL", "inbegrepen, 1.5m"),
        ],
    },
    {
        "name": "Slate Keyboard 75",
        "category": "Mechanisch toetsenbord",
        "price": 159.00,
        "specs": [
            ("SWITCH", "Brown tactile"),
            ("VERBINDING", "Bluetooth + USB-C"),
            ("BATTERIJ", "4000mAh"),
            ("LAYOUT", "75%, BE/QWERTY"),
        ],
    },
    {
        "name": "Orbit Hub",
        "category": "USB-C dock, 7-in-1",
        "price": 79.00,
        "specs": [
            ("UITGANGEN", "HDMI 4K, SD, 3x USB"),
            ("PD", "100W passthrough"),
            ("MATERIAAL", "Geanodiseerd aluminium"),
            ("KABEL", "20cm, gevlochten"),
        ],
    },
]

FEATURES = [
    {
        "label": "SELECTIE",
        "title": "Elk product getest",
        "text": "We voegen niets toe zonder het zelf minstens twee weken te gebruiken. "
                "Geen dropship-ruis, alleen wat wij zelf zouden kopen.",
    },
    {
        "label": "LEVERING",
        "title": "Verzonden vanuit de EU",
        "text": "Geen wekenlang wachten op een pakket van de andere kant van de wereld. "
                "Voorraad ligt bij ons, dus binnen 24u de deur uit.",
    },
    {
        "label": "GARANTIE",
        "title": "2 jaar, standaard",
        "text": "Op elk toestel, zonder kleine lettertjes of verlengde garantie die je "
                "apart moet bijkopen.",
    },
]


@app.route("/")
def home():
    return render_template("index.html", products=PRODUCTS, features=FEATURES)


if __name__ == "__main__":
    # debug=True is handig tijdens ontwikkeling, zet dit uit in productie
    app.run(debug=True, port=5000)
