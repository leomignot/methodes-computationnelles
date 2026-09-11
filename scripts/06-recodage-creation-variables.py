# %% [markdown]
# # Gestion des données
# ## Recodage et création de variables
#
# **Objectif pédagogique :** 
# - Apprendre à recoder et à créer des variables
# - Découvrir les fonctions `.replace()` et `pd.cut()`
# - Apprendre à comparer des variables

# %%
# Charger pandas
import pandas as pd

# Charger des données avec pandas depuis une URL
data_url = "https://raw.githubusercontent.com/datamisc/ts-2024/main/data.csv"
anes_data = pd.read_csv(data_url, compression="gzip")


# %%
# Sélectionner un sous ensemble de variables et renommer
my_vars = [
    "V241042",  # pense aller voter ou non
    "V241043",  # pour qui a l'intention de voter
    "V241458x",  # age
    "V241177",  # autoplacement sur une échelle libéral-conservateur
    "V241156",  # Harris thermometer
    "V241157",  # Trump thermometer
    "V242425",  # Gestion covid par présidence
    "V241229",  # confiance gouvernement
    "V241233",  # corruption gouvernement
    "V241234",  # confiance aux gens
]

df = anes_data[my_vars]

df.columns = [
    "vote",
    "vote_int",
    "age",
    "ideologie",
    "harris_thrm",
    "trump_thrm",
    "covid",
    "conf_gouv",
    "conf_corrupt",
    "conf_gens",
]

df.head()


# %% [markdown]
# ## Recodage des variables 
#
# ### La méthode `.replace()`
#
# On peut utiliser la méthode/fonction `replace` pour faciliter le recodage des variables.
#
# Essayons par exemple de recoder la variable relative à l'intention de vote :
#
#     V241043 – PRE: FOR WHOM DOES R INTEND TO VOTE FOR PRESIDENT
#         -9. Refused
#         -8. Don’t know
#         -1. Inapplicable
#         1. Kamala Harris
#         2. Donald Trump
#         3. Robert F. Kennedy, Jr.
#         4. Cornel West
#         5. Jill Stein
#         6. Another candidate {SPECIFY}
#
#

# %%
# Commençons par filtrer les observations (lignes) qui nous intéressent
mask = (df["vote_int"] > 0) & (df["vote_int"] <= 6)
# Creation d'un nouveau dataframe
new_df = df[mask]

# %%
# On jette un oeil
new_df.describe()

# %% [markdown]
# ## Recodage des valeurs 

# %%
# On essaie de recoder la valeur 1 en "K.Harris" pour les lignes qui respectent la condition
new_df["vote_int"].replace(1, "K.Harris")


# %%
# Lorsqu'on a validé que c'est correct on assigne le tout à la variable initale.
new_df["vote_int"] = new_df["vote_int"].replace(1, "K.Harris")

# %%
# Même chose pour la valeur == 2 qui correspond à Trump
new_df["vote_int"].replace(2, "D.Trump")


# %%
new_df["vote_int"] = new_df["vote_int"].replace(2, "D.Trump")


# %%
new_df["vote_int"].value_counts()


# %% [markdown]
# ### Hack-Time
#
#

# %%
# Terminez de recoder la variable `vote_int`


# %% [markdown]
# Recoder chaque catégorie une par une est **TRÈS** fastidieux ! Mais il y a des solutions.
#
# Recodons cette fois-ci la variable `covid` à l'aide de la méthode `.replace()` et de listes ou d'un dictionnaire !
#
# ```
# V242425 - POST: CSES6-Q08B: PRESIDENT PERFORMANCE COVID
# -9. Refused
# -8. Don’t know
# -7. Insuﬃcient partial, interview deleted
# -6. No post interview
# -5. Suﬃcient partial, breakoﬀ
# -1. Inapplicable
# 1. Very good job
# 2. Good job
# 3. Bad job
# 4. Very bad job
# ```

# %%
# À quoi ressemble la variable `covid` ?
new_df["covid"].value_counts()

# %%
# Commençons par garder les observations (lignes) qui nous intéressent
mask = new_df["covid"] > 0
new_df = new_df[mask]

# %%
# Créer deux listes avec les anciennes et les nouvelles modalités
# ATTENTION, l'ordre des éléments des listes est important!!
old_labels = [1, 2, 3, 4]
new_labels = ["1. Very good job", "2. Good job", "3. Bad job", "4. Very bad job"]


