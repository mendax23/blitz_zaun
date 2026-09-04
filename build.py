#!/usr/bin/env python3
"""Rendert die Seite aus templates/ und inhalt/ nach dist/.

Umgebungsvariablen:
  BLITZ_SITE_URL   Nur Schema und Host, ohne Pfad (Standard https://blitz-zaun.de)
  BLITZ_BASE_PATH  Pfadpräfix, wenn die Seite in einem Unterordner liegt (z. B. /blitz_zaun
                   für die Vorschau unter https://mendax23.github.io/blitz_zaun/)
  BLITZ_PREVIEW    "1" → noindex und robots.txt sperrt alles (Vorschau vor dem Domain-Umzug)
  BLITZ_DOMAIN     Wenn gesetzt, wird eine CNAME-Datei für GitHub Pages geschrieben
"""
import datetime as dt
import json
import os
import shutil
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from markupsafe import Markup

WURZEL = Path(__file__).resolve().parent
sys.path.insert(0, str(WURZEL))
from inhalt import daten  # noqa: E402

DIST = WURZEL / "dist"
SITE_URL = os.environ.get("BLITZ_SITE_URL", "https://blitz-zaun.de").rstrip("/")
BASE_PATH = os.environ.get("BLITZ_BASE_PATH", "").rstrip("/")
PREVIEW = os.environ.get("BLITZ_PREVIEW", "") == "1"
DOMAIN = os.environ.get("BLITZ_DOMAIN", "").strip()

# pfad "" ist die Startseite, sonst immer mit abschließendem Slash → dist/<pfad>/index.html
SEITEN = [
    {"pfad": "", "template": "index.html",
     "titel": "Zaunbau, Pflaster und Erdarbeiten in Erlensee und Hanau",
     "beschreibung": "BLITZ-ZAUN baut Zäune, pflastert Einfahrten und Terrassen und übernimmt Erd-, Bagger- und Kanalarbeiten. Familienbetrieb aus Erlensee mit eigenen Baggern und LKW."},
    {"pfad": "leistungen/", "template": "leistungen.html",
     "titel": "Leistungen: Zaun, Pflaster, Erdarbeiten, Kanal, Abbruch",
     "beschreibung": "Vierzehn Leistungen aus einer Hand: Zaunbau, L-Steine, Pflaster, Terrassen, Wege, Treppen, Erd- und Baggerarbeiten, Kanal, Zisterne, Kellerwandsanierung, Abbruch, Container, Rollrasen."},
    {"pfad": "leistungen/zaunbau/", "template": "zaunbau.html",
     "titel": "Zaunbau in Erlensee, Hanau und Umgebung",
     "beschreibung": "Doppelstabmattenzaun mit Tor, einbetoniert oder auf L-Steinen. Besichtigung vor Ort, schriftliches Angebot, Ausführung mit eigenem Team. BLITZ-ZAUN aus Erlensee."},
    {"pfad": "galerie/", "template": "galerie.html",
     "titel": "Galerie: Zäune, Pflaster und Baustellen",
     "beschreibung": "Fotos von unseren Baustellen: Doppelstabmattenzäune, L-Steine, Pflasterflächen, Erdarbeiten und unser Fuhrpark."},
    {"pfad": "ueber-uns/", "template": "ueber_uns.html",
     "titel": "Über uns: Familienbetrieb mit eigenem Fuhrpark",
     "beschreibung": "BLITZ-ZAUN ist ein Familienbetrieb aus Erlensee. Murat Bayram und Cevdet Bayram planen und bauen mit eigenem Team, drei Baggern und drei LKW."},
    {"pfad": "kontakt/", "template": "kontakt.html",
     "titel": "Kontakt: Anrufen oder per WhatsApp schreiben",
     "beschreibung": "BLITZ-ZAUN, Leipziger Straße 4, 63526 Erlensee. Telefon 0157 73 51 36 95, WhatsApp 0163 57 23 771."},
    {"pfad": "impressum/", "template": "impressum.html", "titel": "Impressum", "beschreibung": "Anbieterkennzeichnung von BLITZ-ZAUN, Murat Bayram, Erlensee.", "noindex": True},
    {"pfad": "datenschutz/", "template": "datenschutz.html", "titel": "Datenschutzerklärung", "beschreibung": "Datenschutzerklärung der Website blitz-zaun.de.", "noindex": True},
    {"pfad": "404.html", "template": "404.html", "titel": "Seite nicht gefunden", "beschreibung": "Diese Seite gibt es nicht.", "noindex": True, "datei": True},
]


