#!/usr/bin/env python3
"""Macht aus den Originalfotos in bilder/original/ optimierte WebP-Dateien in static/img/.

Läuft nur lokal (die Originale sind nicht im Repo). Schreibt inhalt/bilder_masse.json
mit Breite und Höhe jeder Ausgabedatei, damit die Templates width/height setzen können.
Quelle der Originale: bilder/jimdo_quellen.txt (alte Jimdo-Seite, Fotos Studio Seikel).
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageOps

WURZEL = Path(__file__).resolve().parent
sys.path.insert(0, str(WURZEL))
from inhalt import daten  # noqa: E402

ORIG = WURZEL / "bilder" / "original"
IMG = WURZEL / "static" / "img"
masse: dict[str, list[int]] = {}


def original(bild_id: str) -> Image.Image:
    for ext in ("jpg", "png", "gif"):
        p = ORIG / f"{bild_id}.{ext}"
        if p.exists():
            im = Image.open(p)
            return ImageOps.exif_transpose(im)
    raise FileNotFoundError(bild_id)


def speichere(im: Image.Image, rel: str, breite: int | None = None, qualitaet: int = 80,
              seitenverhaeltnis: tuple[int, int] | None = None, format: str = "WEBP") -> None:
    ziel = IMG / rel
    ziel.parent.mkdir(parents=True, exist_ok=True)
    if seitenverhaeltnis:
        im = ImageOps.fit(im, passe(im.size, seitenverhaeltnis), method=Image.LANCZOS)
    if breite and im.width > breite:
        im = im.resize((breite, round(im.height * breite / im.width)), Image.LANCZOS)
    if format == "WEBP":
        im.save(ziel, "WEBP", quality=qualitaet, method=6)
    elif format == "PNG":
        im.save(ziel, "PNG", optimize=True)
    else:
        im.convert("RGB").save(ziel, format, quality=qualitaet, optimize=True)
    masse[rel] = [im.width, im.height]
    print(f"{rel:48s} {im.width}x{im.height} {ziel.stat().st_size // 1024} KB")


def passe(groesse, verhaeltnis):
    """Größter Ausschnitt im gewünschten Verhältnis, der ins Bild passt."""
    b, h = groesse
    vb, vh = verhaeltnis
    if b / h > vb / vh:
        return (round(h * vb / vh), h)
    return (b, round(b * vh / vb))


def main() -> None:
    # Galerie: Lightbox 1600, Kachel 640
    for eintrag in daten.GALERIE:
        im = original(eintrag["id"]).convert("RGB")
        speichere(im.copy(), f"galerie/{eintrag['id']}-1600.webp", 1600, 80)
        speichere(im.copy(), f"galerie/{eintrag['id']}-640.webp", 640, 76, seitenverhaeltnis=(4, 3))
    # Team: 300er Freisteller
    for person in daten.TEAM:
        speichere(original(person["bild"]).convert("RGBA"), f"team/{person['bild']}.webp", 300, 84)
    # Fuhrpark: transparente Freisteller
    for fz in daten.FUHRPARK:
        speichere(original(fz["bild"]).convert("RGBA"), f"fuhrpark/{fz['bild']}.webp", 300, 84)
    # Hero-Bilder, zwei Breiten
    for name, verhaeltnis in (("hero_start", (4, 5)), ("hero_zaunbau", (3, 2)), ("ueber_uns", (3, 2))):
        im = original(daten.BILDER[name]).convert("RGB")
        speichere(im.copy(), f"{name}-1400.webp", 1400, 80, seitenverhaeltnis=verhaeltnis)
        speichere(im.copy(), f"{name}-800.webp", 800, 78, seitenverhaeltnis=verhaeltnis)
    # Leistungsgruppen-Bilder
    for g in daten.LEISTUNGSGRUPPEN:
        speichere(original(g["bild"]).convert("RGB"), f"gruppen/{g['slug']}.webp", 800, 78, seitenverhaeltnis=(3, 2))
    # Open-Graph als JPEG (breiteste Unterstützung)
    speichere(original(daten.BILDER["og"]).convert("RGB"), "og.jpg", 1200, 82, seitenverhaeltnis=(1200, 630), format="JPEG")
    # Logo: Weiß → transparent, Ränder abschneiden
    logo = original(daten.BILDER["logo"]).convert("RGBA")
    px = logo.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b, a = px[x, y]
            if r > 240 and g > 240 and b > 240:
                px[x, y] = (255, 255, 255, 0)
    logo = logo.crop(logo.getbbox())
    speichere(logo, "logo.png", 1200, format="PNG")
    (WURZEL / "inhalt" / "bilder_masse.json").write_text(json.dumps(masse, indent=1, sort_keys=True))
    print(f"\n{len(masse)} Dateien, Maße in inhalt/bilder_masse.json")


if __name__ == "__main__":
    main()
