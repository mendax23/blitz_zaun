# BLITZ-ZAUN

Website des Garten- und Landschaftsbaubetriebs BLITZ-ZAUN, Murat Bayram, Erlensee.
Statische Seite: Jinja2-Templates werden per `build.py` nach `dist/` gerendert und
über GitHub Actions auf GitHub Pages veröffentlicht. Kein Server, keine Datenbank,
keine Kosten außer der Domain.

Vorschau: https://mendax23.github.io/blitz_zaun/ (bis zum Domain-Umzug, siehe unten)
Ziel: https://blitz-zaun.de

---

## Schnellstart

```bash
pip install -r requirements.txt
python3 build.py          # rendert nach dist/
python3 pruefen.py        # Links, Bilder, JSON-LD, Sitemap, Platzhalter
python3 -m http.server 8000 --directory dist
```

Vor jedem Push beide Skripte laufen lassen. Die CI baut und prüft ohnehin, aber ein
roter Build ist schneller lokal gefunden.

---

## Aufbau

```
build.py              rendert Templates, schreibt sitemap.xml, robots.txt, 404.html
pruefen.py            Tests gegen dist/ – laufen in der CI vor dem Deploy
bilder_import.py      Originale → WebP nach static/img/, schreibt inhalt/bilder_masse.json
inhalt/daten.py       ← alle Inhalte: Firmendaten, Leistungen, Team, Fuhrpark, Galerie, FAQ
inhalt/bilder_masse.json  Breite/Höhe jeder Bilddatei (für width/height im HTML)
templates/            base.html, Seiten, includes/ (Icons, CTA, Kontaktknöpfe)
static/css/style.css  Design-System: Variablen ganz oben
static/js/main.js     Navigation, Galerie-Filter, Lightbox – ohne Abhängigkeiten
static/fonts/         Jost (Überschriften) und Inter (Text), selbst gehostet
static/img/           optimierte Bilder (im Repo), Originale liegen lokal in bilder/original/
bilder/jimdo_quellen.txt  URLs der Originalfotos auf der alten Jimdo-Seite
.ralph/               Aufgabenplan, mit dem die Seite gebaut wurde
```

### Wo was geändert wird

| Änderung | Datei |
|---|---|
| Telefon, Adresse, E-Mail, WhatsApp-Nummer | `inhalt/daten.py` → `FIRMA` |
| Einzugsgebiet | `inhalt/daten.py` → `ORTE` |
| Leistungstexte, neue Leistung, Gruppierung | `inhalt/daten.py` → `LEISTUNGSGRUPPEN` |
| Team, Fuhrpark | `inhalt/daten.py` → `TEAM`, `FUHRPARK` |
| Galeriefoto hinzufügen | Original nach `bilder/original/`, Eintrag in `GALERIE`, dann `python3 bilder_import.py` |
| Fragen auf der Zaunbau-Seite | `inhalt/daten.py` → `ZAUN_FAQ` |
| Seitentitel, Meta-Beschreibungen | `build.py` → `SEITEN` |
| Farben, Abstände, Schrift | `static/css/style.css` (Variablen in `:root`) |
| Neue Seite | Template anlegen, Eintrag in `SEITEN`, Link in `base.html` |

---

## Bilder

Alle Fotos stammen von der alten Jimdo-Seite (Fotografie Studio Seikel, Hanau) und liegen
lokal unter `bilder/original/` (nicht im Repo, 75 MB). `bilder/jimdo_quellen.txt` listet die
Quell-URLs, solange die Jimdo-Seite noch online ist.

`python3 bilder_import.py` erzeugt aus den Originalen:

- Galerie: 1600 px für die Lightbox, 640 px im Format 4:3 für die Kacheln
- Hero-Bilder in 1400 und 800 px, Gruppenbilder 800 px, OG-Bild 1200×630 als JPEG
- Team und Fuhrpark: 300 px, Logo als PNG mit transparentem Hintergrund

Neue Fotos: Original ablegen, in `GALERIE` mit Kategorie und Alt-Text eintragen, Import laufen
lassen, die neuen WebP-Dateien mit committen.

---

## Kontakt ohne Formular

Die Seite hat bewusst kein Kontaktformular. Ohne Server gäbe es dafür nur Drittanbieter
(Formspree, Web3Forms), die einen Account des Kunden und einen Passus in der
Datenschutzerklärung brauchen. Stattdessen: Anruf, WhatsApp und E-Mail, auf dem Handy als
feste Leiste unten. Für einen GaLaBau-Betrieb ist das der kürzere Weg, und Fotos vom Grundstück
kommen gleich mit.

Falls später doch ein Formular gewünscht ist: Web3Forms (kostenlos, Access Key per E-Mail
an info@blitz-zaun.de) in `templates/kontakt.html` einbauen und Abschnitt in
`templates/datenschutz.html` ergänzen.

---

## SEO

Eingebaut: `LocalBusiness`-JSON-LD auf jeder Seite mit Einzugsgebiet, `Service`- und
`FAQPage`-JSON-LD auf der Zaunbau-Seite, Canonicals, Open Graph mit Bild, `sitemap.xml`,
`robots.txt`, `width`/`height` an jedem Bild, selbst gehostete Schriften, keine CDNs.

Nach dem Livegang: Google Search Console einrichten, Sitemap einreichen,
Google-Unternehmensprofil prüfen oder anlegen (Adresse, Telefon, Fotos aus der Galerie).

---

## Deployment

Push auf `master` → GitHub Actions: `build.py`, `pruefen.py`, Upload nach GitHub Pages.
Der Workflow steht in `.github/workflows/deploy.yml`. Pages ist im Repo auf die Quelle
„GitHub Actions" gestellt.

### Domain-Umzug auf blitz-zaun.de

Die Domain liegt seit 2014 bei Strato und leitet heute per Frame auf `blitz-zaun.jimdo.de`,
was nicht mehr funktioniert (TLS-Fehler). Für den Umzug:

1. **Strato, DNS für blitz-zaun.de:**
   - `A`-Records für `@` auf `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` für `www` auf `mendax23.github.io`
   - Frame-Weiterleitung bei Strato löschen. MX-Records (Mail) unverändert lassen.
2. **GitHub, Repo-Einstellungen → Pages:** Custom domain `blitz-zaun.de` eintragen,
   nach der DNS-Prüfung „Enforce HTTPS" aktivieren.
3. **Workflow umstellen** (`.github/workflows/deploy.yml`, Block `env`):
   `BLITZ_SITE_URL: https://blitz-zaun.de`, `BLITZ_BASE_PATH: ""`, `BLITZ_PREVIEW: "0"`,
   `BLITZ_DOMAIN: blitz-zaun.de`. Push → die Seite ist live, indexierbar, mit Sitemap.
4. **Jimdo-Seite löschen** oder wenigstens offline nehmen, sonst doppelter Inhalt.
5. Search Console und Unternehmensprofil (siehe SEO).

Offene Punkte beim Kunden: `ZUGANGSDATEN.md`.
