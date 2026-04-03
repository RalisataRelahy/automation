# main.py
from views.views import (
    generateRandomDataView, createAllDocumentView,
    deleteEmptyDirectoryView, deleteAllView, deleteFilesViews, inputFields
)
from utils.func import clear_console

def main():
    while True:
        clear_console()
        print("======= Script CRUD Dossiers/Fichiers =======")
        print("1 - Générer un CSV aléatoire")
        print("2 - Créer des dossiers depuis CSV")
        print("3 - Supprimer des dossiers vides")
        print("4 - Vider un dossier")
        print("5 - Supprimer un fichier")
        print("6 - Quitter")
        choice = inputFields("Votre choix :")
        if choice == "1":
            generateRandomDataView()
        elif choice == "2":
            createAllDocumentView()
        elif choice == "3":
            deleteEmptyDirectoryView()
        elif choice == "4":
            deleteAllView()
        elif choice == "5":
            deleteFilesViews()
        elif choice == "6":
            break

if __name__ == "__main__":
    main()