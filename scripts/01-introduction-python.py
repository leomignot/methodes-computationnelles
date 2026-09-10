# %% [markdown]
# # Introduction à Python pour les Sciences Sociales
#
# **CONSEIL :** Commencez par enregistrer une copie de ce notebook dans votre Google Drive (`Fichier` > `Enregistrer une copie dans Drive`) pour pouvoir prendre vos propres notes !
#
# **Objectifs d'apprentissage** 
# - Apprendre à afficher des résultats (outputs).
# - Exécuter des cellules de code.
# - Documenter son code et analyse avec des commentaires.
# - Réaliser des opérations mathématiques de base.
# - Créer et manipuler des objets (variables).

# %% [markdown]
# ## Pourquoi Python pour les sciences sociales ?
#
# - **Gratuit et Open-source** : Contrairement à Stata ou SPSS.
# - **Polyvalent** : De la collecte à la modélisation de pointe, en passant par l'analyse et la visualisation.
# - **Écosystème immense** : Plus de **700 000 packages** disponibles ! C'est comme un smartphone avec une infinité d'applications spécialisées (statistiques, cartographie, analyse textuelle).
# - **Ressources** : De nombreuses ressources gratuites disponibles en ligne !
# - **Reproductibilité** : Votre code est une trace rigoureuse de votre analyse, indispensable pour tout projet rigoureux.
# - **Compétence recherchée** : Maîtriser Python et les données permet de produire des analyses concrètes et utiles dans la recherche, le conseil, le journalisme, l’action publique, les associations et plus largement dans tout métier faisant appel à l’information et aux données.
# - **Communauté accueillante**

# %% [markdown]
# ## Imprimer sans imprimante...
#
# Un notebook fonctionne par "cellules". Vous pouvez utiliser les notebooks pour lancer/exécuter le code à l'intérieur des cellules de code. 
#
# La première fois que vous exécutez une cellule de code, cela prendra environ 15 secondes avant de voir votre résultat. C'est parce que votre navigateur démarre un ordinateur sur un serveur distant pour exécuter votre code. Pas mal d'avoir un ordinateur qui tourne gratuitement en moins de 15 secondes ! Après cela, votre code s'exécute instantanément.
#
# Pour exécuter le code dans une cellule, commencez par sélectionner la cellule que vous souhaitez lancer. Un bouton "lecture" (play) apparaîtra et vous avez deux options :
#
# - soit vous appuyez sur le bouton "play" à gauche de la cellule.
# - soit vous appuyez sur MAJ+ENTRÉE (SHIFT+ENTER).
#
# Les deux commandes lanceront et exécuteront le code de la cellule. 
#
# Essayons ça !

# %%
# La fonction print() permet d'afficher un résultat
print("Bienvenue au cours de Data Viz à Sciences Po Bordeaux!")

# %% [markdown]
# Remarquez qu'après l'exécution, le résultat apparaît sous la cellule de code.
#
# En programmation, vous avez généralement une fonction pour afficher un résultat (*ouput*). 
#
# Pour afficher du texte (appelé **chaîne de caractères** ou *string*), vous devez impérativement l'entourer de guillemets **"**.
#
# En python, nous utilisons la fonction `print()` pour afficher un résultat.

# %% [markdown]
# ### Hack Time
#
# Dans la cellule de code ci-dessous :
# - Affichez "Bonjour!" 
# - Affichez votre prénom et votre nom.
# - Affichez le message "Analyse de l'ANES 2024".

# %%
# Votre code va dans cette cellule.


# %% [markdown]
# ## Exécution du code & Commentaires
#
# Lorsque vous lancez le code ci-dessous, que voyez-vous ?

# %%
print(" _____")
# Ceci est un commentaire qui sera ignoré quand vous lancerez cette ligne.
print("|     |")
# En voici un autre. Ils sont toujours ignorés.
print("|     |")
# Et en voici un autre. Vous pouvez les utiliser pour documenter le code.
print("|_____|")


# %% [markdown]
# Le code est exécuté de manière séquentielle. C'est similaire à une recette de cuisine. Vous appliquez un ensemble d'instructions dans l'ordre pour obtenir un résultat souhaité.
#
# **Rappel :**
# - Quand vous êtes dans une cellule de texte, vous utilisez la syntaxe markdown. 
# - Quand vous êtes dans une cellule de code, vous utilisez la syntaxe python.
#
# Remarquez qu'un symbole dièse (**#**) est utilisé dans les cellules de texte pour définir des titres, mais à l'intérieur des cellules de code python, il est utilisé pour faire des commentaires !
#
# **CONSEIL :** Quand vous écrivez du code, il est recommandé de le documenter pour aider ceux qui lisent votre code (d’autres personnes ou vous-même!) à comprendre ce que fait le code.
#

# %% [markdown]
# ### Hack Time
#
# Lancez le code ci-dessous, regardez ce qu'il fait, et commentez le code !

# %%
print("Faisons un peu de maths !")

print(5 + 7)


