# %% [markdown]
# # Demo visualisation

# %%
# # Si besoin d'installer les packages via pip dans un notebook :
# # %pip install pandas plotly

# %% [markdown]
# # Appuyer sur le bouton "Play"

# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Charger et nettoyer les noms de colonnes
url = "https://raw.githubusercontent.com/leomignot/DataSHS_initiation_python/refs/heads/main/data/pokemon_data.csv"
df = pd.read_csv(url)

# Mapping de couleurs par type
type_colors = {
    "Normal": "#A8A878",
    "Fire": "#F08030",
    "Water": "#6890F0",
    "Electric": "#F8D030",
    "Grass": "#78C850",
    "Ice": "#98D8D8",
    "Fighting": "#C03028",
    "Poison": "#A040A0",
    "Ground": "#E0C068",
    "Flying": "#A890F0",
    "Psychic": "#F85888",
    "Bug": "#A8B820",
    "Rock": "#B8A038",
    "Ghost": "#705898",
    "Dragon": "#7038F8",
    "Dark": "#705848",
    "Steel": "#B8B8D0",
    "Fairy": "#EE99AC",
}

# Calculer les moyennes par type
stats_cols = ["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]
type_stats = df.groupby("Type 1")[stats_cols].mean().reset_index()

# Obtenir tous les types uniques
all_types_sorted = sorted(type_stats["Type 1"].unique())
n_types = len(all_types_sorted)

# Calculer la grille : pour 4 colonnes
n_cols = 4
n_rows = (n_types + n_cols - 1) // n_cols  # Dark magic

# Créer les subplots
fig = make_subplots(
    rows=n_rows,
    cols=n_cols,
    specs=[[{"type": "polar"}] * n_cols for _ in range(n_rows)],
    subplot_titles=all_types_sorted,
    vertical_spacing=0.1,  # pour ajuster l'intervalle entre lignes
    # horizontal_spacing=0.03,
)

# "If you’re using plotly.express you can use the line_close=True parameter,
# otherwise you’ll have to manually duplicate the first point at the end of your series."
# https://community.plotly.com/t/closing-line-for-radar-cart-and-popup-window-on-chart-radar/47711/2
theta = [
    "HP",
    "Attack",
    "Defense",
    "Sp. Atk",
    "Sp. Def",
    "Speed",
    "HP",  # Re "HP" Pour fermer le radar
]

for idx, poke_type in enumerate(all_types_sorted):
    # déterminer quel subplot
    row = (idx // n_cols) + 1
    col = (idx % n_cols) + 1

    # Extraire les stats brutes moyennes du type
    row_data = type_stats[type_stats["Type 1"] == poke_type].iloc[0]

    values = [
        row_data["HP"],
        row_data["Attack"],
        row_data["Defense"],
        row_data["Sp. Atk"],
        row_data["Sp. Def"],
        row_data["Speed"],
        row_data["HP"],  # pour fermer le radar
    ]

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=theta,
            fill="toself",
            name=poke_type,
            line_color=type_colors.get(poke_type, "#808080"),
            showlegend=False,
        ),
        row=row,
        col=col,
    )

# Configurer tous les axes
polar_config = {}
for idx in range(n_types):
    polar_key = "polar" if idx == 0 else f"polar{idx + 1}"
    polar_config[polar_key] = dict(
        radialaxis=dict(
            visible=True,
            range=[0, 140],  # fixer à la main comme un ane
            showticklabels=False,
        ),  # moche si on affiche les ticks
        angularaxis=dict(showticklabels=True, tickfont=dict(size=10)),
    )

fig.update_layout(**polar_config)

fig.update_layout(
    title_text="Profil statistique par type (Small Multiples)",
    title_font_size=20,
    height=280 * n_rows,
    template="plotly_white",
    font=dict(size=10),
)

fig.show()
