#
# Chapitre 8 - Exercice Initié 9 - Exploration de réseaux sociaux
#

from random import randint, sample, random

class Personne:
    
    def date_correcte(date):
        """ Vérifie que le triplet de nombres en
            argument représente une date valide. """
        return len(date)==3 and (1<=date[0]<=31) and (1<=date[1]<=12)
    
    
    def __init__(self, nom, date_naissance):
        if not Personne.date_correcte(date_naissance):
            raise ValueError(f"La date de naissance {date_naissance} n'est pas correcte !")
            
        self.nom = nom
        self.date_naissance = date_naissance
        
        
    def plus_jeune_que(self, personne):
        """ Renvoie True si la Personne `self`
            est plus jeune que la `personne`en 
            argument. """
        
        ma_date = self.date_naissance
        sa_date = personne.date_naissance
        if ma_date[2] > sa_date[2]:
            return True
        elif ma_date[2] < sa_date[2]:
            return False
        else:
            if ma_date[1] > sa_date[1]:
                return True
            elif ma_date[1] < sa_date[1]:
                return False
            else:
                if ma_date[0] > sa_date[0]:
                    return True
                elif ma_date[0] < sa_date[0]:
                    return False
                else:
                    # Égalité : disons que je suis le plus jeune !
                    return True
                
    def __repr__(self):
        """ Fonction appelée par défaut par `print()`
            pour représenter un objet sous forme 
            textuelle. """
        return f"{self.nom} {self.date_naissance}"

    
class ReseauSocial:
    
    def __init__(self):
        self.graphe = {}
        self._sommets = []
        
    def sommets(self):
        """ Retourne la liste des sommets du réseau. """
        return self._sommets
        
    def ajouter_personne(self, personne):
        """ Ajoute une personne au réseau si elle
            ne s'y trouve pas déjà. """
        
        if personne not in self.graphe.keys():
            self.graphe[personne] = {}
            self._sommets.append(personne)
        else:
            print(f"Attention, {personne} est déjà dans le réseau !")
            
    def retirer_personne(self, personne):
        """ Retire une personne du réseau, 
            si elle s'y trouve. """
        
        if personne in self.graphe.keys():
            del self.graphe[personne]
            self._sommets.remove(personne)
        else:
            print(f"Attention, {personne} n'existe pas dans le réseau !")
            
    def creer_lien(self, p1, p2):
        """ Crée un arc entre `p1` et `p2` 
            si c'est possible. """
        
        if p1 not in self.graphe.keys():
            print(f"Attention, p1 ({p1}) n'existe pas dans le réseau !")
        elif p2 not in self.graphe.keys():
            print(f"Attention, p2 ({p2}) n'existe pas dans le réseau !")
        elif p2 in self.graphe[p1]:
            print(f"Attention, un lien existe déjà de {p1} vers {p2} !")
        else:
            self.graphe[p1][p2] = True
        
    def supprimer_lien(self, p1, p2):
        """ Supprime le lien entre `p1` et `p2`
            s'il existe. """
        
        if p1 not in self.graphe.keys():
            print(f"Attention, p1 ({p1}) n'existe pas dans le réseau !")
        elif p2 not in self.graphe.keys():
            print(f"Attention, p2 ({p2}) n'existe pas dans le réseau !")
        elif p2 not in self.graphe[p1]:
            print(f"Attention, il n'existe pas de lien de {p1} vers {p2} !")
        else:
            del self.graphe[p1][p2]
    
    def ecrire_csv(self, chemin="reseau.csv"):
        """ Écrit une représentation textuelle du
            réseau (`self`) dans un fichier au chemin
            spécifié. """
        
        with open(chemin, "w") as f:
            # noms de colonnes
            f.write("nom,jour,mois,annee,indices voisins\n")
            
            indices_sommets = { self.sommets()[i]: i 
                                for i in range(len(self.sommets())) }
            for p in self.sommets():
                f.write(",".join( [ p.nom, str(p.date_naissance[0]), 
                                    str(p.date_naissance[1]), str(p.date_naissance[2]),
                                    ";".join( [ str(indices_sommets[voisin]) 
                                                for voisin in self.graphe[p].keys() ] ) 
                                  ] ))
                f.write("\n")
                
    def clone(self):
        """ Retourne une copie conforme du réseau. """
        
        copie = ReseauSocial()
        copie._sommets = [p for p in self._sommets ]
        copie.graphe = { s: { v: True 
                             for v in self.graphe[s].keys() }
                        for s in self.graphe.keys() }
        return copie
    
    
def charger_reseau(nom_fichier="reseau.csv"):
    """ Crée un objet ReseauSocial à partie de la
        description contenue dans le fichier dont
        le chemin est passé en paramètre. """
    
    with open(nom_fichier) as f:
        sommets = []
        indices_voisins = {}
        ligne = f.readline() # noms de colonnes
        ligne = f.readline() # première ligne
        while (ligne is not None) and (len(ligne)>0):
            champs = ligne.strip().split(",")
            p = Personne( champs[0], 
                          tuple( [ int(champs[i]) 
                                   for i in range(1, 4) ] ) )
            sommets.append( p )
            indices_voisins[p] = [ int(v) for v in champs[4].split(";") ]
            
            ligne = f.readline()
        
    reseau = ReseauSocial()
    for p in sommets:
        reseau.ajouter_personne(p)

    for p, indices in indices_voisins.items():
        for i in indices:
            reseau.creer_lien( p, reseau.sommets()[i] )
            
    return reseau