"""
Interface minimale du type file
    - creer_file() : constructeur qui retourne une file vide
    - file_vide(f) : accesseur qui retourne True si la file f est vide
    - enfiler(e, f) : opérateur qui insère l'élément e à la fin de la file f
    - defiler(f) : opérateur qui retire et retourne l'élément sité au début de la file f (si elle n'est pas vide)
    - tete_file(f) : accesseur qui retourne l'élément au début de la file f (si elle n'est pas vide)
    - elements_file(f) : itérateur qui retourne un tableau contenant les éléments de la file f. On peut
    ensuite itérer avec une boucle for. Les élément sont parcourus du début jusqu'à la fin de la file.
        
À cette interface on peut ajouter :
    - taille(f) accesseur qui retourne le nombre d'éléments de la file f

l'implémentation utilisera des tableaux.
"""

def creer_file():
    return []

def file_vide(file):
    return file == []

def enfiler(elt, file):
    file.append(elt)

def defiler(file):
    assert not file_vide(file), "file vide"
    tete = file.pop(0)
    return tete

def tete_file(file):
    assert not file_vide(file), "file vide"
    return file[0]

def elements_file(file):
    return file

def taille(file):
    return len(file)

"""
tests
"""
if __name__ == "__main__":
    f = creer_file()
    enfiler(7, f)
    enfiler(8, f)
    enfiler(9, f)
    assert file_vide(f) == False
    assert defiler(f) == 7
    enfiler(5, f)
    assert tete_file(f) == 8
    assert elements_file(f) == [8, 9, 5]
    assert taille(f) == 3