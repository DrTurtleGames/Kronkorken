import os

with open("bilder_tag_template.txt", "w", encoding="utf-8") as f:
    for i in range(15, 164):
        dateiname = f"{i:04d}.webp"
        zeile = f'  {{ "pfad": "Bilder/{dateiname}", "tags": ["-","-","-","-"] }},\n'
        f.write(zeile)