import os
from PIL import Image

# VARIABLEN
zum_ordner = "Alle_Galerien/Galerie_Gemischt"

# Pfad zum Bilderordner (anpassen bei Bedarf)
aktueller_ordner = "Alle_Galerien"

# Alle neuen WebP-Dateien für HTML-Tags sammeln
webp_bilder = sorted([
    f for f in os.listdir(aktueller_ordner)
    if f.lower().endswith(".webp")
])

# Liste der <img>-Tags erstellen
img_tags = []
for datei in webp_bilder:
    src = f"{zum_ordner}/{datei}"
    alt = f"Bild {os.path.splitext(datei)[0]}"
    tag = f'    <img src="{src}" alt="{alt}" loading="lazy">'
    img_tags.append(tag)

# In Datei schreiben
with open("tags_generator_output.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(img_tags))

print(f"{len(img_tags)} <img>-Tags wurden in 'tags_generator_output.txt' geschrieben.")
