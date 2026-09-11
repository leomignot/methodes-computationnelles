# %% [markdown]
# # Introduction à l'exploration des données
#
# **Objectifs d'apprentissage :**  
# - charger un jeu de données  
# - explorer les données  
# - découvrir les fonctions courantes d'exploration de variables
# - et tester des premières visualisations
#
# ## Le pipeline de la Data Science
#
# <!-- passage syntaxe html pour modifier la taille de l'image -->
# <img src="https://mickaeltemporao.github.io/itds/images/pipeline.jpg" alt="pipeline" width="800"/>
#
#

# %% [markdown]
# ## Acquisition de données
# Avec quelques bases de Python, nous allons commencer à combiner des packages existants pour acquérir et explorer des données.
#
#
# Avant de pouvoir commencer à examiner les données, nous devons les charger.

# %%
# Charger les bibliothèques requises
import pandas as pd

# Charger des données avec pandas depuis une URL
data_url = "https://raw.githubusercontent.com/datamisc/ts-2024/main/data.csv"
anes_data = pd.read_csv(data_url, compression="gzip")


# %% [markdown]
# ## Le codebook de l'ANES 2024
# - Page officielle: https://electionstudies.org/data-center/2024-time-series-study/
# - Version web: https://sda.berkeley.edu/sdaweb/docs/anes2024full/DOC/hcbk.htm
# - Version pdf: https://electionstudies.org/anes_timeseries_2024_userguidecodebook_20250808/

# %% [markdown]
# ### Hack Time

# %%
# Quel est le type de anes_data ?


# %% [markdown]
# ### DataFrames
#
# Les DataFrames sont des listes (ou des séries lorsqu'on utilise pandas) qui sont assemblées dans un tableau.
#
# ![](https://storage.googleapis.com/lds-media/images/series-and-dataframe.width-1200.png)

# %%
# Un exemple rapide
participation = [66.8, 55.7, 54.9, 58.2, 56.7, 51.2, 49.0]
annee = [2020, 2016, 2012, 2008, 2004, 2000, 1996]
parti = ["Dem", "Rep", "Dem", "Dem", "Rep", "Rep", "Dem"]

# Nous créons un DataFrame à partir de zéro
my_data = pd.DataFrame(
    {
        "participation": participation,
        "année": annee,
        "parti": parti,
    }
)

# %%
# Quel est le type de `my_data`


# %%
# Regardez le nouveau jeu de données que vous venez de créer
my_data


# %%
# Nous pouvons également en apprendre plus sur notre objet en utilisant la méthode `.info()`.
my_data.info()


# %%
# Lorsque votre jeu de données est trop long, vous pourriez vouloir afficher les premières
# observations (lignes) en utilisant la méthode `.head()`.
my_data.head()


# %% [markdown]
# ### Hack Time

# %%
# Regardez le début des données anes_data


# %%
# Regardez les info des données anes_data


# %% [markdown]
# ## Exploration de données - Variables
#
# Maintenant que vous avez vos données, l'étape suivante est de vous familiariser avec elles. 
#
# La plupart du temps, vous vous intéressez à certains concepts spécifiques. 
# - Vous avez besoin d'un moyen de sélectionner uniquement les variables liées à vos concepts.
#

# %% [markdown]
# ### Sélectionner des variables (colonnes)
#
# Supposons que vous souhaitiez explorer les intentions de participation électorale des citoyens américains (`V241042`).
#
# - Nous pouvons utiliser des crochets sur un objet DataFrame pour sélectionner une seule colonne !
# - Nous pouvons également utiliser une liste de chaînes contenant les noms de colonnes pour sélectionner plusieurs colonnes !
#
# ![](https://pandas.pydata.org/docs/_images/03_subset_columns.svg)
#

# %%
# L'attribut `columns` permet d'obtenir les noms des colonnes d'un DataFrame
anes_data.columns

# %%
# Sélectionner la variable d'intention de vote
anes_data["V241042"]

# %%
# Nous pouvons également la sauvegarder dans un nouvel objet et vérifier son type
vote_int = anes_data["V241042"]
type(vote_int)


# %% [markdown]
# Supposons que vous souhaitiez également savoir pour qui les gens ont l'intention de voter en fonction de leur âge et de leur idéologie ? Dans ce cas, vous pourriez avoir besoin de sélectionner plusieurs variables.

# %%
# Sélectionner plusieurs colonnes
my_vars = [
    "V241042",  # a l'intention de voter ou non
    "V241043",  # pour qui a l'intention de voter
    "V241458x",  # age
    "V241177",  # autoplacement sur une échelle libéral-conservateur
]

anes_data[my_vars]

# %%
# Sauvegarder ce sous-ensemble plus petit de variables dans my_df
my_df = anes_data[my_vars]
print(type(my_df))
print(my_df.columns)
my_df.head()

# %% [markdown]
# Pour éviter d'avoir toujours à vérifier le codebook, nettoyons un peu nos données en rendant les noms des colonnes plus explicites.

# %%
# Renommer les colonnes
my_df.columns = ["vote", "vote_int", "age", "ideologie"]
my_df.head()

# %% [markdown]
# ### Méthodes utiles
# Les Series et les DataFrames fournissent des méthodes très utiles pour explorer facilement les données. Voici quelques-unes des plus courantes :
#
# - `mean()` : moyenne
# - `median()` : médiane
# - `std()` : écart-type
# - `min()` : minimum
# - `max()` : maximum
# - `mode()` : mode (valeur la plus fréquente)
# - `count()` : nombre d'observations
# - `describe()` : statistiques descriptives
# - `value_counts()` : fréquence des valeurs (tri à plat)
#
# Rappel de celles vues plus haut :
# - `info()` : informations sur le DataFrame (types, valeurs manquantes)
# - `head()` : premières lignes
# - `tail()` : dernières lignes
#
#
#

