class Proprietaire:
    def __init__(self, nom, prenom, age, sexe):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.sexe = sexe

    def __str__(self):
        return f"Nom: {self.nom}, Prénom: {self.prenom}, Age: {self.age}, Sexe: {self.sexe}"

class Compte:
    def __init__(self, proprietaire, solde=0):
        self.proprietaire = proprietaire
        self._solde = solde

    def deposer(self, montant):
        if montant <= 0:
            print("Montant invalide")
            return
        
        self._solde += montant
        print("Dépôt effectué")

    def retirer(self, montant):
        if montant <= 0:
            print("Montant invalide")
            return
        
        if montant > self._solde:
            print("Solde insuffisant")
            return
        
        self._solde -= montant
        print("Retrait effectué")

    def afficher_solde(self):
        print(f"Solde: {self._solde}")

    def afficher_info(self):
        print("=== Compte ===")
        print(self.proprietaire)
        print(f"Solde: {self._solde}")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Terrain:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    @staticmethod
    def trouver_tresor(initial, tresor):
        chemin = []

        x = initial.x
        y = initial.y

        while x != tresor.x or y != tresor.y:

            if x < tresor.x:
                x += 1
                chemin.append("E")

            elif x > tresor.x:
                x -= 1
                chemin.append("O")

            elif y < tresor.y:
                y += 1
                chemin.append("N")

            elif y > tresor.y:
                y -= 1
                chemin.append("S")

        return "".join(chemin)


depart = Point(0, 0)
tresor = Point(3, 2)

chemin = Terrain.trouver_tresor(depart, tresor)

print("Chemin vers le trésor:", chemin)

p = Proprietaire("Nekena", "Relahy", 25, "Male")

c = Compte(p)

c.deposer(50000)
c.retirer(2000)

c.afficher_solde()
c.afficher_info()