# %%
# Passer à la fonction replace les anciennes et les nouvelles valeurs
new_df["covid"].replace(old_labels, new_labels)


# %%
# Ça à l'air mieux !
new_df["covid"].replace(old_labels, new_labels).value_counts()

# %% [markdown]
# > **Aparté : dictionnaires**
# > Les [dictionnaires](https://docs.python.org/fr/3.7/tutorial/datastructures.html?highlight=dictionnaire) sont "des ensembles de paires clé-valeur, les clés devant être uniques (au sein d'un dictionnaire)". Ils sont définis entre des accolades :
# >
# > ```python
# >dict = {"clé": "valeur", "autre_clé": "autre_valeur"}
# >```
# >
# > Contrairement aux listes dont les éléments sont accessibles par leur position (index), les éléments d'un dictionnaire sont accessibles par leur clé.

# %%
# Exemple
ma_liste = ["LFI", "Verts", "LREM"]
print(ma_liste[1])

mon_dict = {"a": "LFI", "b": "Verts", "c": "LREM"}
print(mon_dict["b"])

# %%
# Je peux donc aussi utiliser un dictionnaire pour faire le recodage
recode_dict = {
    1: "1. Very good job",
    2: "2. Good job",
    3: "3. Bad job",
    4: "4. Very bad job",
}

# Et voir ce que ça donne :
new_df["covid"].replace(recode_dict).value_counts()


# %% [markdown]
# ### Hack-Time

# %%
# Choisissez une des deux méthodes (listes ou dictionnaire) pour recoder la variable covid
# et assignez le résultat à la variable initiale


# %%
# Visualisons le résultat
new_df["covid"].value_counts(normalize=True).sort_index().plot(kind="bar")

# %% [markdown]
# ### Hack-Time

# %%
# Est-ce que les citoyens qui approuvent les mesures prises
# par le gouvernement pour gérer le COVID sont
# plutôt libéraux ou conservateurs ?
# CONSEIL : utilisez pd.crosstab !


# %% [markdown]
# ## Filtrer ou recoder ?
#
# Jusqu'à présent, nous avons généralement filtré les observations dont nous n'avions pas besoin sans réfléchir aux conséquences que cela pouvait avoir sur nos résultats. 
#
# Or, si on applique plusieurs filtres, on ajoute des biais à notre ensemble de données, et on risque également de perdre une grande partie des données ! 
# - **Avec moins de données, nous avons moins d'éléments pour tirer des conclusions !**
#
# Essayons de prédire le résultat des élections à l'aide des données préélectorales !
#

# %%
# On jette un coup d'oeil à la variable
df["vote_int"].value_counts()


# %%
# Filtrer toutes les observations qui ne sont pas Harris ou Trump
mask = df["vote_int"].between(1, 2)
filter_df = df[mask]

# Dictionnaire les modalités
vote_int_labels = {
    1: "K.Harris",
    2: "D.Trump",
}

filtered_output = (
    filter_df["vote_int"].replace(vote_int_labels).value_counts(normalize=True)
)
filtered_output


# %%
# Recoder les observations
recoded_df = df[df["vote_int"] > 0]

# On crée un dictionnaire pour le recodage
vote_int_labels = {
    1: "K.Harris",
    2: "D.Trump",
    3: "Other",
    4: "Other",
    5: "Other",
    6: "Other",
}

# Recoder les labels restants en utilisant le dictionnaire précédemment créé
recoded_df["vote_int"] = recoded_df["vote_int"].replace(vote_int_labels)

recoded_output = recoded_df["vote_int"].value_counts(normalize=True)
recoded_output


# %%
print("La sortie en filtrant")
print(filtered_output)
print("================================")
print("La sortie en recodant")
print(recoded_output)

# %% [markdown]
# ## Créer de nouvelles variables (~ Ajout de nouvelles colonnes)
#
# Lorsque vous recodez des variables, vous pouvez ajouter une nouvelle variable au jeu de données d'origine afin de conserver la version originale de votre variable.
#
# ![](https://pandas.pydata.org/docs/_images/05_newcolumn_1.svg)
#
#
#

# %%
recoded_df

# %%
recoded_df["my_new_var"] = 0
recoded_df

