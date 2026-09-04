"""Alle Inhalte der Seite an einer Stelle.

Firmendaten (NAP), Leistungen, Einzugsgebiet, Team, Fuhrpark und Galerie.
Wer Telefon, Adresse oder Leistungstexte ändert, ändert sie hier – nirgendwo sonst.
"""

FIRMA = {
    "name": "BLITZ-ZAUN",
    "zusatz": "Garten- und Landschaftsbau",
    "inhaber": "Murat Bayram",
    "strasse": "Leipziger Straße 4",
    "plz": "63526",
    "ort": "Erlensee",
    # Festnetz 06183 898811 ist seit 09/2026 abgeschaltet (Info vom Kunden). Beide Nummern sind mobil.
    "telefon": "0157 73 51 36 95",
    "telefon_link": "+4915773513695",
    "mobil": "0163 57 23 771",
    "mobil_link": "+4916357237711",
    "whatsapp": "4916357237711",
    "email": "info@blitz-zaun.de",
    "steuernummer": "22 804 61 638",
    "finanzamt": "Finanzamt Hanau",
    "slogan": "Blitzschnell für Sie im Einsatz, zuverlässig und preiswert.",
    "maps_link": "https://www.google.com/maps/search/?api=1&query=Leipziger+Stra%C3%9Fe+4%2C+63526+Erlensee",
}

# Einzugsgebiet, Reihenfolge nach Nähe zu Erlensee
ORTE = [
    "Erlensee", "Hanau", "Langenselbold", "Rodenbach", "Bruchköbel", "Neuberg",
    "Hasselroth", "Gelnhausen", "Freigericht", "Maintal", "Nidderau", "Großkrotzenburg",
]
REGION = "Main-Kinzig-Kreis"

