from abc import ABC,abstractmethod

class Vehicule(ABC):
    def __init__(self,mark,speed):
        self.mark=mark
        self.speed=speed
    
    def afficherInfo(self):
        print("==VEHICULE==")
        print(f"Marque:{self.mark}")
        print(f"Vitesse:{self.speed}")
    
    def accelerer(self, valeur):
        self.speed+=valeur
        if self.speed>300:
            self.speed=300
    def freiner(self, valeur):
        self.speed-=valeur
        if self.speed<0:
            self.speed=0
    @abstractmethod
    def demarrer(self):
        pass

class Voiture(Vehicule):
    def __init__(self, mark, speed,nombrePorte):
        super().__init__(mark, speed)
        self.nombrePorte=nombrePorte
    def afficherInfo(self):
        super().afficherInfo()
        print(f"Nombre de porte{self.nombrePorte}")
    def demarrer(self):
        print("La voiture demarre")

class Moto(Vehicule):
    def __init__(self,mark,speed,cylindre):
        super().__init__(mark,speed)
        self.cylindre=cylindre
    def afficherInfo(self):
        super().afficherInfo()
        print(f"Cylindre:{self.cylindre}")
    def demarrer(self):
        print("La moto demarre")

vehicules=[]
vehicules.append(Voiture("Toyota",150,5))
vehicules.append(Moto("Honda",250,150))

for v in vehicules:
    v.demarrer()
    v.accelerer(200)
    v.freiner(100)
    v.afficherInfo()