for _s in SEITEN:
    _s.setdefault("noindex", False)
    _s.setdefault("datei", False)


def url(pfad: str = "") -> str:
    """Interner Link mit Basispfad. url('leistungen/') → '/leistungen/'."""
    pfad = pfad.lstrip("/")
    return f"{BASE_PATH}/{pfad}"


def asset(pfad: str) -> str:
    return f"{BASE_PATH}/static/{pfad.lstrip('/')}"


def absolut(pfad: str = "") -> str:
    return f"{SITE_URL}{url(pfad)}"


def lade_masse() -> dict:
    datei = WURZEL / "inhalt" / "bilder_masse.json"
    return json.loads(datei.read_text()) if datei.exists() else {}


def render_alle() -> list[Path]:
    env = Environment(
        loader=FileSystemLoader(WURZEL / "templates"),
        undefined=StrictUndefined,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals.update(
        url=url, asset=asset, absolut=absolut,
        firma=daten.FIRMA, orte=daten.ORTE, region=daten.REGION,
        gruppen=daten.LEISTUNGSGRUPPEN, ablauf=daten.ABLAUF, team=daten.TEAM,
        fuhrpark=daten.FUHRPARK, kategorien=daten.KATEGORIEN, galerie=daten.GALERIE,
        zaun_faq=daten.ZAUN_FAQ, bilder=daten.BILDER, masse=lade_masse(),
        orte_ld=[{"@type": "City", "name": o} for o in daten.ORTE],
        faq_ld=[{"@type": "Question", "name": f["frage"], "acceptedAnswer": {"@type": "Answer", "text": f["antwort"]}} for f in daten.ZAUN_FAQ],
        preview=PREVIEW, site_url=SITE_URL, jahr=dt.date.today().year,
        seiten=[s for s in SEITEN if not s.get("datei")],
    )
    # JSON-LD darf nicht HTML-escaped werden; "</" trotzdem entschärfen
    env.filters["tojson_ld"] = lambda o: Markup(json.dumps(o, ensure_ascii=False, indent=2).replace("</", "<\\/"))

    geschrieben = []
    for seite in SEITEN:
        ziel = DIST / seite["pfad"] if seite.get("datei") else DIST / seite["pfad"] / "index.html"
        ziel.parent.mkdir(parents=True, exist_ok=True)
        html = env.get_template(seite["template"]).render(seite=seite)
        ziel.write_text(html, encoding="utf-8")
        geschrieben.append(ziel)
    return geschrieben


def schreibe_sitemap() -> None:
    heute = dt.date.today().isoformat()
    zeilen = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for s in SEITEN:
        if s.get("noindex") or s.get("datei"):
            continue
        zeilen.append(f"  <url><loc>{absolut(s['pfad'])}</loc><lastmod>{heute}</lastmod></url>")
    zeilen.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(zeilen) + "\n", encoding="utf-8")


def schreibe_robots() -> None:
    if PREVIEW:
        text = "User-agent: *\nDisallow: /\n"
    else:
        text = f"User-agent: *\nAllow: /\nDisallow: /impressum/\nDisallow: /datenschutz/\n\nSitemap: {absolut('sitemap.xml')}\n"
    (DIST / "robots.txt").write_text(text, encoding="utf-8")


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(WURZEL / "static", DIST / "static")
    seiten = render_alle()
    schreibe_sitemap()
    schreibe_robots()
    (DIST / ".nojekyll").write_text("")
    if DOMAIN:
        (DIST / "CNAME").write_text(DOMAIN + "\n")
    print(f"{len(seiten)} Seiten nach {DIST.relative_to(WURZEL)}/ gerendert"
          f" (SITE_URL={SITE_URL}, BASE_PATH={BASE_PATH or '/'}, PREVIEW={PREVIEW})")


if __name__ == "__main__":
    main()