# %% [markdown]
# ## Opérateurs arithmétiques
#
# Dans sa forme la plus basique, Python peut être utilisé comme une simple calculatrice pour effectuer des opérations mathématiques.
#
# Voyons les principaux opérateurs arithmétiques :
#
# | Description | Opérateur |
# |:-           | :-:      |
# | Somme       | **+** |
# | Différence  | **-** |
# | Produit     | **\*** |
# | Quotient    | **/** |
# | Puissance   | **\*\*** |
# | Modulo      | **%** |
#

# %% [markdown]
# ### Hack Time 

# %%
# Divisez 7 par 3.

# Élevez 2 à la puissance 5.

# Faites une autre opération mathématique.

# Décrivez ce que vous avez fait en utilisant un commentaire.


# %% [markdown]
# ## Opérateur d'assignation - (création d'objets/variables)
#
# Les objets sont des conteneurs qui vous permettent de stocker des informations comme une valeur, une phrase, ou une autre portion de code comme une fonction (nous y reviendrons plus tard). Pour définir ces objets, vous devez utiliser l'opérateur d'assignation.
#
# | Description | Opérateur |
# |:-           | :-:      |
# | Assigner    | **=** |
#
# L'opérateur d'assignation est le symbole égal **"="** en python.

# %%
participation_1 = 55.7
participation_1


# %% [markdown]
# Remarquez que dans ce cas, nous n'avons pas utilisé la fonction `print()` à la ligne 2 et pourtant le notebook a renvoyé une valeur. Les notebooks renvoient toujours la dernière instruction.
#
# Créons quelques objets supplémentaires avec des informations pertinentes.

# %%
election = "United States presidential election"
annee_1 = 2016
vainqueur_1 = "Parti républicain"

annee_2 = 2020
participation_2 = 66.8
vainqueur_2 = "Parti démocrate"


# %% [markdown]
# Le code n'a pas besoin de toujours renvoyer quelque chose. Parfois, vous créez et sauvegardez simplement des éléments en mémoire pour une utilisation ultérieure.

# %% [markdown]
# **NB :** Quand vous devez assigner des chaînes de caractères (`string`) à un objet, vous devez entourer votre texte de guillemets. Vous pouvez utiliser des guillemets simples `'` ou doubles `""`. C'est une bonne pratique de toujours utiliser des guillemets doubles. Il existe aussi des triples guillemets `""" votre texte """`

# %%
print(election, annee_1)
print(vainqueur_1, participation_1)


# %% [markdown]
# Avant de lancer la cellule de code suivante, essayez de deviner ce qui va se passer :
#

# %%
print(Vainqueur_2)

# %% [markdown]
# Pouvez-vous corriger l'erreur et faire fonctionner le code correctement ?
#

# %% [markdown]
# ### Majuscules/minuscules !
# Python est sensible aux majuscules/minuscules (sensibilité à la *casse*). 
# `Vainqueur_2` et `vainqueur_2` sont deux objets différents.
#
# **Exercice :** Essayez d'exécuter la cellule suivante et corrigez l'erreur.

# %%
candidat_favori = "Kamala Harris"
print(Candidat_favori)

# %% [markdown]
# ### D'autres exemples
# Vous pouvez combiner les assignations avec l'arithmétique. Par exemple :

# %%
somme = 3 + 14
somme

# %%
difference = 10 - 3
difference

# %%
produit = 42 * 2.41
produit

# %% [markdown]
# Mais vous pouvez aussi utiliser l'arithmétique simple pour commencer à répondre à des questions intéressantes !
#

# %% [markdown]
# De combien de points de pourcentage la participation a-t-elle augmenté/diminué lors de la dernière élection américaine ?

# %%
ecart_participation = participation_2 - participation_1

# %% [markdown]
# Quel est le pourcentage de changement de la participation depuis la dernière élection ?

# %%
changement_pct = participation_2 / participation_1

# %% [markdown]
# Quelle est la participation moyenne lors des 2 dernières élections ?

# %%
moyenne_part = (participation_1 + participation_2) / 2

# %% [markdown]
# ### Hack Time
#
# Ajoutons les données pour l'élection présidentielle américaine de 2012.

# %%
# Créez 3 nouveaux objets avec les informations pour l'élection américaine de 2012.
annee_3 = 
participation_3 = 
vainqueur_3 = 


# %%
# De combien de points de pourcentage la participation a-t-elle
# augmenté/diminué en 2016 par rapport à 2012 ?


# %%
# Quelle est la participation moyenne sur
# les 3 dernières élections ?


# %% [markdown]
# ### Attention aux noms d'objets
# - Les noms d'objets doivent commencer par une lettre.
# - Les noms d'objets peuvent contenir uniquement des lettres, des chiffres et des tirets bas (underscores `_`).
#
# ### Bonnes pratiques pour nommer/créer vos objets
# - Utilisez des noms d'objets descriptifs.
# - Utilisez uniquement des minuscules et des tirets bas (`_`) : c'est aussi appelé le **snake_case** (ex: `resultat_vote_2024`).
# - Soyez descriptifs : préférez `age_moyen_votants` à `amv`.
# - N'utilisez pas d'accents afin de prévenir les bugs d'encodage.
#
