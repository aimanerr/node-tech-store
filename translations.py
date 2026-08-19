"""
Vertalingen voor NODE.

Hoe het werkt:
- Elke tekst heeft een korte sleutel, bv. "nav_shop".
- Per taal staat de vertaling in het bijbehorende woordenboek.
- In templates gebruik je: {{ t('nav_shop') }}

Een tekst toevoegen? Zet dezelfde sleutel in alle drie de talen.
Ontbreekt een vertaling? Dan valt hij automatisch terug op Nederlands.
"""

LANGUAGES = {
    "nl": "Nederlands",
    "en": "English",
    "fr": "Français",
}

DEFAULT_LANGUAGE = "nl"


TRANSLATIONS = {
    # ---------------------------------------------------------------- NL
    "nl": {
        # Navigatie
        "nav_shop": "Shop",
        "nav_about": "Over ons",
        "nav_contact": "Contact",
        "nav_login": "Inloggen",
        "nav_register": "Account maken",
        "nav_account": "Mijn account",
        "nav_logout": "Uitloggen",
        "nav_cart": "Mandje",

        # Homepage
        "home_status": "STATUS: NIEUWE SHIPMENT BINNEN",
        "home_title": "Tech, zonder de ruis.",
        "home_intro": "Zorgvuldig geselecteerde apparaten voor mensen die weten wat ze zoeken. "
                      "Geen marketingtaal, gewoon de specs die ertoe doen.",
        "home_cta": "Bekijk collectie",
        "home_products_title": "Deze week in de shop",
        "home_products_sub": "Klik op een product voor meer details.",
        "home_why_title": "Waarom NODE.",
        "home_why1_label": "SELECTIE",
        "home_why1_title": "Elk product getest",
        "home_why1_text": "We voegen niets toe zonder het zelf te gebruiken.",
        "home_why2_label": "LEVERING",
        "home_why2_title": "Verzonden vanuit België",
        "home_why2_text": "Geen weken wachten, binnen 24u de deur uit.",
        "home_why3_label": "GARANTIE",
        "home_why3_title": "2 jaar, standaard",
        "home_why3_text": "Op elk toestel, zonder kleine lettertjes.",

        # Product
        "product_back": "Terug naar shop",
        "product_add": "Toevoegen aan winkelmandje",
        "product_stock": "op voorraad",
        "product_sold_out": "Momenteel niet op voorraad",
        "product_added": "Product toegevoegd aan je winkelmandje.",
        "product_not_found": "Product niet gevonden.",

        # Winkelmandje
        "cart_title": "Je winkelmandje",
        "cart_empty": "Je winkelmandje is nog leeg.",
        "cart_continue": "Verder winkelen",
        "cart_remove": "verwijderen",
        "cart_total": "Totaal",
        "cart_checkout": "Afrekenen",

        # Checkout
        "checkout_title": "Afrekenen",
        "checkout_subtotal": "Subtotaal",
        "checkout_shipping": "Verzending",
        "checkout_free": "Gratis",
        "checkout_total": "Totaal",
        "checkout_free_from": "Nog {amount} tot gratis verzending",
        "checkout_details": "Verzendgegevens",
        "checkout_name": "Volledige naam",
        "checkout_address": "Adres",
        "checkout_postal": "Postcode",
        "checkout_city": "Stad",
        "checkout_country": "Land",
        "checkout_place_order": "Bestelling plaatsen",
        "checkout_no_payment": "Let op: er is nog geen echte betaling gekoppeld — "
                               "dit plaatst de bestelling voor testdoeleinden.",

        # Bestelling geplaatst
        "success_order": "BESTELLING",
        "success_title": "Bedankt voor je bestelling!",
        "success_text": "We hebben je bestelling van {amount} ontvangen en gaan ermee aan de slag.",
        "success_continue": "Verder winkelen",

        # Account
        "account_title": "Mijn account",
        "account_logged_in": "Ingelogd als",
        "account_orders": "Mijn bestellingen",
        "account_no_orders": "Je hebt nog geen bestellingen geplaatst.",
        "account_order": "Bestelling",
        "account_shipping_to": "Verzending naar",
        "account_free": "gratis",

        # Inloggen / registreren
        "login_title": "Inloggen",
        "login_sub": "Welkom terug bij NODE.",
        "login_email": "E-mailadres",
        "login_email_ph": "jij@voorbeeld.be",
        "login_password": "Wachtwoord",
        "login_button": "Inloggen",
        "login_no_account": "Nog geen account?",
        "login_create": "Maak er een aan",
        "login_success": "Je bent ingelogd.",
        "login_failed": "E-mailadres of wachtwoord klopt niet.",
        "logout_success": "Je bent uitgelogd.",

        "register_title": "Account maken",
        "register_sub": "Zo kan je je bestellingen volgen.",
        "register_name": "Naam",
        "register_name_ph": "Voor- en achternaam",
        "register_password_ph": "Minstens 6 tekens",
        "register_button": "Account aanmaken",
        "register_has_account": "Heb je al een account?",
        "register_login": "Log hier in",
        "register_success": "Account aangemaakt! Welkom.",
        "register_exists": "Er bestaat al een account met dit e-mailadres.",
        "register_fill_all": "Vul alle velden in.",

        # Over ons
        "about_label": "// OVER ONS",
        "about_title": "Gebouwd door mensen die zelf de spullen gebruiken.",
        "about_p1": "NODE. is ontstaan uit frustratie: te veel webshops verkopen tech-gadgets die na "
                    "twee weken kapot zijn, verpakt in marketingtaal die niks zegt over hoe het "
                    "product écht presteert.",
        "about_p2": "Wij testen elk product minstens twee weken voor het in de shop komt. Geen "
                    "dropship-ruis, geen producten die we zelf niet zouden kopen.",
        "about_p3": "We zijn een klein, onafhankelijk team gevestigd in België. Elke bestelling wordt "
                    "vanuit hier verstuurd, en elke vraag wordt door een echt mens beantwoord.",
        "about_stat1": "OPGERICHT",
        "about_stat2_num": "2 weken",
        "about_stat2": "TESTPERIODE PER PRODUCT",
        "about_stat3": "VERZENDING VANUIT BE",

        # Contact
        "contact_label": "// CONTACT",
        "contact_title": "Vraag, klacht of gewoon een idee?",
        "contact_intro": "Vul het formulier in en we antwoorden meestal binnen 1 werkdag. Voor "
                         "dringende vragen over een lopende bestelling, vermeld gerust je bestelnummer.",
        "contact_email_label": "E-MAIL",
        "contact_region_label": "REGIO",
        "contact_hours_label": "UREN",
        "contact_hours": "Ma–Vr, 9:00–17:00",
        "contact_name": "Naam",
        "contact_email": "E-mailadres",
        "contact_message": "Bericht",
        "contact_send": "Verstuur bericht",
        "contact_thanks": "Bedankt voor je bericht! We nemen zo snel mogelijk contact op.",

        # Footer
        "footer_tagline": "Tech, zonder de ruis.",
        "footer_terms": "Algemene voorwaarden",
        "footer_privacy": "Privacybeleid",
        "footer_returns": "Retourbeleid",

        # Juridisch — gedeeld
        "legal_label": "// JURIDISCH",
        "legal_updated": "Laatst bijgewerkt: augustus 2026",
        "legal_draft": "Let op: deze tekst is een werkversie en moet nog juridisch nagekeken "
                       "worden voor de shop opengaat.",

        # Algemene voorwaarden
        "terms_title": "Algemene voorwaarden",
        "terms_h1": "1. Identiteit van de verkoper",
        "terms_h2": "2. Toepasselijkheid",
        "terms_p2": "Deze algemene voorwaarden zijn van toepassing op elke bestelling die via deze "
                    "webshop wordt geplaatst. Door een bestelling te plaatsen aanvaardt de klant "
                    "deze voorwaarden.",
        "terms_h3": "3. Prijzen",
        "terms_p3": "Alle prijzen zijn uitgedrukt in euro en inclusief BTW. Verzendkosten worden apart "
                    "vermeld en berekend op basis van het afleveradres. Vanaf een bestelbedrag van "
                    "€ 75,00 zijn de verzendkosten gratis.",
        "terms_h4": "4. Bestelling en levering",
        "terms_p4": "Een bestelling komt tot stand op het moment van bevestiging. Wij streven ernaar "
                    "bestellingen binnen 24 uur na betaling te verzenden. Levertijden zijn indicatief "
                    "en afhankelijk van de bestemming.",
        "terms_h5": "5. Herroepingsrecht",
        "terms_p5": "De consument heeft het recht om binnen 14 kalenderdagen na ontvangst van de "
                    "bestelling de overeenkomst te herroepen zonder opgave van reden. Zie ons",
        "terms_p5_link": "retourbeleid",
        "terms_p5_end": "voor de praktische afhandeling.",
        "terms_h6": "6. Garantie",
        "terms_p6": "Op alle producten geldt de wettelijke garantie van 2 jaar op conformiteitsgebreken, "
                    "conform het Belgisch Wetboek van Economisch Recht.",
        "terms_h7": "7. Toepasselijk recht",
        "terms_p7": "Op deze overeenkomst is het Belgisch recht van toepassing. Geschillen worden "
                    "voorgelegd aan de bevoegde rechtbanken.",

        # Privacy
        "privacy_title": "Privacybeleid",
        "privacy_h1": "1. Wie verwerkt je gegevens",
        "privacy_p1": "NODE., met ondernemingsnummer [KBO-nummer], is verantwoordelijk voor de "
                      "verwerking van je persoonsgegevens. Voor vragen kan je terecht op hello@nodetech.be.",
        "privacy_h2": "2. Welke gegevens verzamelen we",
        "privacy_p2": "Bij het aanmaken van een account bewaren we je naam, e-mailadres en een "
                      "versleutelde versie van je wachtwoord. Bij een bestelling bewaren we daarnaast "
                      "je afleveradres en de inhoud van je bestelling.",
        "privacy_h3": "3. Waarom we ze verwerken",
        "privacy_p3": "Uitsluitend om je bestelling te kunnen verwerken en leveren, je account te "
                      "beheren, en om te voldoen aan wettelijke verplichtingen zoals boekhouding. "
                      "We gebruiken je gegevens niet voor reclame en verkopen ze niet door aan derden.",
        "privacy_h4": "4. Hoe lang we ze bewaren",
        "privacy_p4": "Accountgegevens bewaren we zolang je account bestaat. Bestelgegevens bewaren "
                      "we conform de wettelijke bewaartermijn voor boekhoudkundige stukken.",
        "privacy_h5": "5. Je rechten",
        "privacy_p5": "Onder de AVG (GDPR) heb je recht op inzage, correctie, verwijdering en "
                      "overdraagbaarheid van je gegevens, en het recht om bezwaar te maken tegen de "
                      "verwerking. Stuur een e-mail naar hello@nodetech.be om een van deze rechten "
                      "uit te oefenen.",
        "privacy_h6": "6. Cookies",
        "privacy_p6": "Deze site gebruikt enkel functionele cookies die nodig zijn om je winkelmandje "
                      "en inlogsessie te laten werken. We gebruiken geen tracking- of advertentiecookies.",
        "privacy_h7": "7. Klachten",
        "privacy_p7": "Je hebt het recht een klacht in te dienen bij de Gegevensbeschermingsautoriteit "
                      "(Drukpersstraat 35, 1000 Brussel — gegevensbeschermingsautoriteit.be).",

        # Retour
        "returns_title": "Retourbeleid",
        "returns_h1": "Je hebt 14 dagen bedenktijd",
        "returns_p1": "Als consument heb je het recht om binnen 14 kalenderdagen na ontvangst van je "
                      "bestelling aan te geven dat je de aankoop wil herroepen, zonder dat je daarvoor "
                      "een reden hoeft op te geven. Daarna heb je nog eens 14 dagen om het product "
                      "terug te sturen.",
        "returns_h2": "Hoe je retourneert",
        "returns_step1": "Stuur een e-mail naar hello@nodetech.be met je bestelnummer",
        "returns_step2": "Je ontvangt van ons de retourinstructies",
        "returns_step3": "Verpak het product zorgvuldig, bij voorkeur in de originele verpakking",
        "returns_step4": "Stuur het terug naar het adres dat je van ons kreeg",
        "returns_h3": "Voorwaarden",
        "returns_p3": "Het product moet in dezelfde staat verkeren als bij ontvangst. Je mag het "
                      "product uitproberen zoals je in een winkel zou doen, maar bij gebruik dat "
                      "verder gaat dan nodig om de aard en werking vast te stellen, kunnen we een "
                      "waardevermindering aanrekenen.",
        "returns_h4": "Terugbetaling",
        "returns_p4": "Zodra we je retour ontvangen en gecontroleerd hebben, betalen we het "
                      "aankoopbedrag terug binnen 14 dagen, via dezelfde betaalmethode als bij de "
                      "aankoop. De oorspronkelijke verzendkosten worden terugbetaald, de kosten van "
                      "de retourzending zijn voor jouw rekening.",
        "returns_h5": "Defect of verkeerd product ontvangen?",
        "returns_p5": "Dan valt dat niet onder retour maar onder garantie. Neem contact op via",
        "returns_p5_link": "onze contactpagina",
        "returns_p5_end": "— we lossen dat op zonder kosten voor jou.",

        # Algemeen
        "cart_login_first": "Log eerst in om verder te gaan.",
        "cart_is_empty": "Je winkelmandje is leeg.",
    },

    # ---------------------------------------------------------------- EN
    "en": {
        "nav_shop": "Shop",
        "nav_about": "About",
        "nav_contact": "Contact",
        "nav_login": "Log in",
        "nav_register": "Create account",
        "nav_account": "My account",
        "nav_logout": "Log out",
        "nav_cart": "Cart",

        "home_status": "STATUS: NEW SHIPMENT IN",
        "home_title": "Tech, without the noise.",
        "home_intro": "Carefully selected devices for people who know what they're looking for. "
                      "No marketing speak, just the specs that matter.",
        "home_cta": "View collection",
        "home_products_title": "This week in the shop",
        "home_products_sub": "Click a product for more details.",
        "home_why_title": "Why NODE.",
        "home_why1_label": "SELECTION",
        "home_why1_title": "Every product tested",
        "home_why1_text": "We don't add anything we haven't used ourselves.",
        "home_why2_label": "DELIVERY",
        "home_why2_title": "Shipped from Belgium",
        "home_why2_text": "No weeks of waiting — out the door within 24 hours.",
        "home_why3_label": "WARRANTY",
        "home_why3_title": "2 years, standard",
        "home_why3_text": "On every device, no small print.",

        "product_back": "Back to shop",
        "product_add": "Add to cart",
        "product_stock": "in stock",
        "product_sold_out": "Currently out of stock",
        "product_added": "Product added to your cart.",
        "product_not_found": "Product not found.",

        "cart_title": "Your cart",
        "cart_empty": "Your cart is still empty.",
        "cart_continue": "Continue shopping",
        "cart_remove": "remove",
        "cart_total": "Total",
        "cart_checkout": "Checkout",

        "checkout_title": "Checkout",
        "checkout_subtotal": "Subtotal",
        "checkout_shipping": "Shipping",
        "checkout_free": "Free",
        "checkout_total": "Total",
        "checkout_free_from": "{amount} away from free shipping",
        "checkout_details": "Shipping details",
        "checkout_name": "Full name",
        "checkout_address": "Address",
        "checkout_postal": "Postal code",
        "checkout_city": "City",
        "checkout_country": "Country",
        "checkout_place_order": "Place order",
        "checkout_no_payment": "Note: no real payment is connected yet — this places the order "
                               "for testing purposes.",

        "success_order": "ORDER",
        "success_title": "Thanks for your order!",
        "success_text": "We've received your order of {amount} and we're getting to work on it.",
        "success_continue": "Continue shopping",

        "account_title": "My account",
        "account_logged_in": "Logged in as",
        "account_orders": "My orders",
        "account_no_orders": "You haven't placed any orders yet.",
        "account_order": "Order",
        "account_shipping_to": "Shipping to",
        "account_free": "free",

        "login_title": "Log in",
        "login_sub": "Welcome back to NODE.",
        "login_email": "Email address",
        "login_email_ph": "you@example.com",
        "login_password": "Password",
        "login_button": "Log in",
        "login_no_account": "No account yet?",
        "login_create": "Create one",
        "login_success": "You're logged in.",
        "login_failed": "Email address or password is incorrect.",
        "logout_success": "You've been logged out.",

        "register_title": "Create account",
        "register_sub": "So you can track your orders.",
        "register_name": "Name",
        "register_name_ph": "First and last name",
        "register_password_ph": "At least 6 characters",
        "register_button": "Create account",
        "register_has_account": "Already have an account?",
        "register_login": "Log in here",
        "register_success": "Account created! Welcome.",
        "register_exists": "An account with this email address already exists.",
        "register_fill_all": "Please fill in all fields.",

        "about_label": "// ABOUT US",
        "about_title": "Built by people who use the gear themselves.",
        "about_p1": "NODE. came out of frustration: too many web shops sell tech gadgets that break "
                    "after two weeks, wrapped in marketing language that says nothing about how the "
                    "product actually performs.",
        "about_p2": "We test every product for at least two weeks before it reaches the shop. No "
                    "dropship noise, no products we wouldn't buy ourselves.",
        "about_p3": "We're a small, independent team based in Belgium. Every order ships from here, "
                    "and every question is answered by an actual human.",
        "about_stat1": "FOUNDED",
        "about_stat2_num": "2 weeks",
        "about_stat2": "TESTING PER PRODUCT",
        "about_stat3": "SHIPPED FROM BELGIUM",

        "contact_label": "// CONTACT",
        "contact_title": "Question, complaint, or just an idea?",
        "contact_intro": "Fill in the form and we usually reply within one working day. For urgent "
                         "questions about an existing order, feel free to include your order number.",
        "contact_email_label": "EMAIL",
        "contact_region_label": "REGION",
        "contact_hours_label": "HOURS",
        "contact_hours": "Mon–Fri, 9:00–17:00",
        "contact_name": "Name",
        "contact_email": "Email address",
        "contact_message": "Message",
        "contact_send": "Send message",
        "contact_thanks": "Thanks for your message! We'll get back to you as soon as possible.",

        "footer_tagline": "Tech, without the noise.",
        "footer_terms": "Terms and conditions",
        "footer_privacy": "Privacy policy",
        "footer_returns": "Return policy",

        "legal_label": "// LEGAL",
        "legal_updated": "Last updated: August 2026",
        "legal_draft": "Note: this text is a working draft and still needs legal review before "
                       "the shop opens.",

        "terms_title": "Terms and conditions",
        "terms_h1": "1. Seller identity",
        "terms_h2": "2. Applicability",
        "terms_p2": "These terms and conditions apply to every order placed through this web shop. "
                    "By placing an order, the customer accepts these terms.",
        "terms_h3": "3. Prices",
        "terms_p3": "All prices are in euro and include VAT. Shipping costs are listed separately and "
                    "calculated based on the delivery address. Orders of € 75.00 or more ship free.",
        "terms_h4": "4. Orders and delivery",
        "terms_p4": "An order is concluded at the moment of confirmation. We aim to ship orders within "
                    "24 hours of payment. Delivery times are indicative and depend on the destination.",
        "terms_h5": "5. Right of withdrawal",
        "terms_p5": "Consumers have the right to withdraw from the agreement within 14 calendar days "
                    "of receiving the order, without giving a reason. See our",
        "terms_p5_link": "return policy",
        "terms_p5_end": "for the practical handling.",
        "terms_h6": "6. Warranty",
        "terms_p6": "All products carry the statutory 2-year warranty against conformity defects, "
                    "in accordance with the Belgian Code of Economic Law.",
        "terms_h7": "7. Applicable law",
        "terms_p7": "Belgian law applies to this agreement. Disputes are submitted to the competent courts.",

        "privacy_title": "Privacy policy",
        "privacy_h1": "1. Who processes your data",
        "privacy_p1": "NODE., company number [KBO number], is responsible for processing your personal "
                      "data. For questions, contact hello@nodetech.be.",
        "privacy_h2": "2. What data we collect",
        "privacy_p2": "When creating an account we store your name, email address and an encrypted "
                      "version of your password. When you place an order we also store your delivery "
                      "address and the contents of your order.",
        "privacy_h3": "3. Why we process it",
        "privacy_p3": "Solely to process and deliver your order, manage your account, and comply with "
                      "legal obligations such as bookkeeping. We don't use your data for advertising "
                      "and don't sell it to third parties.",
        "privacy_h4": "4. How long we keep it",
        "privacy_p4": "Account data is kept for as long as your account exists. Order data is kept in "
                      "line with the statutory retention period for accounting records.",
        "privacy_h5": "5. Your rights",
        "privacy_p5": "Under the GDPR you have the right to access, correct, delete and port your data, "
                      "and the right to object to processing. Email hello@nodetech.be to exercise any "
                      "of these rights.",
        "privacy_h6": "6. Cookies",
        "privacy_p6": "This site only uses functional cookies needed to keep your cart and login session "
                      "working. We use no tracking or advertising cookies.",
        "privacy_h7": "7. Complaints",
        "privacy_p7": "You have the right to lodge a complaint with the Belgian Data Protection Authority "
                      "(Drukpersstraat 35, 1000 Brussels — gegevensbeschermingsautoriteit.be).",

        "returns_title": "Return policy",
        "returns_h1": "You have 14 days to change your mind",
        "returns_p1": "As a consumer you have the right to state, within 14 calendar days of receiving "
                      "your order, that you wish to withdraw from the purchase, without giving a reason. "
                      "You then have another 14 days to send the product back.",
        "returns_h2": "How to return",
        "returns_step1": "Email hello@nodetech.be with your order number",
        "returns_step2": "You'll receive return instructions from us",
        "returns_step3": "Pack the product carefully, preferably in its original packaging",
        "returns_step4": "Send it to the address we provide",
        "returns_h3": "Conditions",
        "returns_p3": "The product must be in the same condition as when received. You may try the "
                      "product as you would in a shop, but if handling goes beyond what's needed to "
                      "establish its nature and function, we may charge for the reduction in value.",
        "returns_h4": "Refunds",
        "returns_p4": "Once we receive and inspect your return, we refund the purchase amount within "
                      "14 days, using the same payment method as the purchase. Original shipping costs "
                      "are refunded; the cost of the return shipment is yours.",
        "returns_h5": "Received a faulty or wrong product?",
        "returns_p5": "That falls under warranty rather than returns. Get in touch via",
        "returns_p5_link": "our contact page",
        "returns_p5_end": "— we'll sort it out at no cost to you.",

        "cart_login_first": "Please log in to continue.",
        "cart_is_empty": "Your cart is empty.",
    },

    # ---------------------------------------------------------------- FR
    "fr": {
        "nav_shop": "Boutique",
        "nav_about": "À propos",
        "nav_contact": "Contact",
        "nav_login": "Connexion",
        "nav_register": "Créer un compte",
        "nav_account": "Mon compte",
        "nav_logout": "Déconnexion",
        "nav_cart": "Panier",

        "home_status": "STATUT : NOUVEL ARRIVAGE",
        "home_title": "La tech, sans le bruit.",
        "home_intro": "Des appareils sélectionnés avec soin pour ceux qui savent ce qu'ils cherchent. "
                      "Pas de discours marketing, juste les specs qui comptent.",
        "home_cta": "Voir la collection",
        "home_products_title": "Cette semaine en boutique",
        "home_products_sub": "Cliquez sur un produit pour plus de détails.",
        "home_why_title": "Pourquoi NODE.",
        "home_why1_label": "SÉLECTION",
        "home_why1_title": "Chaque produit testé",
        "home_why1_text": "Nous n'ajoutons rien que nous n'ayons utilisé nous-mêmes.",
        "home_why2_label": "LIVRAISON",
        "home_why2_title": "Expédié depuis la Belgique",
        "home_why2_text": "Pas d'attente interminable — expédié sous 24 h.",
        "home_why3_label": "GARANTIE",
        "home_why3_title": "2 ans, d'office",
        "home_why3_text": "Sur chaque appareil, sans petites lignes.",

        "product_back": "Retour à la boutique",
        "product_add": "Ajouter au panier",
        "product_stock": "en stock",
        "product_sold_out": "Actuellement en rupture de stock",
        "product_added": "Produit ajouté à votre panier.",
        "product_not_found": "Produit introuvable.",

        "cart_title": "Votre panier",
        "cart_empty": "Votre panier est encore vide.",
        "cart_continue": "Continuer mes achats",
        "cart_remove": "supprimer",
        "cart_total": "Total",
        "cart_checkout": "Commander",

        "checkout_title": "Commande",
        "checkout_subtotal": "Sous-total",
        "checkout_shipping": "Livraison",
        "checkout_free": "Gratuite",
        "checkout_total": "Total",
        "checkout_free_from": "Encore {amount} pour la livraison gratuite",
        "checkout_details": "Adresse de livraison",
        "checkout_name": "Nom complet",
        "checkout_address": "Adresse",
        "checkout_postal": "Code postal",
        "checkout_city": "Ville",
        "checkout_country": "Pays",
        "checkout_place_order": "Passer la commande",
        "checkout_no_payment": "Attention : aucun paiement réel n'est encore connecté — "
                               "ceci enregistre la commande à des fins de test.",

        "success_order": "COMMANDE",
        "success_title": "Merci pour votre commande !",
        "success_text": "Nous avons bien reçu votre commande de {amount} et nous nous en occupons.",
        "success_continue": "Continuer mes achats",

        "account_title": "Mon compte",
        "account_logged_in": "Connecté en tant que",
        "account_orders": "Mes commandes",
        "account_no_orders": "Vous n'avez pas encore passé de commande.",
        "account_order": "Commande",
        "account_shipping_to": "Livraison vers",
        "account_free": "gratuite",

        "login_title": "Connexion",
        "login_sub": "Bon retour chez NODE.",
        "login_email": "Adresse e-mail",
        "login_email_ph": "vous@exemple.be",
        "login_password": "Mot de passe",
        "login_button": "Se connecter",
        "login_no_account": "Pas encore de compte ?",
        "login_create": "Créez-en un",
        "login_success": "Vous êtes connecté.",
        "login_failed": "Adresse e-mail ou mot de passe incorrect.",
        "logout_success": "Vous êtes déconnecté.",

        "register_title": "Créer un compte",
        "register_sub": "Pour suivre vos commandes.",
        "register_name": "Nom",
        "register_name_ph": "Prénom et nom",
        "register_password_ph": "Au moins 6 caractères",
        "register_button": "Créer le compte",
        "register_has_account": "Vous avez déjà un compte ?",
        "register_login": "Connectez-vous ici",
        "register_success": "Compte créé ! Bienvenue.",
        "register_exists": "Un compte existe déjà avec cette adresse e-mail.",
        "register_fill_all": "Veuillez remplir tous les champs.",

        "about_label": "// À PROPOS",
        "about_title": "Créé par des gens qui utilisent eux-mêmes le matériel.",
        "about_p1": "NODE. est né d'une frustration : trop de boutiques en ligne vendent des gadgets "
                    "qui cassent après deux semaines, emballés dans un discours marketing qui ne dit "
                    "rien des performances réelles.",
        "about_p2": "Nous testons chaque produit au moins deux semaines avant sa mise en vente. Pas "
                    "de dropshipping à l'aveugle, aucun produit que nous n'achèterions pas nous-mêmes.",
        "about_p3": "Nous sommes une petite équipe indépendante basée en Belgique. Chaque commande "
                    "part d'ici, et chaque question reçoit une réponse humaine.",
        "about_stat1": "FONDÉE EN",
        "about_stat2_num": "2 semaines",
        "about_stat2": "DE TEST PAR PRODUIT",
        "about_stat3": "EXPÉDIÉ DE BELGIQUE",

        "contact_label": "// CONTACT",
        "contact_title": "Une question, une réclamation ou juste une idée ?",
        "contact_intro": "Remplissez le formulaire et nous répondons généralement sous un jour ouvrable. "
                         "Pour une question urgente sur une commande en cours, indiquez votre numéro "
                         "de commande.",
        "contact_email_label": "E-MAIL",
        "contact_region_label": "RÉGION",
        "contact_hours_label": "HORAIRES",
        "contact_hours": "Lun–Ven, 9h00–17h00",
        "contact_name": "Nom",
        "contact_email": "Adresse e-mail",
        "contact_message": "Message",
        "contact_send": "Envoyer le message",
        "contact_thanks": "Merci pour votre message ! Nous vous répondrons dès que possible.",

        "footer_tagline": "La tech, sans le bruit.",
        "footer_terms": "Conditions générales",
        "footer_privacy": "Politique de confidentialité",
        "footer_returns": "Politique de retour",

        "legal_label": "// MENTIONS LÉGALES",
        "legal_updated": "Dernière mise à jour : août 2026",
        "legal_draft": "Attention : ce texte est une version de travail et doit encore être validé "
                       "juridiquement avant l'ouverture de la boutique.",

        "terms_title": "Conditions générales",
        "terms_h1": "1. Identité du vendeur",
        "terms_h2": "2. Champ d'application",
        "terms_p2": "Ces conditions générales s'appliquent à toute commande passée via cette boutique "
                    "en ligne. En passant commande, le client accepte ces conditions.",
        "terms_h3": "3. Prix",
        "terms_p3": "Tous les prix sont exprimés en euros, TVA comprise. Les frais de livraison sont "
                    "indiqués séparément et calculés selon l'adresse de livraison. À partir de "
                    "€ 75,00, la livraison est gratuite.",
        "terms_h4": "4. Commande et livraison",
        "terms_p4": "La commande est conclue au moment de la confirmation. Nous nous efforçons "
                    "d'expédier les commandes dans les 24 heures suivant le paiement. Les délais de "
                    "livraison sont indicatifs et dépendent de la destination.",
        "terms_h5": "5. Droit de rétractation",
        "terms_p5": "Le consommateur a le droit de se rétracter dans les 14 jours calendrier suivant "
                    "la réception de la commande, sans avoir à justifier de motif. Voir notre",
        "terms_p5_link": "politique de retour",
        "terms_p5_end": "pour les modalités pratiques.",
        "terms_h6": "6. Garantie",
        "terms_p6": "Tous les produits bénéficient de la garantie légale de 2 ans contre les défauts "
                    "de conformité, conformément au Code de droit économique belge.",
        "terms_h7": "7. Droit applicable",
        "terms_p7": "Le droit belge s'applique à cette convention. Les litiges sont soumis aux "
                    "tribunaux compétents.",

        "privacy_title": "Politique de confidentialité",
        "privacy_h1": "1. Qui traite vos données",
        "privacy_p1": "NODE., numéro d'entreprise [numéro BCE], est responsable du traitement de vos "
                      "données personnelles. Pour toute question : hello@nodetech.be.",
        "privacy_h2": "2. Quelles données nous collectons",
        "privacy_p2": "Lors de la création d'un compte, nous conservons votre nom, votre adresse e-mail "
                      "et une version chiffrée de votre mot de passe. Lors d'une commande, nous "
                      "conservons également votre adresse de livraison et le contenu de la commande.",
        "privacy_h3": "3. Pourquoi nous les traitons",
        "privacy_p3": "Uniquement pour traiter et livrer votre commande, gérer votre compte et "
                      "respecter les obligations légales telles que la comptabilité. Nous n'utilisons "
                      "pas vos données à des fins publicitaires et ne les revendons pas.",
        "privacy_h4": "4. Durée de conservation",
        "privacy_p4": "Les données de compte sont conservées tant que votre compte existe. Les données "
                      "de commande sont conservées conformément au délai légal de conservation des "
                      "pièces comptables.",
        "privacy_h5": "5. Vos droits",
        "privacy_p5": "En vertu du RGPD, vous avez le droit d'accéder à vos données, de les rectifier, "
                      "de les effacer et de les transférer, ainsi que le droit de vous opposer au "
                      "traitement. Écrivez à hello@nodetech.be pour exercer l'un de ces droits.",
        "privacy_h6": "6. Cookies",
        "privacy_p6": "Ce site n'utilise que des cookies fonctionnels nécessaires au fonctionnement de "
                      "votre panier et de votre session. Aucun cookie de suivi ou publicitaire.",
        "privacy_h7": "7. Réclamations",
        "privacy_p7": "Vous avez le droit d'introduire une réclamation auprès de l'Autorité de "
                      "protection des données (Rue de la Presse 35, 1000 Bruxelles — "
                      "autoriteprotectiondonnees.be).",

        "returns_title": "Politique de retour",
        "returns_h1": "Vous avez 14 jours pour changer d'avis",
        "returns_p1": "En tant que consommateur, vous avez le droit d'indiquer, dans les 14 jours "
                      "calendrier suivant la réception de votre commande, que vous souhaitez vous "
                      "rétracter, sans justification. Vous disposez ensuite de 14 jours "
                      "supplémentaires pour renvoyer le produit.",
        "returns_h2": "Comment retourner",
        "returns_step1": "Envoyez un e-mail à hello@nodetech.be avec votre numéro de commande",
        "returns_step2": "Vous recevrez nos instructions de retour",
        "returns_step3": "Emballez soigneusement le produit, de préférence dans son emballage d'origine",
        "returns_step4": "Renvoyez-le à l'adresse que nous vous communiquons",
        "returns_h3": "Conditions",
        "returns_p3": "Le produit doit être dans le même état qu'à la réception. Vous pouvez l'essayer "
                      "comme vous le feriez en magasin, mais en cas de manipulation allant au-delà de "
                      "ce qui est nécessaire pour en établir la nature et le fonctionnement, une "
                      "dépréciation peut être facturée.",
        "returns_h4": "Remboursement",
        "returns_p4": "Dès réception et vérification de votre retour, nous remboursons le montant de "
                      "l'achat dans les 14 jours, via le même moyen de paiement. Les frais de livraison "
                      "initiaux sont remboursés ; les frais de retour sont à votre charge.",
        "returns_h5": "Produit défectueux ou erroné ?",
        "returns_p5": "Cela relève de la garantie et non du retour. Contactez-nous via",
        "returns_p5_link": "notre page de contact",
        "returns_p5_end": "— nous réglons cela sans frais pour vous.",

        "cart_login_first": "Connectez-vous d'abord pour continuer.",
        "cart_is_empty": "Votre panier est vide.",
    },
}


def translate(key, lang, **kwargs):
    """Haalt een vertaling op. Valt terug op Nederlands, dan op de sleutel zelf."""
    table = TRANSLATIONS.get(lang) or TRANSLATIONS[DEFAULT_LANGUAGE]
    text = table.get(key) or TRANSLATIONS[DEFAULT_LANGUAGE].get(key) or key
    if kwargs:
        try:
            text = text.format(**kwargs)
        except (KeyError, IndexError):
            pass
    return text
