# %%
# Installer bertopic
# # %pip install bertopic

# %%
import os

os.environ["NUMBA_THREADING_LAYER"] = "workqueue"  # fix for kernel crash with UV

# importer les bibliothèques nécessaires
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer
from stopwordsiso import stopwords

# préciser l'url et charger les données
# url = "https://raw.githubusercontent.com/cristobalmitchell/pokedex/refs/heads/main/data/pokemon_utf8.csv"
url = "hf://datasets/regicid/LRFAF/corpus.csv"
df = pd.read_csv(url)
df = df.sample(1000, random_state=42)  # échantillonner pour accélérer le calcul

# passer les lyrics comme docs
docs = df["lyrics"].tolist()

# VECTORIZER pour gestion stopwords
french_stopwords = list(stopwords("fr"))
vectorizer_model = CountVectorizer(stop_words=french_stopwords)

# créer le modèle de topic modeling et l'appliquer (avec gestion stopwords)
topic_model = BERTopic(vectorizer_model=vectorizer_model)
topics, probs = topic_model.fit_transform(docs)

# %%
# topic_model.get_topic_info()[0:10]
# topic_model.visualize_barchart()
# topic_model.visualize_topics() # Meeh https://github.com/MaartenGr/BERTopic/issues/2269#issuecomment-2607040736
# topic_model.visualize_hierarchy()
# topic_model.visualize_heatmap()
# topic_model.get_document_info(docs)
topic_model.visualize_documents(docs)

# %%
topic_model.visualize_hierarchy()


# %%