# Fünf Gruppen, vierzehn Leistungen – entspricht der Liste der bisherigen Seite.
LEISTUNGSGRUPPEN = [
    {
        "slug": "zaunbau",
        "titel": "Zaunbau und L-Steine",
        "kurz": "Doppelstab\u00admatten\u00adzäune, Tore und Pfosten – auch auf L-Steinen, wenn das Gelände Höhenunterschiede hat.",
        "bild": "i9ece2051e20113d1",
        "leistungen": [
            {
                "name": "Zaunbau",
                "text": "Wir bauen Ihren Zaun nach Ihren Wünschen: Doppelstabmatten in Anthrazit oder Grün, passende Tore und Türen, Pfosten einbetoniert oder auf L-Steinen. Wir verwenden nur Zaunelemente, die viele Jahre halten.",
                "link": "leistungen/zaunbau/",
            },
            {
                "name": "L-Steine",
                "text": "Um Höhenunterschiede im Gelände abzufangen, setzen wir L-Steine in allen Größen. Oft sitzt der neue Zaun direkt darauf – dann sind Stützmauer und Zaun in einem Arbeitsgang fertig.",
            },
        ],
    },
    {
        "slug": "pflaster",
        "titel": "Pflaster, Wege und Garten",
        "kurz": "Vom Garagen\u00advorplatz bis zur Terrasse mit Verlegemuster, dazu Wege, Treppen, Stellplätze und Rollrasen.",
        "bild": "icd3917b9aa3559df",
        "leistungen": [
            {
                "name": "Pflasterarbeiten",
                "text": "Einfache Garagenvorplätze oder aufwendige Verlegemuster: Wir bereiten den Unterbau vor, verlegen Betonstein oder Naturstein und fugen sauber ein. Damit die Fläche auch nach Jahren noch eben liegt.",
            },
            {
                "name": "Terrassenbau",
                "text": "Kleine oder große Terrassen in der Form, die zu Ihrem Haus passt. Wir planen gemeinsam mit Ihnen Größe, Belag und Anschluss an den Garten und bauen dann alles aus einer Hand.",
            },
            {
                "name": "Wegebau",
                "text": "Gartenwege, Zugänge zur Haustür und Einfahrten mit tragfähigem Unterbau und sauberen Randsteinen, damit nichts absackt und Regenwasser abfließt.",
            },
            {
                "name": "Treppenbau",
                "text": "Außentreppen aus Blockstufen oder Winkelstufen, passend zu Terrasse und Weg. Wir richten Steigung und Auftritt so ein, dass die Treppe bequem und sicher zu gehen ist.",
            },
            {
                "name": "Parkplatzbau",
                "text": "Stellplätze und Parkflächen für Wohnhäuser und Gewerbe, gepflastert oder mit Rasengittersteinen. Auf Wunsch mit Entwässerung und Beleuchtungsleerrohren.",
            },
            {
                "name": "Rollrasenverlegung",
                "text": "Sie wollen schnell einen schönen, begehbaren Rasen. Dann ist Rollrasen die erste Wahl. Wir bereiten den Boden vor, verlegen den Rasen und sagen Ihnen, wie Sie ihn in den ersten Wochen pflegen.",
            },
        ],
    },
    {
        "slug": "erdarbeiten",
        "titel": "Erd- und Baggerarbeiten",
        "kurz": "Baugruben, Aushub und Gelände\u00admodellierung mit eigenen Baggern. Boden, Sand, Kies und Schotter liefern wir mit dem eigenen Kipper.",
        "bild": "i460588a49b0b7cd8",
        "leistungen": [
            {
                "name": "Erdarbeiten",
                "text": "Mit unserem eigenen Kipplaster bewegen wir schnell große Erdmengen. Ob Mutterboden, Sand, Kies oder Schotter: Wir liefern das Material direkt zur Baustelle und nehmen Aushub mit.",
            },
            {
                "name": "Baggerarbeiten",
                "text": "Unser erfahrenes Team schachtet exakte Baugruben aus und übernimmt alle anderen Baggerarbeiten: Fundamente, Leitungsgräben, Planum für Pflaster oder Terrasse.",
            },
        ],
    },
    {
        "slug": "kanal",
        "titel": "Kanal, Zisterne und Keller",
        "kurz": "Neue Kanal\u00adanschlüsse, Sanierung alter Leitungen, Regen\u00adwasser\u00adzisternen und trockene Kellerwände.",
        "bild": "i98c6149be7ec473d",
        "leistungen": [
            {
                "name": "Kanal- und Zisternenarbeiten",
                "text": "Wir bauen Kanalsysteme neu oder sanieren vorhandene Anlagen in jeder Größe. Zisternen zur Nutzung des Regenwassers in Haus und Garten setzen wir einschließlich Aushub, Anschluss und Überlauf.",
            },
            {
                "name": "Kellerwandsanierung",
                "text": "Feuchte Kellerwände legen wir von außen frei, reinigen die Wand, bringen die Abdichtung auf und verfüllen den Graben wieder fachgerecht mit Drainage.",
            },
        ],
    },
    {
        "slug": "abbruch",
        "titel": "Abbruch und Container",
        "kurz": "Vom alten Weg bis zur Scheune: Wir brechen ab, laden auf und entsorgen. Container stellen wir mit dem eigenen LKW.",
        "bild": "i44b4a2db62fc5dc0",
        "leistungen": [
            {
                "name": "Abbrucharbeiten",
                "text": "Wir übernehmen jede Art von Abbrucharbeiten: ein altes Haus, eine alte Scheune, ein asphaltierter Weg oder eine Betonplatte. Der Schutt geht direkt in unsere Container.",
            },
            {
                "name": "Containerdienst",
                "text": "Wenn Sie einen Container zur Abfallentsorgung benötigen, stellen wir ihn mit unserem eigenen LKW auf und holen ihn wieder ab – für Bauschutt, Erde oder Grünschnitt.",
            },
        ],
    },
]

