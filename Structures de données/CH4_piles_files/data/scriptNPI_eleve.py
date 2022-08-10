class cellule:
    """ Classe qui modélise une cellule dans une structure linéaire """
    def __init__(self,element):
        self.contenu = element
        self.suivant = None

class pile:
    """ Classe qui implémente une pile"""
    def __init__(self):
        self.sommet = None

    def estVide(self):
        return self.sommet == None

    def empile(self,element):
        nouveau = cellule(element)
        nouveau.suivant = self.sommet
        self.sommet = nouveau

    def depile(self):
        valeur = self.sommet.contenu
        self.sommet = self.sommet.suivant
        return valeur

    def affiche(self):
        pointeur = self.sommet
        while pointeur != None :
            print(pointeur.contenu)
            pointeur = pointeur.suivant

def calcule(expression):
    valeur = None
    tableau = expression.split()
    ### Mettez votre code ici

    return valeur

assert calcule('2 3 + 11 *')==55, "erreur sur le premier calcul"
assert calcule('2 5 * 7  +')==17, "erreur sur le second calcul"
assert calcule('8 2 / 4 - ')== 0, "erreur sur le troisième calcul"
assert calcule('1 2 3 4 + * +')==15 , "erreur sur le quatrième calcul"
assert calcule("1 2 3 + ")==None," chaine mal formée mais valeur retournée"
