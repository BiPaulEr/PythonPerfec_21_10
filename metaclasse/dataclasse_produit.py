from dataclasses import dataclass, field

@dataclass(order = True)
class Produit:
    name : str = field(compare=False)
    price : float
    identifiant_sercret : str = field(compare=False, repr=False)
    checksum : float = field(init=False)

    def __post_init__(self):
        self.checksum = str(self.name)+str(self.price)+str(self.identifiant_sercret)

produit1 = Produit("vache", 13, "Moau")
produit2 = Produit("chat", 26, "Meuh")

print(produit1 < produit2)
print(produit1)