# CH3 : Structures de données - Listes et dictionnaires

??? note "Programme officiel"
    ![image](img/prog_off.png){: .center}
    ![image](img/BO2.png){: .center}

Le langage Python dispose, comme tous les langages de haut niveau, d'un ensemble de types simples et de types structurés vus dans le programme de première : nombres, booléens, chaînes de caractères, tuples, tableaux, dictionnaires ...
Ces types de bases sont appellés **types concrets**. Cette année, comme nous allons manipuler des données plus complexes que des simples nombres, on va créer des structures de données plus complexes. Pour définir ces structures, on utilise des **types abstraits de données**.

## 1. Type abstrait de données

### 1.1 Interface
Un **type abstrait** est caractérisé par une **interface de programmation**. L'interface, c'est l'ensemble des **opérations** ou **primitives** qui vont permettre de manipuler les données.

On distingue :
- les **constructeurs** qui permettent de créer une nouvelle structure de données.
- les **opérateurs** qui permettent de modifier la structure. On peut par exemple ajouter ou retirer des données.
- les **accesseurs** qui donnent des informations sur la structure. Par exemple, donner le nombre d'éléments dans la structure.
- les **itérateurs** qui permettent d'énumérer les éléments de la structure.

### 1.2 Implémentation
**Implémenter** un type abstrait, c'est coder les différentes opérations qui répondent à spécification de l'interface. Il est possible de réaliser plusieurs implémentations différentes pour répondre à la même spécification. Certaines implémentation vont être plus rapides,  moins gourmandes en espace mémoire, plus adaptées à la taille des données ...


!!! exp "Du concret pour mieux comprendre : INTERFACE vs IMPLÉMENTATION"
    On peut choisir comme image une machine à café à capsule, dans laquelle on peut distinguer :
    
    <center>**L'interface**</center>
    ![image](img/nespressoInterface.webp){: .center width=50%}

    On distinge ici : les boutons, le levier, les petites lumières ... C'est la partie **utilisateur**.

    <center>**L'implémentation**</center>
    ![image](img/nespressoImplementation.png){: .center width=50%}

    Sur ce schéma apparaissent : les électrovannes, la pompe, le bloc de chauffe, voire le déroulement des opérations ... C'est la partie **constructeur**.

    Pas besoin de savoir comment fonctionne la machine à l'intérieur (implémentation), pour se faire un café (interface)...
   
Dans notre programme de terminale, on va présenter plusieurs types abstraits comme : les listes (Ne pas confondre avec le type `list` de Python), les piles, les files ... On va apprendre à utiliser ces types, puis on les implémentera de différentes façon.

### 1.3 Exemple des tableaux
En première, on utilise des objets de type `list` pour manipuler des données. Le type `list` est un type concret du langage Python. Par abus de langage on appelle cela des **listes** mais en fait ce sont des **tableaux dynamiques**. L'interface de ce type serait :


| Opérations  | Exemple(s)             |complexité|
|-------------|------------------------|----------|
|Constructeurs|`l = []` ou `l = list()`| O(1)     |
|accesseurs   | `len(l)`               | O(1)     |
|             | `l[i]`                 | O(1)     |
|opérateurs   | `l[i] = x`             | O(1)     |
|             | `l.append(x)`          | O(1)     |
|             | `l.insert(i, x)`       | O(n)     |
|             | `l.pop()`              | O(1)     |
|             | `del l[i]`             | O(n)     |
|itérateurs   | `for elt in l`         | O(n)     |


??? question "Exercice 1"
    === "Énoncé"
        Donner le contenu de la variable `l` après avoir executer les instructions ci-dessous :
        ```python
        >>> l = list()
        >>> l.append(4)
        >>> l.append(6)
        >>> l.insert(0, 6)
        >>> l.pop()
        >>> l[0] = 2
        >>> l.append(3)
        ```
    === "Solution"
        ```python
        [2, 4, 3]
        ```
        Là encore pas besoin de comprendre comment cela fonction. Il suffit juste d'utiliser l'interface.

### 1.4 Exemples de types abstraits
Voici les différents types abstraits que l'on va étudier cette année.
![image](img/tda.png){: .center}

En informatique comme dans la vie courante, il est conseillé d'adapter sa manière de stocker et de traiter des données en fonction de la nature de celles-ci :

- Le serveur d'un café, chargé de transporter les boissons du comptoir aux tables des clients, n'utilisera pas un sac en plastique pour faire le transport : il préfèrera un plateau. 
- Le chercheur de champignons, lui, n'utilisera pas un plateau pour stocker ses trouvailles : il préfèrera un panier.
- Pour stocker des chaussettes, on préfèrera les entasser dans un tiroir (après les avoir appairées), plutôt que de les suspendre à des cintres. 

