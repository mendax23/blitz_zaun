#!/usr/bin/env python3
"""Prüft dist/ nach dem Build. Beendet mit Fehlercode, wenn etwas nicht stimmt."""
import json
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

WURZEL = Path(__file__).resolve().parent
DIST = WURZEL / "dist"
BASE_PATH = os.environ.get("BLITZ_BASE_PATH", "").rstrip("/")
VERBOTEN = ["{{", "{%", "[bitte", "Lorem ipsum", "TODO", "PLATZHALTER", "lorem",
            "0 61 83", "6183898811", "06183"]  # Festnetz ist abgeschaltet
fehler: list[str] = []


class Sammler(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.bilder, self.ids, self.h1, self.jsonld = [], [], set(), 0, []
        self.title = self.description = self.canonical = False
        self._in_ld = False
        self._ld = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("href"):
            self.links.append(a["href"])
        if tag == "img":
            self.bilder.append((a.get("src", ""), a.get("alt")))
            for s in (a.get("srcset") or "").split(","):
                s = s.strip().split(" ")[0]
                if s:
                    self.bilder.append((s, "srcset"))
        if tag in ("link",) and a.get("href"):
            if a.get("rel") == "canonical":
                self.canonical = True
            if a.get("rel") in ("stylesheet", "icon", "preload"):
                self.links.append(a["href"])
        if tag == "script" and a.get("src"):
            self.links.append(a["src"])
        if tag == "script" and a.get("type") == "application/ld+json":
            self._in_ld = True
        if tag == "meta" and a.get("name") == "description" and a.get("content"):
            self.description = True
        if tag == "title":
            self.title = True
        if tag == "h1":
            self.h1 += 1

    def handle_endtag(self, tag):
        if tag == "script" and self._in_ld:
            self.jsonld.append("".join(self._ld))
            self._ld, self._in_ld = [], False

    def handle_data(self, data):
        if self._in_ld:
            self._ld.append(data)


def ziel_datei(href: str, von: Path) -> Path | None:
    """Interner Link → Datei in dist/, None bei externen Links."""
    if re.match(r"^(https?:|mailto:|tel:|#|data:)", href):
        return None
    pfad = href.split("#")[0].split("?")[0]
    if not pfad:
        return von
    if pfad.startswith("/"):
        if BASE_PATH and pfad.startswith(BASE_PATH + "/"):
            pfad = pfad[len(BASE_PATH):]
        elif BASE_PATH and pfad == BASE_PATH:
            pfad = "/"
        ziel = DIST / pfad.lstrip("/")
    else:
        ziel = von.parent / pfad
    if ziel.is_dir():
        ziel = ziel / "index.html"
    return ziel


def pruefe_html(datei: Path, alle_ids: dict[Path, set]):
    text = datei.read_text(encoding="utf-8")
    rel = datei.relative_to(DIST)
    for v in VERBOTEN:
        if v in text:
            fehler.append(f"{rel}: enthält '{v}'")
    s = Sammler()
    s.feed(text)
    alle_ids[datei] = s.ids
    if s.h1 != 1:
        fehler.append(f"{rel}: {s.h1} h1-Elemente statt 1")
    if not s.title:
        fehler.append(f"{rel}: kein <title>")
    if not s.description:
        fehler.append(f"{rel}: keine meta description")
    if not s.canonical and datei.name != "404.html":
        fehler.append(f"{rel}: kein canonical")
    for src, alt in s.bilder:
        if alt is None:
            fehler.append(f"{rel}: <img src='{src}'> ohne alt-Attribut")
        z = ziel_datei(src, datei)
        if z is not None and not z.exists():
            fehler.append(f"{rel}: Bild fehlt: {src}")
    for ld in s.jsonld:
        try:
            json.loads(ld)
        except json.JSONDecodeError as e:
            fehler.append(f"{rel}: ungültiges JSON-LD ({e})")
    return [(h, datei) for h in s.links]


def main():
    if not DIST.exists():
        print("dist/ fehlt – erst python3 build.py laufen lassen")
        sys.exit(1)
    htmls = sorted(DIST.rglob("*.html"))
    if len(htmls) < 5:
        fehler.append(f"nur {len(htmls)} HTML-Dateien in dist/")
    alle_ids: dict[Path, set] = {}
    links = []
    for h in htmls:
        links += pruefe_html(h, alle_ids)
    # Links und Anker
    for href, von in links:
        z = ziel_datei(href, von)
        if z is None:
            continue
        if not z.exists():
            fehler.append(f"{von.relative_to(DIST)}: Link ins Leere: {href}")
            continue
        if "#" in href:
            anker = href.split("#", 1)[1]
            if anker and z.suffix == ".html" and anker not in alle_ids.get(z, set()):
                # Ziel evtl. noch nicht geparst (Datei ohne Link von woanders)
                if z not in alle_ids:
                    pruefe_html(z, alle_ids)
                if anker not in alle_ids.get(z, set()):
                    fehler.append(f"{von.relative_to(DIST)}: Anker #{anker} fehlt in {z.relative_to(DIST)}")
    # Sitemap
    sm = DIST / "sitemap.xml"
    if not sm.exists():
        fehler.append("sitemap.xml fehlt")
    else:
        for loc in re.findall(r"<loc>([^<]+)</loc>", sm.read_text()):
            pfad = re.sub(r"^https?://[^/]+", "", loc)
            z = ziel_datei(pfad or "/", DIST / "index.html")
            if z is None or not z.exists():
                fehler.append(f"sitemap: {loc} zeigt auf keine Datei")
    for name in ("robots.txt", "static/css/style.css", "static/js/main.js"):
        if not (DIST / name).exists():
            fehler.append(f"{name} fehlt")
    # Schriften aus dem CSS
    css = DIST / "static/css/style.css"
    if css.exists():
        for f in re.findall(r"url\(['\"]?([^'\")]+\.woff2)", css.read_text()):
            if not (css.parent / f).resolve().exists():
                fehler.append(f"style.css: Schrift fehlt: {f}")
    if fehler:
        print(f"{len(fehler)} Problem(e):")
        for f in fehler:
            print(" -", f)
        sys.exit(1)
    print(f"OK: {len(htmls)} Seiten, {len(links)} Links geprüft, keine Probleme")


if __name__ == "__main__":
    main()