# Der Ablauf einer Anfrage – eine echte Reihenfolge, daher nummeriert.
ABLAUF = [
    {"titel": "Sie melden sich", "text": "Per Anruf oder WhatsApp. Sagen Sie kurz, was ansteht, und schicken Sie gern ein Foto vom Grundstück."},
    {"titel": "Wir schauen es uns an", "text": "Vor Ort messen wir aus, prüfen Untergrund und Zufahrt und besprechen mit Ihnen, was sinnvoll ist."},
    {"titel": "Sie bekommen ein Angebot", "text": "Schriftlich, mit allen Positionen. Erst wenn Sie zustimmen, planen wir den Termin."},
    {"titel": "Wir bauen", "text": "Mit eigenem Team, eigenen Baggern und LKW. Am Ende gehen wir die Arbeit gemeinsam mit Ihnen ab."},
]

TEAM = [
    {"name": "Murat Bayram", "rolle": "Inhaber", "bild": "ida64f53a9a170fb3"},
    {"name": "Cevdet Bayram", "rolle": "Projektleitung und Kundenbetreuung", "bild": "ia813b48ec2f87b31", "mobil": True},
]

# Drei Bagger, drei LKW – so steht es auf der bisherigen Seite. Freisteller aus Jimdo.
FUHRPARK = [
    {"name": "Minibagger", "art": "Bagger", "text": "Kommt durch jede Gartenpforte, für Zaunfundamente und kleine Gräben.", "bild": "id028dfbbafa15b3f"},
    {"name": "Kompaktbagger", "art": "Bagger", "text": "Für Baugruben, Planum und Aushub auf normalen Baustellen.", "bild": "i80321ac417c91eee"},
    {"name": "Kompaktbagger", "art": "Bagger", "text": "Zweite Maschine, damit zwei Baustellen parallel laufen können.", "bild": "iea0819e79043eaf4"},
    {"name": "Abrollkipper", "art": "LKW", "text": "Bringt Container und holt Schutt und Aushub ab.", "bild": "i43707fbc6238e19a"},
    {"name": "Pritschenwagen", "art": "LKW", "text": "Für Zaunelemente, Werkzeug und Kleinmaterial.", "bild": "i9b6dd78746cd9eab"},
    {"name": "Kipper", "art": "LKW", "text": "Liefert Boden, Sand, Kies und Schotter direkt zur Baustelle.", "bild": "icd2a48c381bb71eb"},
]

# Galerie-Kategorien in Anzeigereihenfolge
KATEGORIEN = {
    "zaun": "Zaunbau",
    "erde": "L-Steine und Erdarbeiten",
    "pflaster": "Pflaster, Wege und Rasen",
    "bagger": "Bagger und Fuhrpark",
    "kanal": "Abbruch, Kanal und Zisterne",
}

