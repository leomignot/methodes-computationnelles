# Méthodes Computationnelles - 4A

Ce repo contiendra les supports pour le cours de Méthodes Computationnelles 4A - Sciences Po Bordeaux (24 séances * 1H30).

## Table des matières  <!-- omit in toc -->

<!-- no toc -->
- [Introduction](#introduction)
- [Format](#format-du-cours-et-programme-prévisionnel)
- [Validation](#validation-des-acquis)
- [Calendrier](#calendrier)
- [Contact](#contact--support)
- [Liens utiles](#liens-utiles)

## Introduction

Comment explorer des masses de données complexes et les transformer en connaissance ?

La numérisation des sociétés a profondément transformé la quantité et la nature des données disponibles sur les individus et leurs comportements. Associée au développement des puissances de calcul et l'apparition de nouveaux outils, cette évolution a contribué à un renouvellement des objets de recherche et des méthodes en sciences sociales.

Dans ce contexte, la capacité à collecter, comprendre et analyser des données est devenue une compétence importante pour les chercheur·es et a conduit à l'emergence des sciences sociales computationnelles.

Cet atelier propose une initiation progressive aux méthodes computationnelles à l'aide du langage Python. Aucun prérequis dans ces domaines n'est exigé.

En s'inscrivant dans une réflexion critique sur les usages computationnels en sciences sociales, il s'agira d'apprendre à collecter, manipuler, explorer et analyser des données empiriques dans le cadre de projets de recherche en sociologie et science politique.

<!--
Dans un monde où les données sont omniprésentes
tout en interrogeant les avantages et limites de ces méthodes.
Tout au long du module des thèmes tels que la polarisation, le knowledge gap, la participation électorale ou encore la confiance politique seront explorés.
-->

### À la fin du semestre, vous saurez <!-- omit in toc -->

- Mobiliser des méthodes computationnelles pour vos projets.
- Réaliser les étapes clés d'un projet : collecte, chargement, préparation, analyses statistiques & textuelles, production graphique, etc.
- Choisir les méthodes et outils pertinents selon vos données et questions de recherche.
- Exercer un regard critique sur ces méthodes, comprendre leurs avantages et leurs limites (enjeux éthiques, théoriques, etc.).
- Mobiliser des bibliothèques Python devenues incontournables en analyse de données, NLP, etc.

## Format du cours et programme prévisionnel

Les séances sont organisées en format atelier. Chaque séance comportera une dimension pratique, avec des temps d'application et exercices sur des cas concrets. Le module est organisé en séquences progressives :

- au premier semestre : (1) installation de l’environnement de travail, (2) introduction au traitement et la manipulation de données, (3) statistiques et visualisations, (4) introduction aux principes du machine learning et de l'intelligence artificielle, (5) collecte de données sur le web (web scrapping et API)
- au second semestre : (6) traitement automatique des langues (TAL/NLP), (7) Projets et analyse de réseau, (8) autonomie et installation locale.

**Blocs semestre 1 :**

Bloc 1 – Mise en place & premiers pas (1 séance)  
*Objectif : permettre à chacun·e de disposer d’un environnement de travail fonctionnel*

- Présentation du cours et des attendus
- Présentation de l'environnement de développement (Google Colab) et prise en main
- Exécution d’un premier script à partir d'un code fourni par les enseignants

Bloc 2 – Initiation à Python et à Pandas (5 séances)  
*Objectif : acquérir les bases de la programmation et du traitement de données*

- Syntaxe de base en Python
- Introduction à Pandas : chargement de bases, nettoyage, recodage, analyse
- Manipulation de variables et statistiques descriptives

Bloc 3 – Statistiques et visualisations (2 séances)  
*Objectif : maîtriser les grands types de visualisation selon la nature des variables, s'approprier les outils statistiques*

- Visualisations univariées : histogrammes, barplots, boxplots, lineplots
- Visualisations bivariées : scatterplots, lineplots, boxplots croisés
- Tests statistiques, régression linéaire et logistique

Bloc 4 – Fondamentaux du Machine Learning et de l'IA (2 séances)  
*Objectif : découvrir les grands principes du ML et de l'IA générative*

- Panorama de l'IA
- ML : entraînement de modèles, train et test sets, etc.
- Principes de fonctionnement et cas d'usages en sciences sociales

Bloc 5 – Collecte de données sur le Web (2 séances)  
*Objectif : constituer un corpus de données à partir du web*

- Web scraping : principes et mise en pratique
- Les API et les données ouvertes

**Blocs semestre 2 :**

Bloc 6 – Traitement automatique des langues (TAL/NLP)  
*Objectif : découvrir l'analyse automatique de textes, des classiques à l'IA Générative*

- Bag of words, matrices documents-termes, TF-IDF
- Embeddings et transformers
- BERT et classifiers
- Topic modelling
- LLM, GPT et IA générative
- Évaluer un modèle

Bloc 7 – Projets et analyse de réseau  
*Objectif : travailler sur un projet et s'initier à l'analyse de réseau*

- Ateliers projets
- Données relationnelles

Bloc 8 – Autonomie (2 séances)  
*Objectif : autonomie et installation locale, prendre du recul sur les méthodes*

- Rappel enjeux éthiques & régulation
- Outillage, installation locale, reproductibilité
- Bilan, présentations informelles

*Ce programme est provisoire et est susceptible de changer selon les besoins des étudiant.es et le déroulement du cours.*

## Validation des acquis

Ce module, adoptant une approche incrémentale, propose une évaluation continue par la remise de trois types de rendus : des démonstrations, des notes de lecture et des rendus computationnels.

| Date rendu | Description                                         | Poids |
|------------|-----------------------------------------------------|-------|
| **Semestre 1** |  |  |
| Selon GP   | Démo commentée                                      | 30%   |
| Séance Y   | Note de lecture                                     | 30%   |
| xx/yy/zzzz | Rendu computationnel : infographie ou analyse stat  | 40%   |
| **Semestre 2** |  |  |
| Selon GP   | Démo commentée                                      | 30%   |
| Séance Y   | Note de lecture                                     | 30%   |
| xx/yy/zzzz | Rendu computationnel : application des méthodes     | 40%   |

**Description des rendus :**

- **Démo commentée  :** Remise d'un notebook démonstratif et présentation orale (10 minutes) = vous assurez un mini-cours.
- **Note de lecture :** Note de lecture en 2 pages d'un article de sciences sociales computationnelles. Idéalement en lien avec le sujet de mémoire envisagé, ou plus générique.
- **Rendu computationnel :** Application des éléments de programmation. Au premier semestre, rendu d'une infographie ou d'une analyse statistique. Au deuxième semestre, rendu d'un projet appliquant des méthodes de NLP.
- **Critères de réussite des rendus :** Voir les [consignes](https://github.com/leomignot/methodes-computationnelles/tree/main/rendus).

<!-- TODO: Établir suite consignes rendu -->

## Calendrier

**Semestre 1 :**

| Séance | Description | Slides | Rendu |
|---|---|---|---|
| Séance 1 | Introduction |  |  |
| Séance 2 | Programmer en Python I |  |  |
| Séance 3 | Programmer en Python II |  |  |
| Séance 4 | Charger et explorer des données |  |  |
| Séance 5 | Filtrer et analyser des données |  |  |
| Séance 6 | Recoder et créer des variables |  |  |
| Séance 7 | Statistiques et Visualisations I |  |  |
| Séance 8 | Statistiques et Visualisations II |  |  |
| Séance 9 | Fondamentaux ML & IA I |  |  |
| Séance 10 | Fondamentaux ML & IA II |  |  |
| Séance 11 | Collecter des données sur le Web (web scraping) |  |  |
| Séance 12 | Les API et les données ouvertes |  |  |
| XX/yy/ZZZZ | Rendu S1 |  |  |

**Semestre 2 :**

| Séance | Description | Slides | Rendu |
|---|---|---|---|
| Séance 13 | C'est la reprise + suite accès données |  |  |
| Séance 14 | Text as data 101 (BoW, DTM, TF-IDF) |  |  |
| Séance 15 | Le texte en contexte (SPACY, POS, NER, Embeddings) |  |  |
| Séance 16 | Topic modelling avec BERTopic |  |  |
| Séance 17 | Classifier (BERT, Active Tigger) |  |  |
| Séance 18 | Le texte génératif (LLM et IA GEN) |  |  |
| Séance 19 | Requête LLM et prompt engineering |  |  |
| Séance 20 | Évaluer les modèles |  |  |
| Séance 21 | Atelier projet I + bonus Réseaux et données relationnelles |  |  |
| Séance 22 | Atelier projet II + bonus Réseaux et données relationnelles |  |  |
| Séance 23 | Autonomie : outillage et installation locale |  |  |
| Séance 24 | Perspectives et bilan du cours |  |  |
| XX/yy/ZZZZ | Rendu S2 |  |  |

## Contact & Support

- **:calendar: Prendre rendez-vous :** [Léo Mignot](mailto:l.mignot@sciencespobordeaux.fr)

## Liens utiles

Cours et formations :

- https://pythonds.linogaliana.fr
- https://melaniewalsh.github.io/Intro-Cultural-Analytics/welcome.html
- https://github.com/mickaeltemporao/lillelms
- https://github.com/css-polytechnique/SICSS-2025-Material
- https://paulcbauer.github.io/teaching.html

Livres :

- https://www.bitbybitbook.com/
- https://press.princeton.edu/books/hardcover/9780691207544/text-as-data

<!-- ACTUALISER LISTE -->

## Licence  <!-- omit in toc -->

Ce projet est sous licence Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0). Vous êtes libre d'utiliser, copier, adapter ce contenu ou le partager à condition de créditer les auteurs originaux, de ne pas en faire un usage commercial et de distribuer toute oeuvre dérivée sous cette même licence.

## À propos  <!-- omit in toc -->

Une partie des contenus proposés ici s'inspire de ressources pédagogiques disponibles sous licence libre et d'échanges et collaborations avec d'autres contributeur·ices, notamment :

- Axel Morin
- Émilien Schultz
- Mickael Temporão
- Flore Vancompernolle Vromman
- Corentin Vande Kerckhove

(N'hésitez pas à signaler si un crédit venait à manquer)
