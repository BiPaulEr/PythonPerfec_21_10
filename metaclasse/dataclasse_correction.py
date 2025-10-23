from dataclasses import dataclass, field

@dataclass(order=True)
class Produit:
    nom : str = field(compare = False)
    prix : float = field(repr=False)
    categorie : str
    quantite_stock : int = field(init = False)

    def __post_init__(self):
        self.quantite_stock = 0

produit1 = Produit("Produit A", 20.0, "Electronique")

produit2 = Produit("Produit B", 10.0, "Maison")

produit3 = Produit("Produit A", 20.0, "Electronique")

print(produit1, produit2, produit3)

print("P1 vs P2", produit1 >  produit2)
print("P2 vs P3", produit2 > produit3)
print("P1 vs P3", produit1 > produit3)