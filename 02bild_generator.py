import os
from PIL import Image

# Pfad zum Bilderordner (anpassen bei Bedarf)
ordnername = "Neue Bilder"

ziel_format = "webp"
qualitaet = 80  # WebP-Qualität 0–100
zielordner = "Bilder Cache"

# Unterstützte Bildformate
bild_endungen = [".jpg", ".jpeg", ".png"]

# Alle gültigen Bilddateien im Ordner sammeln
bild_pfade = [
    datei for datei in os.listdir(ordnername)
    if os.path.splitext(datei)[1].lower() in bild_endungen
]

# Sortieren (optional)
#bild_pfade.sort()

# WebP-Bilder erstellen (falls nicht vorhanden)
for datei in bild_pfade:
    quellpfad =  os.path.join(ordnername, datei)
    basisname = os.path.splitext(datei)[0]
    ziel_datei = f"{basisname}.{ziel_format}"
    zielpfad = os.path.join(zielordner, ziel_datei)

    if not os.path.exists(zielpfad):
        try:
            bild = Image.open(quellpfad).convert("RGB")
            bild.save(zielpfad, ziel_format, quality=qualitaet)
            print(f"Konvertiert: {ziel_datei}")
        except Exception as e:
            print(f"Fehler bei {datei}: {e}")
