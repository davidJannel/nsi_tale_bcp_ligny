"""
Interface minimale du type liste
    - creer_liste() : constructeur qui retourne une liste vide
    - liste_vide(l) : accesseur qui retourne True si la liste l est vide
    - inserer(e, l) : opérateur qui insère l'élément e en tête de la liste l
    - tete(l) : accesseur qui retourne l'élément en tête de liste l (si elle n'est pas vide)
    - queue(l) : accesseur qui retourne la liste l privée de son premier élément (si elle n'est pas vide)
    - elements_liste(l) : itérateur qui retourne un tableau contenant les méléments de la liste l. On peut
    ensuite itérer avec une boucle for
        
À cette interface on peut ajouter :
    - taille(l) accesseur qui retourne le nombre d'éléments de la liste l

l'implémentation utilisera des tuples.
Une liste est donc représenté par le couple (tete, queue)
"""

def creer_liste():
    return ()

def liste_vide(liste):
    return liste == ()

def inserer(elt, liste):
    return (elt, liste)

def tete(liste):
    assert not liste_vide(liste), "liste vide"
    return liste[0]

def queue(liste):
    assert not liste_vide(liste), 'liste vide'
    return liste[1]

def elements_liste(liste):
    tab_iter = []
    while not liste_vide(liste):
        tab_iter.append(tete(liste))
        liste = queue(liste)
    return tab_iter

def taille(liste):
    nb = 0
    while not liste_vide(liste):
        nb = nb + 1
        liste = queue(liste)
    return nb

"""
tests
"""
if __name__ == "__main__":
    l = creer_liste()
    l = inserer(7, l)
    l = inserer(8, l)
    l = inserer(14, l)
    assert liste_vide(l) == False
    assert tete(l) == 14
    assert queue(l) == (8, (7, ()))
    assert elements_liste(l) == [14, 8, 7]
    assert taille(l) == 3