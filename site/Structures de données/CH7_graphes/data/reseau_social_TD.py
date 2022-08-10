#
# TD : Exploration de réseaux sociaux
#

from reseau_social import Personne, ReseauSocial, charger_reseau
reseau = charger_reseau("mon_reseau.csv")

#
# a.
#

def est_oriente(reseau):
    """ Renvoie `True` si le ReseauSocial en
        argument est orienté. """

    for p in reseau.sommets():
        for voisin in reseau.graphe[p].keys():
            if p not in reseau.graphe[voisin]:
                return False
    return True

# Pour tester
def test_est_oriente():
    print("reseau est orienté :", est_oriente(reseau))

#
# b.
#

def meme_anniv():
    meme_anniv = {}
    for p in reseau.sommets():
        for voisin in reseau.graphe[p].keys():
            if p.date_naissance == voisin.date_naissance:
                meme_anniv[p] = True
                meme_anniv[voisin] = True

    print( "Personnes connaissant quelqu'un ayant le même anniversaire :", 
           list(meme_anniv.keys()) )

#
# c.
#

def amis_memes_annivs():
    amis_memes_anniv = {}
    for p in reseau.sommets():

        # On classe les voisins de `p` par leur date de naissance
        anniversaires = {}
        for voisin in reseau.graphe[p].keys():
            if voisin.date_naissance not in anniversaires:
                anniversaires[voisin.date_naissance] = [voisin]
            else:
                anniversaires[voisin.date_naissance].append(voisin)

        # On ne garde que les valeurs de `anniversaires` ayant plus 
        # d'un élément.
        for date, voisins in anniversaires.items():
            if len(voisins) > 1:
                if p not in amis_memes_anniv:
                    amis_memes_anniv[p] = {}
                for v in voisins:
                    if v not in amis_memes_anniv[p]:
                        amis_memes_anniv[p][v] = True

    print("Personnes connaissant plusieurs autres personnes ayant le même anniversaire :")
    for p, amis in amis_memes_anniv.items():
        print( f"{p} est ami avec {amis.keys()}" )

#
# d.
#
    
# La fonction sample permet de choisir un nombre
# d'éléments au harasd dans un ensemble.
from random import sample

def plus_connectes(reseau, n):
    """ Renvoie les `n` membres les plus connectés
        dans le `ReseauSocial` `reseau`. """

    # Dictionnaire contenant, pour une valeur
    # entière donnée, les personnes du réseau
    # ayant ce nombre d'amis.
    personnes_nb_amis = {}
    for p in reseau.sommets():
        nb_amis = len(reseau.graphe[p])
        if nb_amis not in personnes_nb_amis:
            personnes_nb_amis[nb_amis] = [p]
        else:
            personnes_nb_amis[nb_amis].append(p)

    # On va ensuite trier les clés de ce
    # dictionnaire et en extraire les `n`
    # personnes les plus connectées.

    n_restant = n
    resultat = []
    plus_connectes = sorted( list(personnes_nb_amis.keys()), reverse=True )

    for nb_amis in plus_connectes:
        personnes = personnes_nb_amis[nb_amis]
        nb_personnes = len(personnes)
        if nb_personnes <= n_restant:
            resultat += personnes
            n_restant -= nb_personnes
        else:
            # Il y a plus de personnes ayant `nb_amis`
            # que d'emplacements restants dans notre
            # résultat : on les choisit au hasard.
            resultat += sample( personnes, n_restant )
            n_restant = 0

        if n_restant == 0:
            break

    return resultat

# Pour tester
def test_plus_connectes():
    n = 12
    print(f"{n} personnes les plus connectées du réseau :")
    for p in plus_connectes(reseau, n):
        print(f"{p} : {len(reseau.graphe[p])} connaissances")
