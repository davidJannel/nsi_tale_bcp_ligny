"""
Implémentation minimale du type dictionnaire à l'aide d'une table de hachage.
    - creer_dico() : constructeur qui retourne un dictionnaire vide
    - ajouter(d, cle, valeur) : opérateur qui ajoute cle au dico d et l'associe à valeur
    - valeur_cle(d, cle) : accesseur qui retourne la valeur associée à la cle
    dans le dico d à condition qu'elle soit présente.
    - cles_dico(d) : itérateur qui énumère les clés du dico d

Pour gérer les collisions dans la table de hachage, on va stocker dans chaque élément de la table
de hachage une liste des paires (cle, valeur) qui auront le même code de hachage.
"""

from files_cours_correction import * # utilisation de l'interface liste du cours

HTAILLE = 109 # taille de la table de hachage

def hachage(cle):
    """
    retourne une valeur comprise entre 0 et 109 de la cle passée en argument
    input : cle (str)
    output : h (int)
    """
    code = 0
    for car in cle:
        code = code + ord(car)
    h = code % HTAILLE
    return h

def creer_dico():
    # votre code ici

def ajouter_cle(dico, cle, valeur):
    # votre code ici

def valeur_cle(dico, cle):
   # votre code ici

def cles_dico(dico):
    # votre code ici


"""
On peut ajouter à cette interface :
    - taille(d) : accesseur qui retourne le nombre d'éléments présents dans le dictionnaire d
"""
def taille(dico):
    # votre code ici


"""
La fonction moyenne calcule la moyenne des notes présentes dans le dictionnaire.
Elle prend en argument un dictionnaire implémenté comme ci-dessus.
On s'assurera que le dictionnaire n'est pas vide.
"""
def moyenne(dico):
    # votre code ici


"""
tests
"""
if __name__ == "__main__":
    notes = creer_dico()
    ajouter_cle(notes, 'Arthur', 13)
    ajouter_cle(notes, 'David', 20)
    ajouter_cle(notes, 'Alice', 15)
    ajouter_cle(notes, 'Bob', 12)
    ajouter_cle(notes, 'Dan', 14)
    assert valeur_cle(notes, 'David') == 20
    assert valeur_cle(notes, 'Denis') == None
    assert cles_dico(notes) == ['Alice', 'David', 'Dan', 'Bob', 'Arthur']
    assert taille(notes) == 5
    assert moyenne(notes) == 14.8