import os
import shutil
import filetype

from path import source_dir, destination_dir

# Dictionnaire des types de fichiers
File_type = {
    "Image": [".png", ".jpeg", ".jpg"],
    "Document": [".pdf", ".doc", ".zip", ".txt"],
    "Video": [".mp4", ".avi"],
    "Audio": [".mp3"],
    "Code": [".py", ".html", ".js", ".json", ".php", ".pyc", ".ipynb"],
    "Excel": [".xlsx", ".csv", ".xls"],
    "Powerpoint": [".pptx"],
    "Scripts": [".sh"],
    "Divers": [".drawio", ".rdp", ".DS_Store"],
    "SansExtension": []
}

# Créer les répertoires cibles dans destination_dir
for category in File_type.keys():
    os.makedirs(os.path.join(destination_dir, category), exist_ok=True)

# Itérer sur les fichiers dans le répertoire source
with os.scandir(source_dir) as entries:
    for entry in entries:
        if entry.is_file():
            filename, ext = os.path.splitext(entry.name)
            target_dir = None
            if not ext:
                if entry.is_dir():
                    pass
                elif entry.is_file():
                    try:
                        # Utilisation de filetype pour déterminer le type de fichier
                        kind = filetype.guess(entry.path)
                        if kind is None:
                            target_dir = os.path.join(destination_dir, "SansExtension")
                        else:
                            mime_type = kind.mime.split('/')[0]
                            target_dir = os.path.join(destination_dir, mime_type.capitalize())
                        print(f"Fichier sans extension: {filename}, Type MIME: {kind.mime if kind else 'Type inconnu'}")
                    except Exception as e:
                        print(f"Erreur lors de l'accès au fichier {entry.name}: {e}")
                        continue
            elif ext:
                if entry.is_file():
                    target_dir = next((os.path.join(destination_dir, cat) for cat, exts in File_type.items() if ext in exts), os.path.join(destination_dir, "Divers"))
                    print(f"Fichier avec extension: {filename} possède une extension explicite ({ext})")
                elif entry.is_dir():
                    pass

            # Déplacer le fichier si le répertoire cible est déterminé
            if target_dir:
                try:
                    shutil.move(entry.path, os.path.join(target_dir, entry.name))
                    print(f"Déplacement du fichier {entry.name} vers {target_dir}")
                except Exception as e:
                    print(f"Erreur lors du déplacement du fichier {entry.name} vers {target_dir}: {e}")

print("Fichiers déplacés avec succès !")
