# %% [markdown]
# # Types de données et structures
#
# **Objectifs d'apprentissage** 
# - les types de données
# - les opérateurs relationnels
# - les opérateurs logiques
# - les listes
# - manipuler les listes
#

# %% [markdown]
# ## Types de données
#
# Python fonctionne avec de nombreux types de données. 
# Voici quelques-uns des types les plus basiques pour commencer :
#
# | Type    | Description               | Exemple   |
# | :-:     |-                          | -         |
# | *int*   | Nombres entiers/naturels  | 42        |
# | *float* | Valeurs décimales         | 0.42      |
# | *str*   | Chaîne de caractères      | "Libéral" |
# | *None*  | Valeurs manquantes        | None      |
# | *bool*  | Valeurs logiques/booléene | True      |
#
# Vous pouvez utiliser la fonction `type()` pour connaitre le type d'un objet.
# Chaque type de données permet d'effectuer des opérations spécifiques et restreint également les fonctions que vous pouvez leur appliquer.
#

# %% [markdown]
# ### Hack Time
#
# Commençons par créer quelques variables.

# %%
# Créons quelques objets

a = 42
b = 5
c = a / b

annee = 2020
parti_1 = "Democrate"
parti_2 = "Conservateur"
description = """
L'American National Election Studies (ANES)
est une série d'enquêtes nationales menées
par des universitaires auprès des électeurs américains,
avant et après chaque élection présidentielle.
"""

sept = "7"
trois = "3"


# %%
# Utilisez la fonction `type()` pour vérifier le type de ces objets


# %%
# ATTENTION : Que se passe-t-il si vous additionnez l'objet sept et l'objet trois ?


# %%
# Python a une représentation spéciale des valeurs booléennes/logiques.
vote_2016 = True
vote_2020 = False

# Que se passe-t-il lorsque vous exécutez ce code ?

# %%
# Que se passe-t-il si vous additionnez des objets booléens ?


# %%
# Python a également un moyen de stocker des informations manquantes ou vides.
resultats_2028 = None

# Quel est le type de cet objet ?

# Pouvez-vous additionner le nombre 100 à resultats_2028 ?


# %% [markdown]
# ## Opérateurs relationnels
#
# Les opérateurs relationnels permettent de comparer des objets. Ils sont également connus sous le nom d'opérateurs de comparaison. Ils sont souvent utilisés dans les instructions conditionnelles et les boucles pour construire des programmes. Les opérateurs relationnels retournent une valeur booléenne.
#
# | Opérateur  | Description      | Exemple |
# | :-:        |-                 | -:      |
# | **==**     | Égal à           | a == b  |
# | **!=**     | Différent de     | a != b  |
# | **<**      | Inférieur à      | a  < b  |
# | **<=**     | Inférieur ou égal| a <= b  |
# | **>**      | Supérieur à      | a  > b  |
# | **>=**     | Supérieur ou égal| a >= b  |
#
#

# %% [markdown]
# ### Hack Time
#

# %%
# Utilisez les opérateurs relationnels pour comparer certains des objets créés précédemment !


# %% [markdown]
# # Opérateurs logiques
#
# Les opérateurs logiques permettent de joindre des expressions booléennes pour créer des conditions plus complexes.
#
# | Opérateur  | Description             | Exemple |
# | :-:        |-                        | :-      |
# | **and**    | Les deux expressions sont vraies | True **and** False  |
# | **or**     | Au moins une expression est vraie | True **or** True  |
# | **not**    | Inverse l'expression    | **not** True |
#
#

# %% [markdown]
# #### Essayez de prédire les résultats des deux cellules suivantes ?

# %%
print(True and True)
print(True and False)
print(False and True)
print(False and False)

# %%
# Essayez de prédire la sortie de cette cellule de code
print(True or True)
print(True or False)
print(False or True)
print(False or False)

# %% [markdown]
# ### Hack Time
#
# Vous avez mené une enquête auprès des étudiants de votre école. 
# Vous avez décidé d'examiner chacune des réponses fournies par les participants et de les coder dans des objets distincts.
#

# %%
# Répondant 1
age = 24
genre = "Feminin"
pays = "France"
travaille = True
vote = True
tiktok = False

# %% [markdown]
# #### Pouvez-vous prédire les résultats des instructions suivantes ?

# %%
pays == "France" and age >= 18


# %%
travaille and not tiktok


# %%
# Vérifier si le répondant peut se présenter à l'élection présidentielle américaine.
# Il doit être né aux États-Unis et être âgé d'au moins 35 ans.


