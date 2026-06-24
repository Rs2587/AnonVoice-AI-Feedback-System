import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

import pickle

df = pd.read_csv(
    "dataset/sentiment_data.csv"
)

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

model.fit(
    df["text"],
    df["sentiment"]
)

with open(
    "sentiment_model.pkl",
    "wb"
) as f:
    pickle.dump(model, f)

print("Model Trained Successfully")