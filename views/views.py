# views/views.py
from pathlib import Path
from utils.func import clear_console, generateRandomCSV, recupererCSV, createDoc, deleteEmptyDoc, deleteFiles, deleteAll

def inputFields(msg):
    return input(msg + " ")


def generateRandomDataView():
    try:
        name = inputFields("Nom du fichier CSV à générer (sans extension) :")
        generateRandomCSV(name)
    except Exception as e:
        print(f"Erreur lors de la génération CSV : {e}")


def createAllDocumentView():
    try:
        csv_name = inputFields("Nom du CSV à lire :")
        users = recupererCSV(csv_name)
        if not users:
            return
        folder = inputFields("Nom du dossier où créer les documents :")
        createDoc(folder, users)
    except Exception as e:
        print(f"Erreur : {e}")


def deleteEmptyDirectoryView():
    try:
        folder = inputFields("Nom du dossier à nettoyer des dossiers vides :")
        deleteEmptyDoc(folder)
    except Exception as e:
        print(f"Erreur : {e}")


def deleteAllView():
    try:
        folder = inputFields("Nom du dossier à vider totalement :")
        deleteAll(folder)
    except Exception as e:
        print(f"Erreur : {e}")


def deleteFilesViews():
    try:
        folder = inputFields("Nom du dossier parent :")
        filename = inputFields("Nom du fichier à supprimer :")
        deleteFiles(folder, filename)
    except Exception as e:
        print(f"Erreur : {e}")