GALERIE = [
    {"id": "i9ece2051e20113d1", "kat": "zaun", "alt": "Doppelstabmattenzaun in Anthrazit entlang eines Rapsfelds"},
    {"id": "i460588a49b0b7cd8", "kat": "bagger", "alt": "Gelber Minibagger beim Zaunbau vor einem Neubau"},
    {"id": "icd3917b9aa3559df", "kat": "pflaster", "alt": "Verlegte Betonpflastersteine im Reihenverband"},
    {"id": "i1193aaeaab4db8a8", "kat": "zaun", "alt": "Zwei Mitarbeiter richten Zaunpfosten auf L-Steinen aus"},
    {"id": "i81c21412d83234ba", "kat": "zaun", "alt": "Detail eines Zaunpfostens mit Pfostenkappe und Mattenhalter"},
    {"id": "ibbb28b63d24b9081", "kat": "zaun", "alt": "Minibagger und neue Zaunpfosten am Rand eines Rapsfelds"},
    {"id": "i362212e20475302e", "kat": "bagger", "alt": "Bagger beim Aushub neben einem Neubau"},
    {"id": "i42bd650df98b1283", "kat": "zaun", "alt": "Doppelstabmattenzaun auf L-Steinen entlang der Grundstücksgrenze"},
    {"id": "i04906e36a2ac57b1", "kat": "erde", "alt": "Minibagger und gestapelte L-Steine auf einer Baustelle im Neubaugebiet"},
    {"id": "i3870e95efe9a9b24", "kat": "pflaster", "alt": "Mitarbeiter mit Nivellierlatte auf frisch gepflasterter Fläche"},
    {"id": "i12931cfebce9f13d", "kat": "zaun", "alt": "Frisch gesetzte Zaunpfosten auf L-Stein-Fundament vor einem Einfamilienhaus"},
    {"id": "i63f29034614721f1", "kat": "bagger", "alt": "Roter Kompaktbagger beim Aushub neben einem Wohnhaus"},
    {"id": "i445d1f5028b25ba2", "kat": "erde", "alt": "Palettierte L-Steine, bereit zum Versetzen"},
    {"id": "i2be7e555e4e20719", "kat": "zaun", "alt": "Doppelstabmattenzaun entlang eines gepflasterten Wegs"},
    {"id": "i98c6149be7ec473d", "kat": "kanal", "alt": "Betonschachtringe für den Kanalbau"},
    {"id": "i1276c9205b150646", "kat": "bagger", "alt": "Abrollkipper mit Container auf dem Weg zur Baustelle"},
    {"id": "i7dc81f74d219b23a", "kat": "zaun", "alt": "Zaunpfosten wird in Beton gesetzt"},
    {"id": "i90d8d99740e52d94", "kat": "pflaster", "alt": "Gesetzte Randsteine als Einfassung für einen Weg"},
    {"id": "i4d4279d2b52017b6", "kat": "bagger", "alt": "Minibagger und Mitarbeiter beim Setzen von Zaunpfosten"},
    {"id": "i3cb6597933c816ad", "kat": "kanal", "alt": "Aufgebrochener Asphalt bei Abbrucharbeiten"},
    {"id": "i319dda285d53974b", "kat": "zaun", "alt": "Zaunpfosten auf L-Stein, Detail der Verankerung"},
    {"id": "ibf56fee4e8bddc2e", "kat": "erde", "alt": "Angelieferter Mutterboden vor einem Neubau"},
    {"id": "i235822fb58701d01", "kat": "zaun", "alt": "Anthrazitfarbener Zaunpfosten mit Abdeckkappe, Nahaufnahme"},
    {"id": "i44b4a2db62fc5dc0", "kat": "kanal", "alt": "LKW mit Abrollcontainer für Bauschutt"},
    {"id": "ia143efaf7ae8fea0", "kat": "erde", "alt": "Minibagger versetzt L-Steine vor einem Neubau"},
    {"id": "i68f3c799ceed526e", "kat": "zaun", "alt": "Zaunpfosten auf L-Stein, Ansicht von der Gartenseite"},
    {"id": "i63ee4c542f74b966", "kat": "bagger", "alt": "Minibagger beim Aushub für ein Zaunfundament"},
    {"id": "ibbf3aab9d0685beb", "kat": "pflaster", "alt": "Frisch verlegter Rollrasen"},
    {"id": "iabceafc5db8da338", "kat": "zaun", "alt": "Zaun auf L-Steinen entlang einer Hauseinfahrt"},
    {"id": "i65de2cddd330cd59", "kat": "kanal", "alt": "Betonzisterne vor dem Einbau"},
    {"id": "i7ff075817999d2a0", "kat": "bagger", "alt": "Mitarbeiter und Minibagger auf einer Baustelle mit L-Steinen"},
    {"id": "ia917902d6fc021bb", "kat": "zaun", "alt": "Zaunpfosten mit Pfostenkappe, Nahaufnahme"},
    {"id": "i3c3e4f4fbc7d36c2", "kat": "erde", "alt": "Erdhaufen aus Mutterboden auf einer Baustelle"},
    {"id": "i88f02694a57eebfd", "kat": "bagger", "alt": "Minibagger bei Erdarbeiten vor einem Rohbau"},
    {"id": "ie7d3857cafcef776", "kat": "zaun", "alt": "Zaunpfosten in einer Reihe auf L-Steinen, vorbereitet für die Matten"},
    {"id": "i1af7035b7d649993", "kat": "bagger", "alt": "Pritschenwagen vor einem Neubau"},
    {"id": "i8a9dec25dfa0dc15", "kat": "bagger", "alt": "Kompaktbagger und Mitarbeiter mit Nivellierlatte beim Aushub"},
    {"id": "ic691558827d9d09f", "kat": "zaun", "alt": "Zaunfeld auf L-Stein-Sockel vor einem Wohnhaus"},
    {"id": "iffed7a66d2e7579c", "kat": "erde", "alt": "Aushub und Schotterbett für ein L-Stein-Fundament"},
    {"id": "i7cc6c2dd75f2a0d5", "kat": "zaun", "alt": "Anthrazitfarbener Zaunpfosten mit Doppelstabmatte"},
    {"id": "idb133e1ae2203432", "kat": "bagger", "alt": "Roter Kompaktbagger beim Aushub"},
    {"id": "if2c9b79c5d1783bf", "kat": "erde", "alt": "L-Steine und Minibagger vor Baubeginn"},
    {"id": "ie8c32ce344e0f796", "kat": "kanal", "alt": "LKW mit Abrollcontainer für Bauschutt und Aushub"},
    {"id": "i73ba2be2bb91490f", "kat": "erde", "alt": "L-Steine auf Paletten am Straßenrand"},
]

