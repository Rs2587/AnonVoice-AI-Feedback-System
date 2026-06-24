import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

df = pd.read_csv(
    "dataset/category_data.csv"
)

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer()
    ),
    (
        "clf",
        MultinomialNB()
    )
])

model.fit(
    df["text"],
    df["category"]
)

with open(
    "category_model.pkl",
    "wb"
) as f:

    pickle.dump(
        model,
        f
    )

print(
    "Category Model Trained Successfully"
)