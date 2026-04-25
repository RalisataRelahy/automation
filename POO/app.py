from abc import ABC,abstractmethod

class Parent(ABC):
    def __init__(self,n,p):
        self.nom=n
        self.prenom=p
    @abstractmethod
    def parler(self):
        pass

class Enfant(Parent):
    def __init__(self, n, p,nd):
        super().__init__(n, p)
        self.namedad=nd
    def parler(self):
        print(f"Je suis {self.nom} {self.prenom}, enfant de {self.namedad}")
        
p=Enfant("nekena","Relahy","Jean")
p.parler()