# %% [markdown]
# # Listes
#
# Nous avons maintenant une meilleure compréhension des types de données de base. Les structures de données permettent de combiner plusieurs objets en un seul objet. Les listes sont l'une des structures de données les plus courantes.
#
# Les listes en Python permettent de regrouper n'importe quel nombre d'objets de n'importe quel type en un seul objet. 
#
# Comprendre les listes est la première étape pour travailler efficacement avec de grandes quantités de données.
#
# ## Créer des listes
# Pour créer une liste, vous écrivez simplement les noms d'objets séparés par des virgules à l'intérieur de crochets.
#
# ```python 
# mon_nouvel_objet_liste = [objet_1, objet_2, ...]
# ```
#

# %%
une_liste = [2008, 2012, 2016, 2020, 2024]
une_liste

# %%
type(une_liste)

# %% [markdown]
# ### Hack Time
#

# %%
# Créez une liste nommée `repondant_1` contenant les variables créées précédemment pour le répondant 1
repondant_1 = ...

# %%
# Affichez `repondant_1`


# %%
# Vérifiez le type de l'objet `repondant_1`


# %%
# Quelle est la longueur de cette liste ? Utilisez la fonction `len()` !


# %%
# Créez des valeurs pour un nouveau répondant fictif.
age =
genre =
pays =
travaille =
vote =
twitter =

# Créez un nouvel objet nommé `repondant_2` contenant les valeurs pour ce nouveau répondant.
repondant_2 = [age, genre, pays, travaille, vote, twitter]

# %%
# Créez une nouvelle liste nommée `repondants` contenant les 2 objets repondant_1 et repondant_2


# %% [markdown]
# # Manipulation de listes
#
# Maintenant que nous avons une meilleure compréhension des listes, nous devons apprendre comment sous-ensembler, découper ou modifier leurs éléments.
#
# ### Sous-ensemble

# %%
# Sous-ensembler un élément dans une liste : liste[index]
data = [
    "participation",
    2012,
    54.9,
    "democrate",
    2016,
    55.7,
    "repubilcain",
    2021,
    66.8,
    "democrate",
]
data[1]

# %% [markdown]
# ATTENTION : La plupart des langages de programmation sont indexés à partir de **0**, comme Python !
#
# Pourquoi ? Python lit les informations de gauche à droite. Les langages de programmation sont développés par des humains de différentes cultures. Cela signifie que vous pouvez trouver certaines habitudes culturelles dans de nombreux langages. 
#
# Plongeons dans l'indexation
#
# ```python
# # Ceci est une liste de 4 éléments
# partis = ["democrate","republicain","libertarien","vert"]
#           ^0          ^1            ^2            ^3
# ```

# %%
partis = ["democrate", "republicain", "libertarien", "vert"]
partis[1]

# %% [markdown]
# #### Hack Time
#

# %%
# En utilisant l'objet `data``, affichez le niveau de participation en 2016


# %%
# Calculez le niveau de participation moyen


# %% [markdown]
# ### Découpage de listes
#
# `liste[début:fin]`
#
# Cette notation permet d’extraire une *sous-liste* à partir d’une liste existante.
#
# * `début` correspond à l’indice de départ (inclus).
# * `fin` correspond à l’indice de fin (exclu).
#

# %%
# Découper des listes : liste[début:fin]
data[4:6]


# %% [markdown]
# Dans l’exemple `data[4:6]`, on récupère les éléments de la liste `data` situés aux indices 4 et 5.
# Cette méthode est utile pour sélectionner une portion précise d’une liste sans modifier la liste originale.
#

# %% [markdown]
# #### Hack Time
#

# %%
# Affichez toutes les infos dans l'objet data en lien avec l'élection de 2016


# %% [markdown]
# ### Modifier des listes

# %%
# Une? erreur semble s'être glissée dans nos données
data[7]

# %%
# Modifier une liste
data[7] = 2020
data


# %% [markdown]
# #### Hack Time
#

# %%
# Corrigez la dernière erreur dans le nom du parti


# %% [markdown]
# ### Ajouter des éléments

# %%
# Ajouter des élements à une liste
annee_2008 = [2008, 58.2, "democrate"]
data = data + annee_2008
data


# %% [markdown]
# #### Hack Time

# %%
# Ajoutez les données pour les élections de 2024

# %%
# Calculez le niveau de participation moyen sur toutes les années présentes dans la liste `data`

