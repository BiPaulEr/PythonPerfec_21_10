from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def jouer(self):
        pass

class Guitare(Instrument):
    def jouer(self):
        print("Dring dring")

class Batterie(Instrument):
    def jouer(self):
        print("Booom")

class Saxo(Instrument):
    def jouer(self):
        print("Vrooou")

def faire_jouer_un_orchestre(liste_instrument : list[Instrument]):
    for instrument in liste_instrument:
        instrument.jouer()


liste = [Guitare(), Batterie(), Saxo()]

faire_jouer_un_orchestre(liste)