# %%
# Combien de personnes ont l'intention d'aller voter ?
my_df["vote"].value_counts()


# %%
# Quel pourcentage des gens pensent aller voter ?
my_df["vote"].value_counts(normalize=True)


# %%
# Un peu plus propre
my_results = my_df["vote"].value_counts(normalize=True) * 100
my_results.round(1)


# %% [markdown]
# ### Hack Time

# %%
# Quel est l'age moyen des répondants ?


# %%
# Quelle est l'idéologie moyenne des répondants ?

# %%
# Quelle est la proportion de personnes ayant
# l'intention de voter pour kamala harris ?


# %% [markdown]
# ## Visualisation de données
#
# Une fois que vous avez trouvé les informations dont vous avez besoin, il est généralement judicieux de représenter graphiquement vos résultats. En effet, une visualisation vous aidera parfois à mieux comprendre les problèmes liés à vos données !
#
# La plupart du temps, vous utiliserez des graphiques en barres et des histogrammes pour visualiser une seule variable, selon son type.
#
# ### Types de données
#
# Nous avons vu qu'il existe différents types de données en Python (chaînes de caractères, entiers, décimaux, booléens, ...). Lorsqu'on fait de la recherche, nous pouvons regrouper les données en grandes familles : les données numériques/quantitatives et catégorielles/qualitatives
#
# Les **données numériques** ("quantitatives") : caractéristiques quantifiables, des nombres qui mesurent des quantités. On peut distinguer 2 sous catégories :
# - Numériques **continues**, qui peuvent prendre un nombre infini de valeurs.
#   - La taille d'un étudiant (par ex. 182.5 cm)
#   - Pour ces variables, vous utiliserez généralement des **histogrammes**.
# - Numériques **discrètes**, qui ne peuvent prendre qu'un nombre fini de valeurs.
#   - Le nombre d'étudiants dans une classe (par ex. 22)
#   - Pour ces variables, vous utiliserez des **histogrammes** ou des **diagrammes en barres**.
#
# Les données **catégorielles** ("qualitatives") : caractéristiques qui ne sont pas mesurables numériquement. On peut distinguer 2 sous catégories :
# - Catégorielles **nominales** : les valeurs sont des modalités, des catégories sans hiérarchie 
#   - Le genre d'un étudiant, sa couleur de cheveux, sa discipline (par ex. Sociologie)
# - Catégorielles **ordinales** : on peut ordonner les catégories.
#    - (par ex. Jamais/parfois/souvent/toujours)
# - Pour ces variables, vous utiliserez des **diagrammes en barres**.
#
#
# >C'est plus compliqué que ça :
# >- zones grises entre les types de variables.
# >- plein de sortes de graphiques possibles, des "règles" et plein d'exceptions, etc.  
# >
# >**TIP :** Pour vous aider à choisir le type adapté de visualisation, regardez par là :  [**Data to Viz**]( https://www.data-to-viz.com/)
#
# **N'oubliez pas de synthétiser/regrouper/résumer vos données avant de les tracer !**
#
# - Sinon votre ordinateur ne sera pas content...
#
# ### Visualisations avec Pandas
#
# Vous pouvez utiliser pandas pour tracer vos résultats en utilisant la méthode `.plot()` sur un objet DataFrame ou Series.
#
# Pour plus d'informations, cliquez [**ici**](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html).
#

# %%
# Traçons la distribution de la variable age.
my_df["age"].plot(kind="hist")


# %%
# Approfondir
my_df["age"].plot(kind="hist", bins=40)


# %%
# Regardons l'intention de participation

# on avait déjà fait un objet results plus haut :
# cf : my_results = my_df["vote"].value_counts(normalize=True) * 100

my_results.plot(kind="bar")


# %% [markdown]
# ### Hack Time

# %%
# Est-ce que les citoyens américains sont polarisés ?


# %%
# Qui aurait gagné le vote populaire selon l'ANES 2024 ?


# %% [markdown]
# ### Aller plus loin
#
# Il existe de nombreuses options pour jouer avec et améliorer une figure. 
# Lorsque vous cherchez de l'aide pour changer quelque chose sur une figure, si vous avez la bonne terminologie, il est assez facile de trouver de l'aide !
#
# #### Anatomie d'une figure
# ![Anatomie d'une figure](https://matplotlib.org/3.1.1/_images/anatomy.png)
#
# #### Exemple d'amélioration de figure
# Essayons d'améliorer un peu notre graphique des intentions de vote en filtrant les observations et en renommant les modalités.
# (On découvrira tout cela ensemble lors des prochaines séances)
#

# %%
# Filtrer les observations (pour la prochaine fois)
mask = my_df["vote_int"].between(1, 6)

# synthétiser les données
tmp_data = (
    my_df.loc[mask, "vote_int"]
    .replace(
        {1: "Harris", 2: "Trump", 3: "Kennedy", 4: "West", 5: "Stein", 6: "Other"}
    )  # modif si garde
    .value_counts(normalize=True)
)

# Créer un graphique/figure/plot
tmp_data.plot(
    kind="bar",
    title="Intention de vote",
    ylabel="Pourcentage",
    rot=0,
);


# %%
# Y a t-il un lien entre l'age et l'idéologie ?
mask = my_df["ideologie"].between(1, 7)
my_df[mask].plot(kind="box", column="age", by="ideologie")
