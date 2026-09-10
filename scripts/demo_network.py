# %% [markdown]
# # Démo réseau
#

# %%
# # si besoin installer les dépendances nécessaires via pip
# %pip install networkx pandas ipywidgets ipysigma

# %%
import networkx as nx
import pandas as pd
from ipysigma import Sigma

# %%
url = "https://raw.githubusercontent.com/cristobalmitchell/pokedex/refs/heads/main/data/pokemon_utf8.csv"
df = pd.read_csv(url)
df.head()

# %% [markdown]
# ## Créer le réseau

# %%
# Should work

G = nx.Graph()

for _, row in df.dropna(subset=["primary_type", "secondary_type"]).iterrows():
    t1, t2 = sorted([row["primary_type"], row["secondary_type"]])
    # G.add_node(t1) # add_edge() ajoute automatiquement les nœuds
    # G.add_node(t2) # add_edge() ajoute automatiquement les nœuds

    if G.has_edge(t1, t2):
        G[t1][t2]["weight"] += 1
    else:
        G.add_edge(t1, t2, weight=1)

G.number_of_nodes(), G.number_of_edges()

# %% [markdown]
# ## Visualisation interactive avec ipysigma
#

# %%
# # Si vous travaillez dans Google Colab :
# from google.colab import output
# output.enable_custom_widget_manager()

# %%
viz = Sigma(
    G,
    node_size=G.degree,
    edge_size="weight",
    node_metrics=["louvain"],
    node_color="louvain",
    node_size_range=(3, 20),
    default_edge_type="curve",
    node_border_color_from="node",
    node_label_size=G.degree,
    show_all_labels=True,
    # Des options si on veut fignoler :
    # ex pour la detection de communauté plus fine :
    # node_metrics={"community": {"name": "louvain", "resolution": 1.2}},
    # node_color="community",
    # edge_color= # mettre une couleur en fonction d'une métrique
    # label_rendered_size_threshold=10,  # ou jouer sur l'affichage labels
    # default_node_label_size=14, # mettre une taille par défaut
)

viz
