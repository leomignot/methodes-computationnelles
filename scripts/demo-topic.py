# %%
# Installer bertopic
# %pip install bertopic

# %%
import os
os.environ["NUMBA_THREADING_LAYER"] = "workqueue" # fix for kernel crash with UV

# importer les bibliothèques nécessaires
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# préciser l'url et charger les données
url = "https://raw.githubusercontent.com/cristobalmitchell/pokedex/refs/heads/main/data/pokemon_utf8.csv"
df = pd.read_csv(url)

# passer les descriptions comme docs
docs = df['description'].tolist()

# créer le modèle de topic modeling et l'appliquer (avec gestion stopwords)
vectorizer_model = CountVectorizer(stop_words="english")
topic_model = BERTopic(vectorizer_model=vectorizer_model)
topics, probs = topic_model.fit_transform(docs)

# Visualiser
topic_model.visualize_documents(docs)
