class Cellule:
    def __init__(self, valeur, suivante = None):
        self.valeur = valeur
        self.suivante = suivante
    
    def __str__(self):
        return f"({self.valeur}, {self.suivante})"
        
        
class Liste:
    def __init__(self):
        self.debut = None
        self.dernier = None
        
    def __str__(self):
        return f"{self.debut}"

    def est_vide(self):
        return self.debut == None
    
    def inserer(self, valeur):
        if self.debut == None:
            self.dernier = Cellule(valeur, self.debut)
            self.debut = self.dernier
        else:
            self.debut = Cellule(valeur, self.debut)
            
    def tete(self):
        assert not self.est_vide(), "liste vide"
        return self.debut.valeur
    
    def queue(self):
        assert not self.est_vide(), "liste vide"
        queue_liste = Liste()
        queue_liste.debut = self.debut.suivante
        return queue_liste
     
    def elements_liste(self):
        tab_elt = []
        cellule_en_cours = self.debut
        while cellule_en_cours != None:
            tab_elt.append(cellule_en_cours.valeur)
            cellule_en_cours = cellule_en_cours.suivante
        tab_elt.reverse()
        return tab_elt
    
    def ajouter_fin(self, elt):
        if self.est_vide():
            self.inserer(elt)
        else:
            self.dernier.suivante = Cellule(elt)
            self.dernier = self.dernier.suivante
            
    def copie(self):
        liste_copie = Liste()
        for elt in self.elements_liste():
            liste_copie.inserer(elt)
        return liste_copie



# tests
print("Question 1.4")
liste = Liste()
liste.inserer("Paris")
liste.inserer("Berlin")
ville = liste.tete()
liste.inserer("Londres")
reste = liste.queue()
print(liste.est_vide())
print(f'liste : {liste}')
print(f'reste : {reste}')
for v in liste.elements_liste():
    print(v)

print(10*'#')
print("Question 2.2")
liste = Liste()
liste.inserer("Paris")
liste.inserer("Berlin")
liste.inserer("Londres")
reste = liste.queue()
liste.ajouter_fin("Rome")
print(f'liste : {liste}')
print(f'reste : {reste}')

print(10*'#')
print("Question 2.5")
liste = Liste()
liste.inserer("Paris")
liste.inserer("Berlin")
liste.inserer("Londres")
reste = liste.queue().copie()
liste.ajouter_fin("Rome")
print(f'liste : {liste}')
print(f'reste : {reste}')

print(10*'#')
print("Question 4.1 et 4.2")
liste1 = Liste()
liste1.inserer("Lille")
liste1.inserer("Bcp Ligny")
print(f'liste1 : {liste1}')

liste2 = Liste()
liste2.inserer(liste)
liste2.inserer(liste1)
print(f'liste2 : {liste2}')

for liste_ville in liste2.elements_liste():
    for ville in liste_ville.elements_liste():
        print(ville)
        
"""
    def ajouter_fin(self, elt):
        if self.est_vide():
            self.inserer(elt)
        else:
            c = self.debut
            while c.suivante != None:
                c = c.suivante
            c.suivante = Cellule(elt)
"""