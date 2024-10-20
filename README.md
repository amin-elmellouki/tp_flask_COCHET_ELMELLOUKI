# Projet flask 2024

## Présentation du projet

Ce projet consiste en la création d'un site web répertoriant des livres de science-fiction.<br>Le projet est développé en Python avec le framework Flask ainsi qu'en HTML/CSS.

## Développeurs

- **Amin EL MELLOUKI**
- **Raphaël COCHET**

## Installation

### Importation du projet
Importer le projet en clonant le [dépôt git](https://github.com/amin-elmellouki/tp_flask_COCHET_ELMELLOUKI.git) sur votre machine.


### Création de l'environnement virtuel

- Placez vous dans le répertoire racine du projet.
- `requirements.txt` contient toutes les dépendances utilisées. 
- Pour créer un environnement virtuel et y installer les dépendances, exécutez les commandes suivantes:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Lancement de l'application

1. Pour pouvoir lancer l'application il faut tout d'abord créer les tables nécessaires avec la commande suivante:
```bash
flask syncdb
```

2. A présent vous pouvez lancer l'application avec la commande suivante:
```bash
flask run
```

## Fonctionnalités implémentées

### Fonctionnalités primaires
- Affichage des livres, détails (au click)<br>
- Intégration Bootstrap<br>
- Edition/Ajout/Suppression Auteurs<br>
- Edition/Ajout/Suppression Livres<br>
- Recherche des livres par auteur<br>
- commande d’import de données (loaddb)<br>
- commande de création des tables (syncdb)<br>
- Login (commandes newuser, password) avec limitation des pages d’édition aux utilisateurs authentifiés.

### Fonctionnalités supplémentaires
- Possibilité d’avoir des favoris par utilisateur <br>
- Affichage paginé des livres, par ordre alphabétique des auteurs<br>
- Recherche avancée des livres par titre, auteur, prix minimum et prix maximum<br>
- Possibilité de passer au livre suivant ou précédent avec des boutons sur la page de 
  détail d'un livre<br>
- Ajout d'une page affichant tous les auteurs<br>
- Ajout des livres écris par l'auteur sur sa page de détail<br>
- Retirer un livre des favoris depuis sa page de détail<br>
- Accéder aux détails de l'auteur d'un livre à partir de la page de déatil du livre<br>
- Amélioration du défilement (scroll) avec l'ajout d'un bouton d'un retour en haut de page<br>
- Ajout d'une page affichant tous les favoris d'un utilisateur
- Ajout d'une inscription au site web pour les personnes n'ayant pas de compte