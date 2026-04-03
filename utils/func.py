# utils/func.py
import os
from pathlib import Path
import csv
import random
import shutil

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def generateRandomCSV(file_name):
    noms = ["Dupont", "Martin", "Bernard", "Petit", "Robert", "Richard", "Durand", "Leroy", "Moreau", "Simon"]
    prenoms = ["Alice", "Bob", "Charlie", "David", "Emma", "Fanny", "Gabriel", "Hugo", "Inès", "Julien"]
    roles = ["Admin", "User", "Moderator", "Guest"]

    path_csv = Path(f"{file_name}.csv")
    with open(path_csv, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["id", "nom", "prenom", "age", "role"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(1, 21):
            writer.writerow({
                "id": i,
                "nom": random.choice(noms),
                "prenom": random.choice(prenoms),
                "age": random.randint(18, 60),
                "role": random.choice(roles)
            })
    print(f"CSV généré : {path_csv.resolve()}")


def recupererCSV(file_name):
    path_csv = Path(f"{file_name}.csv")
    if not path_csv.exists():
        print(f"Le fichier {file_name}.csv n'existe pas !")
        return []
    with open(path_csv, newline="", encoding="utf-8") as csvFiles:
        reader = csv.DictReader(csvFiles)
        return list(reader)


def createDoc(parent_folder, users):
    parent_folder = Path(parent_folder)
    parent_folder.mkdir(exist_ok=True)
    for i, user in enumerate(users, start=1):
        dossier = parent_folder / f"Dossier_{user['prenom']}_{user['nom']}"
        dossier.mkdir(exist_ok=True)
        if i == 5:  # simulate empty folder
            continue
        fichier = dossier / "Role.txt"
        with open(fichier, "w", encoding="utf-8") as f:
            f.write(f"Je suis {user['role']}")
    print(f"{len(users)} dossiers créés dans {parent_folder}")


def deleteEmptyDoc(parent_dir):
    parent_dir = Path(parent_dir)
    if not parent_dir.exists():
        print("Le dossier n'existe pas !")
        return
    count = 0
    for d in parent_dir.iterdir():
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
            count += 1
    print(f"{count} dossiers vides supprimés dans {parent_dir}")


def deleteFiles(current_dir, filename):
    current_dir = Path(current_dir)
    if not current_dir.exists():
        print(f"Le dossier {current_dir} n'existe pas !")
        return
    count = 0
    for d in current_dir.rglob(filename):
        if d.is_file():
            d.unlink()
            count += 1
    print(f"{count} fichiers '{filename}' supprimés.")


def deleteAll(parent_dir):
    parent_dir = Path(parent_dir)
    if not parent_dir.exists():
        print(f"{parent_dir} n'existe pas !")
        return
    shutil.rmtree(parent_dir)
    parent_dir.mkdir(exist_ok=True)
    print(f"Dossier {parent_dir} vidé complètement !")