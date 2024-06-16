import os

#import de la variable qui contient l'absolute path
from path import source_dir 


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
    "Divers" : [".drawio", ".rdp", ".DS_Store"]
}

# os.scandir() est plus efficace que os.Listdir()

#Je liste tout les fichiers de mon répértoire de départ

all_unique_entry = os.scandir(source_dir)

with all_unique_entry as entries:
    for entry in entries:
        if entry.is_file():
            print(f"Fichier : {entry.name} , Path: {entry.path}")
        elif entry.is_dir():
            print(f"Dossier : {entry.name} , Path : {entry.path}")
        else:
            raise TypeError(f"Liste des éléement qui ne son ni un fichier ni un dossier : {entry.name} avec comme chemin : {entry.path}")