De même en informatique, pour chaque type de données, pour chaque utilisation prévue, une structure particulière de données se revèlera (peut-être) plus adaptée qu'une autre.

Intéressons nous par exemple aux **données linéaires**. Ce sont des données qui ne comportent pas de *hiérarchie* : toutes les données sont de la même nature et ont le même rôle. 
Par exemple, un relevé mensuel de températures, la liste des élèves d'une classe, un historique d'opérations bancaires... 

Ces données sont «plates», n'ont pas de sous-domaines : la structure de **liste** paraît parfaitement adaptée. 

Lorsque les données de cette liste sont en fait des couples (comme dans le cas d'une liste de noms/numéros de téléphone), alors la structure la plus adaptée est sans doute celle du **dictionnaire**.

Les listes et les dictionnaires sont donc des exemples de structures de **données linéaires**.


## 2. Les listes
### 2.1 Définitions générales
Une liste est un ensemble ordonné d'objets. Généralement, ces données seront de même type, mais ce n'est pas structurellement obligatoire.

![image](img/linked.png){: .center width=40%}

Lorsque l'implémentation de la liste fait apparaître une chaîne de valeurs, chacune pointant vers la suivante, on dit que la liste est une liste **chaînée**.

![image](img/listechainee.png){: .center}

L'interface minimale d'une liste est :

- **constructeur** : `creer_liste()` qui retourne une liste vide.
- **accesseur** : `liste_vide(l)` qui retourne `True` si la liste l est vide.
- **opérateur** : `inserer(e, l)` qui insère l'élément `e` dans la liste `l` et retourne une nouvelle liste.
- **accesseur** : `tete(l)` qui retourne l'élément en tête de liste (si elle n'est pas vide).
- **accesseur** : `queue(l)` qui retourne la liste privée de son premier élément (la tête)(si elle n'est pas vide).
- **itérateur** : `elements_liste(l)` qui retourne un tableau contenant les éléments de la liste `l`, que l'on peut ensuite énumérer avec une boucle for.

### 2.2 Exemple d'implémentation par des tuples
On peut implémenter une liste en Python en utilisant des tuples. Une liste sera représentée par un tuple `(tete, queue)`. `tete` est le premier élément de la liste et `queue` est le reste de la liste, qui est elle même une liste. C'est récursif.

On peut utiliser la liste de la manière suivante :
```python linenums='1'
>>> liste = creer_liste()
>>> liste = inserer("Alice", liste)
>>> liste = inserer("Bob", liste)
>>> liste = inserer("Charlie", liste)
>>> print(tete(liste))
Charlie
>>> print(queue(liste))
("Bob", ("Alice", ()))
>>>for elt in elements_liste(liste):
        print(elt)
Charlie
Bob
Alice
```

L'état de la liste après la ligne 4 est :
```python
("Charlie", ("Bob", ("Alice", ())))
```
Soit :

![image](img/liste_cours.png)

Les différentes étapes de l'implémentation de l'interface sont à réaliser en complétant le fichier [listes_cours.py](listes_cours.py).

#### Le constructeur : création de la liste
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `creer_liste` qui ne prend pas d'argument et qui renvoie un tuple.
    === "Solution"
        ```python
        def creer_liste():
            return ()
        ```

#### Un accesseur : savoir si la liste est vide
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `liste_vide` qui prend en argument une liste et qui renvoie `True` si la liste est vide.
    === "Solution"
        ```python
        def liste_vide(liste):
            return liste == ()
        ```

#### Un opérateur : insertion d'un élément
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `inserer` qui prend en argument un élément et une liste et qui renvoie la liste.
    === "Aides"
        L'élément est ajouté en tête de liste et la liste vient en queue.
    === "Solution"
        ```python
        def inserer(elt, liste):
            return (elt, liste)
        ```

#### Des accesseurs :
!!! question "Exercice"
    === "Énoncé"
        Créer deux fonctions :

        - `tete` qui prend en argument une liste et qui renvoie l'élément en tête de liste.
        - `queue` qui prend en argument une liste et qui renvoie la liste privée de sa tête.
    === "Aides"
        Vérifier pour les deux fonctions que la liste passée en argument n'est pas vide avec un `assert`.
    === "Solution"
        ```python
        def tete(liste):
            assert not liste_vide(liste), "liste vide"
            return liste[0]

        def queue(liste):
            assert not liste_vide(liste), 'liste vide'
            return liste[1]
        ```

#### Un itérateur : lister les éléments présents dans la liste
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `elements_liste` qui prend en argument une liste et qui renvoie un tableau contenant les éléments de la liste.
    === "Aides"
        La fonction doit retourner un tableau.

        Utiliser une boucle while pour parcourir la liste.
    === "Solution"
        ```python
        def elements_liste(liste):
            tab_iter = []
            while not liste_vide(liste):
                tab_iter.append(tete(liste))
                liste = queue(liste)
            return tab_iter
        ```

#### Étendre l'interface
On peut ajouter un accesseur `taille` qui retourne le nombre d'éléments de la liste.
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `taille` qui prend en argument une liste et qui renvoie le nombre d'éléments de la liste.
    === "Solution"
        ```python
        def taille(liste):
            nb = 0
            while not liste_vide(liste):
                nb = nb + 1
                liste = queue(liste)
            return nb
        ```

### 2.3 Autre implémentation et utilisation des listes
Travail à réaliser sur le notebook TD_listes.ypnb

Il vous est conseillé de faire et conserver un fichier (module) nommé listes.py avec l'implémentation utilisant la POO.

## 3. Les dictionnaires
### 3.1 tableau associatif
Les dictionnaires ont déjà été étudiés en classe de première. Pour rappel, ce type de données,
aussi appelé **tableau associatif** , permet de stocker des **valeurs** et d'y accéder au moyen d'une **clé** ,
contrairement au tableau qui permet d'accéder à une donnée au moyen d'un indice .

On parle d'association **clé: valeur**. Le langage Python fournit directement le type structuré `dict` qui implémente un dictionnaire.

- **Constructeur** : ```d = dict()``` ou ```d = {}``` , création d'un dictionnaire nommé `d`.
- **opérateur** : ```d[cle] = valeur``` , ajouter une association `cle: valeur` dans `d`.
- **accesseur** : ```d[cle]``` , lire la `valeur` associée à `cle` dans `d`.
- **itérateur** : ```for cle in d``` , énumèrer toutes les clés de `d`.

!!! exemple "Exemple"
    ```python
    >>> dico = dict()
    >>> dico["nom"] = "Jannel"
    >>> dico["prenom"] = "David"
    >>> print(f:"{dico["nom"]} {dico["prenom"]}")
    Jannel David
    ```

La recherche dans un dictionnaire est optimisée pour s'effectuer sur les clés et non sur les
valeurs. Par exemple avec le dictionnaire que nous avons créé précédemment dans l'exemple, la commande
```"Nom" in dico``` renverra `True` alors que ```"Jannel" in dico``` renverra `False` . Dans un dictionnaire, 
les clés et les valeurs ne jouent donc pas du tout le même rôle et ne sont pas interchangeables.

### 3.2 Tables de hachage et clés
Une clé peut être d'un autre type que chaîne de caractère, du moment que c'est un objet
non mutable , c'est à dire qui ne peut pas être modifié. Une clé ne peut pas être une liste
par exemple car une liste est un objet mutable que l'on peut modifier, par exemple au travers
de la méthode .append().

Regardons ce qui se passe si on essaye de définir une clé de type list pour un dictionnaire :
```python
>>> dico[[2, 1]] = "blablabla ..."
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
```
Le type `list` n'est pas pas **hashable** . Mais qu'est-ce que le hachage ?


[![Watch the video](img/hachage.jpeg){ width=50% ; align=center}](https://youtu.be/IhJo8sXLfVw)

### 3.3 Implémentation d'un type *dictionnaire* à l'aide d'une table de hachage
#### Présentation du problème
Ici on ne veut pas utiliser directement le type `dict` de Python. Une implémentation simple consiste à créer une liste de tuples `(cle, valeur)`.

Le problème de cette implémentation est dans l'efficacité de la recherche d'une clé. On doit parcourir la totalité de la liste au pire des cas et donc la compléxité est linéaire O(n).

Une implémentation plus efficace est donc de continuer à utiliser un tableau et à transformer la clé en un indice à l'aide d'une fonction de hachage. Ça a l'avantage de trouver directement une clé dans le tableau. La fonction de hachage transforme la clé en un indice et il suffit donc de lire la donnée stockée dans le tableau à l'indice correspondant. La complexité de la recherche est donc O(1).

Les différentes étapes de l'implémentation de l'interface sont à réaliser en complétant le fichier [table_hachage_cours.py](table_hachage_cours.py).

#### La fonction de hachage
Si on prend pour clé une chaine de caractère, une fonction de hachage peut consister à additionner le code ascii de chaque caractère, modulo la taille du tableau.
```python
HTAILLE = 109 # taille de la table de hachage
def hachage(cle):
    code = 0
    for car in cle:
        code = code + ord(car)
    return code % HTAILLE
```
!!! question "Question"
    === "Question"
        Quel soucis peut appaître avec une telle fonction de hachage ?
    === "Réponse"
        Il est possible que deux clés différentes aient le même code de hachage. On appelle cela une **collision**.

        Une méthode pour traiter ces collisions, consiste à stocker dans chaque élément de la table de hachage, une liste des tuples `(cle, valeur)`
        qui on le même code de hachage. C'est cette implémentation qui vous est proposée ci-dessous.

        Vous pouvez tester la fonction en prenant HTAILLE = 7 et deux clés comme "Alice" et "Bob". La fonction renvoie 2 pour les deux clés. 

#### Le constructeur : Création du dictionnaire
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `creer_dico` qui ne prend pas d'argument et qui renvoie un tableau contenant `HTAILLE` cases remplies avec `None`.
    === "Solution"
        ```python
        def creer_dico():
            return [None] * HTAILLE
        ```

#### Un opérateur : Ajouter une entrée dans le dictionnaire
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `ajouter` qui prend en arguments `dico`, `cle` et `valeur` et qui ajoute le couple `(cle, valeur)` dans le dictionnaire `dico`.
    === "Aides"
        Utiliser les opérations spécifiées dans l'interface des listes données en cours. L'interface et ses opérations doivent être importées dans votre fichier.

        Les entrées de la table de hachage étant des listes, il faut penser à créer une nouvelle liste si elle n'existe pas avant d'ajouter le tuple au dictionnaire.
    === "Solution"
        ```python
        def ajouter_cle(dico, cle, valeur):
            h = hachage(cle)
            if dico[h] == None:
                dico[h] = creer_liste()
            dico[h] = inserer((cle, valeur), dico[h])
            return dico
        ```

#### Un accesseur : lire la valeur associée à un clé du dictionnaire
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `valeur_cle` qui prend en arguments `dico` et `cle`. Et qui retourne la valeur associée à la clé dans le dictionnaire `dico`.
    === "Aides"
        Vérifier que le résultat de la fonction de hachage, appliquée à la clé, correspond à une liste sinon retourner `None`.
        
        La fonction `elements_liste` permet de récupérer une liste de tous les tuples présents dans une liste.

    === "Solution"
        ```python
        def valeur_cle(dico, cle):
            h = hachage(cle)
            if dico[h] == None:
                return None
            else:
                for (c, v) in elements_liste(dico[h]):
                    if c == cle:
                    return v
            return None
        ```

#### Un itérateur : lister les clés présentes dans un dictionnaire
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `cle_dico` qui prend en arguments `dico`. Et qui retourne la liste des clés présentes dans le dictionnaire `dico`.
    === "Aides"
        La fonction doit retourner un tableau de clés.
        
        La fonction `elements_liste` permet de récupérer une liste de tous les tuples `(cle, valeur)` présents dans une liste.

    === "Solution"
        ```python
        def cles_dico(dico):
            tab_cles = []
            for h in range(len(dico)):
                if dico[h] != None:
                    for (c, v) in elements_liste(dico[h]):
                        tab_cles.append(c)
            return tab_cles
        ```


#### Étendre l'interface :
L'objectif est d'ajouter une fonction permettant de connaitre le nombre d'éléments (couples) présents dans le dictionnaire.

!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `taille` qui prend en arguments `dico`. Et qui retourne le nombre d'éléments présents dans le dictionnaire `dico`.


    === "Solution"
        Une façon de procéder est de compter le nombre de clés présentes dans le tableau renvoyé par l'itérateur `cle_dico`.
        ```python
        def taille(dico):
            return len(cles_dico(dico))
        ```

#### Utiliser l'interface :
Créer une fonction moyenne qui retourne la moyenne des notes présentes dans un dictionnaire ou les clés seraient des noms d'élèves et la valeur associée la note.
!!! question "Exercice"
    === "Énoncé"
        Créer une fonction `moyenne` qui prend en arguments `dico`. Et qui retourne la moyenne des valeurs présentes dans le dictionnaire `dico`.
    === "Aides"
        Tester si le dictionnaire n'est pas vide.


        Utiliser les fonctions `cle_dico`, `valeur_cle` et `taille` pour calculer la moyenne.

    === "Solution"
        ```python
        def moyenne(dico):
            assert cles_dico(dico) != [], "dictionnaire vide"
            total = 0
                for cle in cles_dico(dico):
                    total = total + valeur_cle(dico, cle)
            return total / taille(dico)
        ```