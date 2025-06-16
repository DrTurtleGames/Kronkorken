import os

# ====== KONFIGURATION ======
startnummer = 46                   # Startwert, z. B. 1 für 0001
ordner = "Neue Bilder"            # Pfad zum Bildordner
ziel_endung = ".png"              # Ausgabeformat: .jpg, .png, .webp usw.
ziffern = 4                       # z. B. 0001, 0100, 9999 → 4 Ziffern
# ============================

# Alle Bilddateien im Ordner finden
bild_endungen = [".jpg", ".jpeg", ".png", ".webp"]
dateien = sorted([
    f for f in os.listdir(ordner)
    if os.path.splitext(f)[1].lower() in bild_endungen
])

# Bilder umbenennen
for i, datei in enumerate(dateien, start=startnummer):
    _, ext = os.path.splitext(datei)
    neuer_name = f"{i:0{ziffern}d}{ziel_endung}"
    alt_pfad = os.path.join(ordner, datei)
    neu_pfad = os.path.join(ordner, neuer_name)

    # Falls Zielname bereits existiert (sicherheitshalber überspringen)
    if os.path.exists(neu_pfad):
        print(f"ERROR: Datei existiert schon: {neuer_name}, wird übersprungen.")
        continue

    os.rename(alt_pfad, neu_pfad)
    print(f"OK: {datei} → {neuer_name}")

print("\nUmbenennung abgeschlossen.")
