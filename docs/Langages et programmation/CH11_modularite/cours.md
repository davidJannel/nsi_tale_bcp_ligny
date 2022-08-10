# CH11 : Modularité - API

??? note "Programme officiel"
    ![image](img/BO.png){: .center}

## 1. Qu'est qu'une API ?
Une **API** (en anglais « Application programming interface ») est une interface de programmation d’application. Elle est destinée à être utilisée par des programmes. Le principe de ce type d’interface est le même que celui des **UI** (« User Interface ») ou des **GUI** (« Graphical User Interface ») destinées elles à un utilisateur humain.

Composée de constantes, de fonctions, de classes, elle sert de lien entre un programme et les programmes qui vont l’utiliser. Elle peut être proposée par un service web avec une documentation décrivant l’utilisation qui permettra la communication et l’échange des données. Il existe, par exemple, plusieurs API de géolocalisation qui peuvent être intégrées à des programmes. Une API est très souvent proposée par une bibliothèque logicielle composée de fonctions destinées à être utilisées dans divers programmes.

Le principe de base est que le fonctionnement interne n’a pas besoin d’être connu du programme utilisateur. Cela nécessite une documentation fournie décrivant précisément son l’utilisation. Ainsi, lors de l’élaboration d’un logiciel il est possible d’utiliser des parties d’autres logiciels, sans connaître leur fonctionnement interne, si l’on sait comment faire interagir ces différentes parties.
Par exemple, pour utiliser une fonction il suffit de connaître sa spécification, c’est à dire son nom, les types de ses paramètres et de la valeur qu’elle retourne et sa documentation. Dans tous les cas, l’utilisateur, un programme ou un humain, se contente de fournir les données demandées et obtient le résultat du traitement.

On s'intéresse ici à la Base Adresse Nationale qui est une API gratuite du gouvernement français permettant d'obtenir un certain nombre d'informations à partir d'une adresse postale.

## 2. Interrogation de l'API
On souhaite, grâce à l'API, obtenir des informations sur l'adresse postale de l'institution Ste Marie. Pour interroger l'API, il suffit d'envoyer une requête GET à l'URL [https://api-adresse.data.gouv.fr/search/?q=54-rue-de-l-eglise&postcode=59134](https://api-adresse.data.gouv.fr/search/?q=54-rue-de-l-eglise&postcode=59134).

On remarque que l'adresse postale sur laquelle on souhaite interroger l'API est indiquée dans l'URL. La réponse renvoyée par l'API est la suivante :

```json
{"type": "FeatureCollection", "version": "draft", "features": [{"type": "Feature", "geometry": {"type": "Point", "coordinates": [2.919014, 50.603896]}, "properties": {"label": "Rue de l\u2019Eglise 59134 Beaucamps-Ligny", "score": 0.7158977005347593, "id": "59056_0060", "name": "Rue de l\u2019Eglise", "postcode": "59134", "citycode": "59056", "x": 694257.21, "y": 7056318.52, "city": "Beaucamps-Ligny", "context": "59, Nord, Hauts-de-France", "type": "street", "importance": 0.46311}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [2.864853, 50.571784]}, "properties": {"label": "Rue de l\u2019Eglise 59134 Wicres", "score": 0.712733155080214, "id": "59658_0020", "name": "Rue de l\u2019Eglise", "postcode": "59134", "citycode": "59658", "x": 690410.49, "y": 7052745.79, "city": "Wicres", "context": "59, Nord, Hauts-de-France", "type": "street", "importance": 0.4283}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [2.884764, 50.614966]}, "properties": {"label": "Rue de l\u2019Eglise 59134 Le Maisnil", "score": 0.7101831550802139, "id": "59371_0060", "name": "Rue de l\u2019Eglise", "postcode": "59134", "citycode": "59371", "x": 691830.32, "y": 7057555.01, "city": "Le Maisnil", "context": "59, Nord, Hauts-de-France", "type": "street", "importance": 0.40025}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [2.86755, 50.570217]}, "properties": {"label": "Rue de l\u2019Eglise et Bas Champ 59134 Wicres", "score": 0.41261, "id": "59658_gy8iak", "name": "Rue de l\u2019Eglise et Bas Champ", "postcode": "59134", "citycode": "59658", "x": 690601.57, "y": 7052570.87, "city": "Wicres", "context": "59, Nord, Hauts-de-France", "type": "street", "importance": 0.33871}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [2.86596, 50.572264]}, "properties": {"label": "Chemin Pieton Rues (l\u2019Eglise - Viguier) 59134 Wicres", "score": 0.2762463636363636, "id": "59658_k3ui6a", "name": "Chemin Pieton Rues (l\u2019Eglise - Viguier)", "postcode": "59134", "citycode": "59658", "x": 690489.13, "y": 7052799.13, "city": "Wicres", "context": "59, Nord, Hauts-de-France", "type": "street", "importance": 0.33871}}], "attribution": "BAN", "licence": "ETALAB-2.0", "query": "54-rue-de-l-eglise", "filters": {"postcode": "59134"}, "limit": 5}
```

La réponse reçue est au format JSON (JavaScript Object Notation). La signification des champs de la réponse est donnée dans la [documentation](https://adresse.data.gouv.fr/api-doc/adresse) de l'API.

L'interrogation de l'API peut être réalisée grâce au code Python ci-dessous. Lors de son exécution, la réponse renvoyée par l'API est stockée dans la variable reponse.

```python linenums='1'
import requests
url = "https://api-adresse.data.gouv.fr/search/?q=54-rue-de-l-eglise&postcode=59134"
reponse = requests.get(url)
reponse = reponse.json()
```