# Fragen, die bei fast jeder Zaun-Anfrage kommen
ZAUN_FAQ = [
    {
        "frage": "Welche Zäune bauen Sie?",
        "antwort": "Vor allem Doppelstabmattenzäune in Anthrazit oder Grün, mit passenden Toren und Türen. Auf Wunsch mit Sichtschutzstreifen. Andere Zaunarten besprechen wir gern bei der Besichtigung.",
    },
    {
        "frage": "Mein Grundstück liegt höher als das des Nachbarn. Geht da ein Zaun?",
        "antwort": "Ja. Wir fangen den Höhenunterschied mit L-Steinen ab und setzen den Zaun direkt auf die Steine. Stützmauer und Zaun entstehen so in einem Arbeitsgang.",
    },
    {
        "frage": "Brauche ich eine Genehmigung für den Zaun?",
        "antwort": "Zäune sind in Hessen bis zu einer bestimmten Höhe meist genehmigungsfrei. Bebauungsplan und Nachbarrecht können aber Vorgaben zu Höhe und Grenzabstand machen. Wir klären das bei der Besichtigung mit Ihnen.",
    },
    {
        "frage": "Was kostet ein Zaun?",
        "antwort": "Das hängt von Länge, Höhe, Untergrund und Fundament ab. Nach der Besichtigung bekommen Sie ein schriftliches Angebot mit allen Positionen, an dem wir uns festhalten lassen.",
    },
    {
        "frage": "Wie lange dauert der Zaunbau?",
        "antwort": "Das richtet sich nach Länge und Untergrund. Bei der Besichtigung nennen wir Ihnen einen realistischen Zeitrahmen und halten den Termin dann ein.",
    },
]

# Welche Fotos wofür (Hero, OG-Bild, Zaunbau-Seite) – IDs aus bilder/original/
BILDER = {
    "hero_start": "i9ece2051e20113d1",
    "hero_zaunbau": "ibbb28b63d24b9081",
    "og": "i9ece2051e20113d1",
    "ueber_uns": "i1193aaeaab4db8a8",
    "logo": "ieb212e97aabeef4f",
}