# %%
# On peut également supprimer une colonne à l'aide de la méthode drop.
# Voyons à quoi ressemble le recoded_df si nous supprimons/dropons la variable.
recoded_df.drop("my_new_var", axis=1)

# nb: axis=1 indique que nous voulons supprimer une colonne(=1), et pas une ligne(=0)

# %%
# Une fois satisfaits du résultat, on sauvegarde !
recoded_df = recoded_df.drop("my_new_var", axis=1)

# %% [markdown]
# ## Hack-Time

# %%
# Ajoutez une nouvelle variable binaire qui prend la valeur 1 lorsque
# le répondant a l'intention de voter pour Trump.
# Nommez cette variable « vote_trump ».


# %% [markdown]
# ## Recodage de variable
#
# ### La méthode `.cut()` 
#
# La méthode/fonction `pd.cut()` nous permet de transformer une variable continue en catégories !

# %%
# On passe d'abord les bornes souhaitées,
# puis les labels correspondants

recoded_df["age_cat"] = pd.cut(
    df["age"],  # la variable à recoder
    bins=[17, 35, 50, 65, 80],  # les bornes
    labels=["18-35", "36-50", "51-65", "66+"],  # les labels
)
recoded_df["age_cat"].value_counts()

# nb : il est possible de préciser le comportement souhaité
# dans les paramètres de pd.cut
# de base : right=True / include_lowest=False

# %%
recoded_df["age_cat"].value_counts().sort_index().plot(kind="bar")


# %%
pd.crosstab(recoded_df["vote_int"], recoded_df["age_cat"], normalize=True).plot(
    kind="bar", subplots=True, figsize=(10, 10), layout=(2, 2)
);
# TIP : ce petit `;` qu'on utilise parfois c'est pour nettoyer la sortie

# %% [markdown]
# ### Hack-Time

# %%
# Ajoutez à recoded_df une version nettoyée de la variable covid nommée « clean_covid »
# TIP : repartez de ce que l'on a fait plus haut dans `new_df``.


# %%
# Quelle tranche d'âge approuve le plus la manière dont le gouvernement gère la crise du Covid ?


# %% [markdown]
# ## BONUS - Création d'échelles | indices
#
# En sciences sociales, nous étudions des réalités souvent complexes et non directement observables. Comment mesurer concrètement des notions comme la confiance politique, l'engagement citoyen, la satisfaction démocratique ?
#
# Pour approcher ces concepts latents, nous construisons des instruments de mesure qui reposent sur des indicateurs observables. Parmi ces instruments, l'échelle additive est l'une des plus simples et des plus utilisées.
#
# Une échelle additive est composée de plusieurs questions (items) censées refléter une même dimension. Chaque réponse est codée numériquement, et l'on additionne (ou l'on fait la moyenne de) ces valeurs pour obtenir un score global, qui représente le niveau de la variable étudiée chez la personne interrogée.
#

# %% [markdown]
# ### Créer une échelle de confiance politique

# %%
# On selectionne les trois variables liées à la confiance
trust_scale_vars = ["conf_gouv", "conf_corrupt", "conf_gens"]
df[trust_scale_vars]

# %%
# Recodage des valeurs spécifiques (missing values du questionnaire)
old_labels = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
recoded_df[trust_scale_vars] = df[trust_scale_vars].replace(old_labels, pd.NA)

# %%
# Inversons les échelles pour que les valeurs plus élevées correspondent à plus de confiance
# Il faut vérifier dans le codebook pour comprendre la direction
recoded_df["conf_gouv"] = 6 - recoded_df["conf_gouv"]
recoded_df["conf_gens"] = 6 - recoded_df["conf_gens"]

# Vous avez remarqué que l'on n'a pas inversé la variable `conf_corrupt`/V241233.
# Pourquoi ?


# %%
# Création d'une simple échelle additive en additionnant les trois variables
recoded_df["trust_scale"] = recoded_df[trust_scale_vars].sum(axis=1)


# %%
# Vérifions si tout à l'air ok !
print(recoded_df["trust_scale"].describe())
recoded_df["trust_scale"].value_counts().sort_index().plot(kind="bar")


# %% [markdown]
# ### Hack-Time

# %%
# En utilisant cette échelle de confiance politique, les jeunes font-ils
# preuve de plus ou de moins de confiance que les autres groupes d'âge ?


# %%
# Remarque-t-on autre chose ?
# Notre describe est-il "normal" ?

