# Projet X-D-FENCE

**X-D-FENCE** est un petit projet en Python qui permet de surveiller un dossier en temps réel.
Le but est de détecter automatiquement si un fichier est créé, modifié ou supprimé, et d'enregistrer ces événements dans un fichier de log.

---

## Fonctionnalités

- Surveillance d'un dossier en continu
- Détection de :
    - Création de fichiers
    - Modification de fichiers
    - Suppression de fichiers
- Enregistrement des événements détectés dans 'logs/events.log'
- Affichage en temps réel dans le terminal

---

## Prérequis

- Python
- Bibliothèque Python 'watchdog'

Pour installer les dépendances :
'''bash
pip install -r requirements.txt