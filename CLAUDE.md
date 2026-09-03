# BLITZ-ZAUN – Hinweise für die Arbeit am Projekt

Statische Firmenwebsite eines GaLaBau-Betriebs in Erlensee. Jinja2 + `build.py` → `dist/`,
GitHub Pages. Kein Server, kein Formular, kein CSS-Framework, keine CDNs.
Aufbau und Pflege stehen in `README.md`, offene Punkte beim Kunden in `ZUGANGSDATEN.md`.

## Regeln

- **Inhalte nur in `inhalt/daten.py` ändern**, nicht in den Templates. NAP (Name, Adresse,
  Telefon) muss auf jeder Seite identisch sein.
- **Nichts erfinden.** Keine Zahlen („seit 20 Jahren"), keine Kundenstimmen, keine Festpreise,
  keine Maschinen-Spezifikationen, die nicht vom Kunden kommen. Preise immer als „nach Besichtigung".
- **Keine Stockfotos.** Nur eigene Baustellen- und Fahrzeugfotos aus `bilder/original/`.
- **Tonalität:** Sie-Form, kurz, bodenständig. Der Betrieb sagt „blitzschnell" über sich, mehr
  Werbesprech verträgt die Seite nicht.
- **Deutsche Umlaute korrekt**, auch in Alt-Texten und Meta-Beschreibungen.
- **Jinja kennt keine List Comprehensions.** Listen für JSON-LD werden in `build.py` gebaut
  (`orte_ld`, `faq_ld`) und als Globals übergeben.
- **StrictUndefined ist an.** Jedes Feld, das ein Template liest, muss existieren; optionale
  Felder mit `is defined` prüfen (siehe `l.link`, `p.mobil`).
- **JSON-LD läuft durch `tojson_ld`**, das die Ausgabe als `Markup` markiert. Sonst escaped
  autoescape die Anführungszeichen und `pruefen.py` schlägt an.
- **Vorschau vs. Livegang** steuern nur die vier `BLITZ_*`-Variablen im Workflow.
  `BLITZ_SITE_URL` ist nur Schema und Host, der Pfad kommt aus `BLITZ_BASE_PATH`.
- Lokal testen mit einem freien Port. Auf 8765 läuft auf diesem Rechner oft ein Django-Devserver
  eines anderen Kundenprojekts.

## Vor dem Commit

```bash
python3 build.py && python3 pruefen.py
```
