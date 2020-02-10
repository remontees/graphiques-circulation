# Programme de **tracé de graphiques de circulation**

## Présentation

Ce programme est un exécutable en ligne de commande permettant de générer des [graphiques de circulation](https://fr.wikipedia.org/wiki/Graphique_de_circulation). Ces graphiques espace-temps conduisent à tracer sous forme de ligne brisée la circulation de l'ensemble des trains sur une période donnée. On trouve ainsi en ordonnée les points kilométriques de la ligne (avec le nom des points singuliers principaux de la ligne) et l'heure de circulation correspondante en abscisse.

Pour générer ces graphiques, ce programme a besoin de deux classeurs au format **.xls** (fichier de type *Excel* 2003) :
* l'un contenant la liste des gares desservies sur la ligne avec leurs points kilométriques respectifs ;
* l'autre contenant les horaires de passage des différents trains de la ligne.

Des modèles de ces deux classeurs requis sont présentés dans le répertoire `models`.

## Installation

Veillez avant toute chose à installer les dépendances de l'application en exécutant la commande `pip3 install -r requirements.txt` depuis la racine du projet.

## Utilisation

Exemple de commande pour générer les graphiques associés aux classeurs *Excel* de tests :
```./run_traceur_cli.py models/gares-model.xls models/sillons-model.xls```

Vous obtiendrez ainsi ce genre de graphiques :

![Graphique fictif obtenu avec les données de modèle.](models/graphe_model.png "Graphique fictif obtenu avec les données du modèle.")
