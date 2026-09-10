# %%
# Installer bertopic
# # %pip install bertopic

# %%
# importer les bibliothèques nécessaires
import pandas as pd
from bertopic import BERTopic
from sklearn.feature_extraction.text import CountVectorizer

# préciser l'url et charger les données
url = "https://raw.githubusercontent.com/cristobalmitchell/pokedex/refs/heads/main/data/pokemon_utf8.csv"
df = pd.read_csv(url)

# passer les descriptions comme docs
docs = df["description"].tolist()

# créer le modèle de topic modeling et l'appliquer (avec gestion stopwords)
vectorizer_model = CountVectorizer(stop_words="english")
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

# %% [markdown]
# # BUG VERSION NUMPY ? CF RETROUVER COMMENT A DEBUG PRÉCÉDENT ENV
