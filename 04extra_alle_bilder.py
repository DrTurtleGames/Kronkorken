import os

with open("bilder_tag_template.txt", "w", encoding="utf-8") as f:
    for i in range(720, 830):
        dateiname = f"{i:04d}.webp"
        zeile = f'    <img src="Bilder/{dateiname}" alt="Bild{dateiname}" loading="lazy" onclick="zoom_in(this)">\n'
        f.write(zeile)