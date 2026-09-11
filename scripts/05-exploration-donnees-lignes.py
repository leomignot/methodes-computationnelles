# %% [markdown]
# # Filtrer des données et explorer les relations
#
# **Objectif d'apprentissage :**
# - Apprendre à filtrer des observations
# - Apprendre à comparer des relations
# - Apprendre à synthétiser des relations

# %% [markdown]
# ## Filtrer les observations (lignes)
#
# Généralement, les données c'est "messy", sale/désordonné. La plupart du temps, vous avez besoin de filtrer certaines observations (lignes) dans votre jeu de données.
# - Vous vous intéressez à certains aspects particuliers de votre jeu de données (ex : les jeunes électeurs).
# - L'information est non pertinente et vous devez supprimer certaines données pour éviter de tirer de mauvaises conclusions (ex : les personnes qui refusent de répondre).
#
# Vous avez donc besoin d'un moyen de filtrer les observations dans votre jeu de données.
#
# - Les opérateurs relationnels permettent de sélectionner des observations.
# - Il existe aussi des méthodes utiles pour vous aider dans cette tâche.
#
# ![](https://pandas.pydata.org/docs/_images/03_subset_rows.svg)
#
# Nous avons vu que les données de l'ANES contiennent des valeurs comme -8, -9, 99, qui peuvent ou non être utiles selon le problème que l'on souhaite traiter.
#
# Comment peut-on les gérer ?
#
# Commençons par cette question pour illustrer :
# - Les jeunes électeurs sont-ils plus libéraux ou conservateurs ?
#

# %%
# Charger pandas
import pandas as pd

# Charger des données avec pandas depuis une URL
data_url = "https://raw.githubusercontent.com/datamisc/ts-2024/main/data.csv"
anes_data = pd.read_csv(data_url, compression="gzip", low_memory=False)


# %%
# Sélectionner un sous ensemble de  variables et renommer
my_vars = [
    "V241042",  # a l'intention de voter ou non
    "V241043",  # pour qui a l'intention de voter
    "V241458x",  # age
    "V241177",  # autoplacement sur une échelle libéral-conservateur
    "V241157",  # feeling thermometer Trump
]

df = anes_data[my_vars]
df.columns = ["vote", "vote_int", "age", "ideologie", "trump_thermometer"]

df.head()

# %%
# Quelle est la distribution par idéologie ?
df.value_counts("ideologie").sort_index().plot(kind="bar")

# nb : .sort_index() permet de trier les barres par ordre alphanumérique de l'index
# (ici, les valeurs de la variable idéologie)
# plutôt que par effectifs

# nb2 : df.value_counts("ideologie") est ici équivalent
# à df["ideologie"].value_counts()
# que l'on avait vu précédemment

# %%
# Quelle est la distribution par âge ?
df["age"].plot(kind="hist", bins=30)


# %% [markdown]
# On a besoin de faire un peu de nettoyage dans ces variables !

# %%
# nettoyer la variable âge
mask_age = df["age"] >= 18
mask_age


# %%
# L'âge a l'air ok désormais, mais on a perdu des observations !
df[mask_age].describe()


# %%
# Sauvegarder le dataframe avec les données filtrées
df = df[mask_age]

# %%
# Nettoyons la variable idéologie
mask_ideo = (df["ideologie"] >= 1) & (df["ideologie"] <= 7)
mask_ideo

# %%
df = df[mask_ideo]
df.describe()

# %%
# Comment est distribué l'âge désormais ?
df["age"].plot(kind="hist", bins=30)


# %%
# Comment est distribuée l'idéologie maintenant ?
df.value_counts("ideologie").sort_index().plot(kind="bar")

# %% [markdown]
# ### Hack-Time
#

# %%
# Nettoyer la variable `vote`


# %%
# Nettoyer la variable `vote_int`


# %% [markdown]
# ### Explorons les jeunes électeur.ices

# %%
# Definir les jeunes électeurs
mask = df["age"] <= 80


# %%
# Quel groupe est plus libéral ? Quel groupe est plus conservateur ?
print(df[mask]["ideologie"].mean())
print(df[~mask]["ideologie"].mean())


# %% [markdown]
# ### Hack-Time
#

# %%
# Que pouvons-nous observer d'autre par rapport aux jeunes?


# %% [markdown]
# Pourrait-on visualiser ces relations d'une autre manière ?
#

# %% [markdown]
# ## Types de données & et mesures
#
# Rappel sur les types de variables :
#
# | **Type**                | **Sous-type**      | **Exemples**                                 | **Type Altair**   |
# |-------------------------|-------------------------|-----------------------------------------------|-------------------|
# | Numérique (quantitative)| Continue                | Niveau de revenus (1825€)               | quantitative (Q)  |
# | Numérique (quantitative)| Discrète                | Nombre d'enfants       | quantitative (Q) / ordinal (O)  |
# | Catégorielle (qualitative) | Ordinale             | Jamais/parfois/souvent/toujours              | ordinal (O)       |
# | Catégorielle (qualitative) | Nominale             | Genre, couleur de cheveux, discipline         | nominal (N)       |
#
# *NB : il existe en réalité des zones grises*
# *NB : et il existe d'autres types dans Altair (temporal (T) : valeur de temps ou date, geojson (G) : forme géographique)*

