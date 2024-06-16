import shutil
import os
import filetype

#import de la variable qui contient mon directory à déplacer
from path import source_dir, destination_dir



#Etape 1 : Détérminer les catégories ainsi que les extensions associés
File_type = {
    "Image" : [".png", ".jpeg", ".jpg"],
    "Document" : [".pdf", ".doc", ".zip", ".txt"],
    "Video" : [".mp4", ".avi"],
    "Audio" : [".mp3"],
    "Code" : [".py", ".html", ".js", ".json", ".php", ".pyc", ".ipynb"],
    "Excel" : [".xlsx", ".csv", ".xls"],
    "Powerpoint" : [".pptx"],
    "Scripts" : [".sh"],
    "Divers" : [".drawio", ".rdp", ".DS_Store"],
    "SansExtension" : []

}

#Création des catégories
for category in File_type.keys():
    os.makedirs(os.path.join(destination_dir, category), exist_ok=True)

# os.scandir() est plus efficace que os.Listdir()
all_unique_entry = os.scandir(source_dir)

#Etape 2 : Je liste tout les fichiers de mon répértoire de départ
with all_unique_entry as entries:
    for entry in entries:
        if entry.is_file():
            print(f"Fichier : {entry.name} , Path: {entry.path}")
        elif entry.is_dir():
            print(f"Dossier : {entry.name} , Path : {entry.path}")
        else:
            raise TypeError(f"Liste des éléement qui ne son ni un fichier ni un dossier : {entry.name} avec comme chemin : {entry.path}")

all_unique_entry = os.scandir(source_dir)

with all_unique_entry as entries:
    for entry in entries:
        filename, ext = os.path.splitext(entry.name)
        if not ext:
            if entry.is_dir():
                pass
            elif entry.is_file():
                try:
                    # Utilisation de filetype pour déterminer le type de fichier
                    kind = filetype.guess(entry.path)
                    if kind is None:
                        file_type = 'Type inconnu'
                    else:
                        file_type = kind.mime
                    print(f"Fichier sans extension: {filename}, Type MIME: {file_type}")
                except Exception as e:
                    print(f"Erreur lors de l'accès au fichier {entry.name}: {e}")
        elif ext:
            if entry.is_file():
                print(f"Fichier avec extension: {filename} possède une extension explicite ({ext})")
            elif entry.is_dir():
                pass

#Etape 3 : import de la variable qui contient mon directory à déplacer

for category in File_type.keys():
    os.makedirs(os.path.join(destination_dir, category), exist_ok=True)