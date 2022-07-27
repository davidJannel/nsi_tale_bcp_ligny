"""
Interface minimale du type pile
    - creer_pile() : constructeur qui retourne une pile vide
    - pile_vide(p) : accesseur qui retourne True si la pile p est vide
    - empiler(e, p) : opérateur qui insère l'élément e au sommet de la pile p
    - depiler(p) : opérateur qui enlève et retourne l'élément sité au sommet de la pile p (si elle n'est pas vide)
    - sommet(p) : accesseur qui retourne l'élément au sommet de la pile p (si elle n'est pas vide)
    - elements_pile(p) : itérateur qui retourne un tableau contenant les éléments de la pile p. On peut
    ensuite itérer avec une boucle for. Les élément sont parcourus du sommet jusqu'à la base de la pile.
        
À cette interface on peut ajouter :
    - taille(p) accesseur qui retourne le nombre d'éléments de la pile p

l'implémentation utilisera des tableaux.
"""

def creer_pile():
    return []

def pile_vide(pile):
    return pile == []

def empiler(elt, pile):
    pile.append(elt)

def depiler(pile):
    assert not pile_vide(pile), "pile vide"
    sommet = pile.pop()
    return sommet

def sommet(pile):
    assert not pile_vide(pile), "pile vide"
    return pile[-1]

def elements_pile(pile):
    tab_elt = []
    for i in range(len(pile)-1, -1, -1):
        tab_elt.append(pile[i])
    return tab_elt

def taille(pile):
    return len(pile)

"""
tests
"""
if __name__ == "__main__":
    p = creer_pile()
    empiler(7, p)
    empiler(8, p)
    empiler(9, p)
    assert pile_vide(p) == False
    assert depiler(p) == 9
    empiler(5, p)
    assert sommet(p) == 5
    assert p == [7, 8, 5]
    assert elements_pile(p) == [5, 8, 7]
    assert taille(p) == 3