# %% [markdown]
# ### Continue & Continue
#
#

# %% [markdown]
# #### Scatter plot (nuages de points)

# %%
# Quelle est la relation entre age et le sentiment envers D. Trump ?

# filtrons les valeurs pour le thermomètre :
# on peut le faire sans masque en définissant directement le filtre dans les crochets
df = df[df["trump_thermometer"] >= 0]

# Et tentons de faire un nuage de points (scatter plot en anglais)
df.plot(kind="scatter", x="age", y="trump_thermometer", figsize=(10, 10))


# %% [markdown]
# ### Hack-Time
#

# %%
# On peut tenter d'améliorer le graphique
# en échantillonnant pour l'alléger
# ou en jouant sur la transparence des points

# Tentez de jouer sur les options sample() et alpha ci-dessous
# N'executez qu'une seule des deux lignes à la fois
# (vous pouvez commenter/décommenter les lignes)

# df.sample(200).plot(kind="scatter", x="age", y="trump_thermometer", figsize=(10, 10))
# df.plot(kind="scatter", x="age", y="trump_thermometer", alpha=0.02, figsize=(10, 10))


# %% [markdown]
# ### Discrète & Continue | Catégorielle & Continue
#

# %% [markdown]
# #### Groupby et statistiques agrégées

# %% [markdown]
# La **fonction `groupby`** de pandas permet de regrouper les données selon les valeurs d'une ou plusieurs colonnes, puis d'appliquer des opérations statistiques (comme la moyenne, la médiane, l'écart-type, etc.) sur chaque groupe.
#
# Cela facilite la comparaison entre différentes catégories ou groupes d'observations.
#
# La syntaxe suit ce format :
# ```python
# df.groupby("colonne_à_grouper")[["autre_colonne"]].operation() # .mean(), .std(), etc.
# ```

# %%
# regroupons par idéologie et calculons des statistiques sur l'age
df.groupby("ideologie")["age"].mean()  # ou median(), ou std()

# %% [markdown]
# ### Hack-Time
#

# %%
# Calculez l'age médian par groupe d'idéologie


# %%
# Calculez l'écart type (std) d'age par groupe d'idéologie


# %% [markdown]
# On sait donc calculer une mediane par groupe, des quartiles, un écart type, etc.
#
# Quelle visualisation marche bien pour ces informations ?
#
# Team "boite à moustache"/boxplot !!

# %% [markdown]
# #### Boxplots / boite à moustache
#
# <!-- passage par html pour la taille de l'image -->
# <img src="https://miro.medium.com/max/1400/1*2c21SkzJMf3frPXPAR_gZA.png" width="900"/>

# %%
# Pour une boxplot sur une seule variable
df["age"].plot(kind="box")

# %%
# Mais on peut aussi croiser les variables

# Ex : Y a t-il une relation entre age et ideologie ?
df.plot(kind="box", column="age", by="ideologie")


# %% [markdown]
# ### Discrète & Discrète | catégorielle & catégorielle
#
# #### Tableaux croisés
#
# On peut utiliser la fonction `pd.crosstab()` pour réaliser des tableaux croisés entre deux variables (ou plus) 
#
# ![](https://raw.githubusercontent.com/SciencesPoBordeaux/data-viz/refs/heads/main/figures/pd.crosstab.png)
#
# Pour de l'aide sur une fonction, vous pouvez faire appel à :
# ```python
# help(pd.crosstab)
# # ou
# pd.crosstab?
# ```

# %%
# APPELEZ À L'AIDE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# %%
# Exemple de tableau croisé :
pd.crosstab(df["ideologie"], df["vote_int"])

# %%
# Revient à ...
df.groupby("ideologie")["vote_int"].value_counts().unstack().fillna(0).astype(int)


# %%
# Les valeurs absolues ne sont pas très parlantes
# pourcentage du total :
pd.crosstab(df["ideologie"], df["vote_int"], normalize=True)


# %%
# Les barplots à la rescousse !
pd.crosstab(df["ideologie"], df["vote_int"], normalize=True).plot(
    kind="bar",
    # On peut jouer sur les options pour améliorer le rendu :
    # stacked=True,
    # width=2
    # figsize=(10, 5)
    # subplots=True, sharey=True
)


# %%
# Exemple d'un tableau croisé pourcentages en ligne
tab = pd.crosstab(df["ideologie"], df["vote_int"], normalize="index", margins=True)
tab.round(2)

# %%
tab.plot(kind="bar", stacked=True, legend=False)
