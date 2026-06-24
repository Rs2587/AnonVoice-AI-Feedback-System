import sqlite3
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from utils.encryption import decrypt_message

conn = sqlite3.connect(
    "database/feedback.db"
)

cursor = conn.execute(
    """
    SELECT message
    FROM feedback
    """
)

rows = cursor.fetchall()

messages = []

for row in rows:

    try:
        messages.append(
            decrypt_message(row[0])
        )
    except:
        messages.append(
            row[0]
        )

if len(messages) < 3:

    print(
        "Need at least 3 complaints for clustering"
    )

else:

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    X = vectorizer.fit_transform(
        messages
    )

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X)

    df = pd.DataFrame({
        "Complaint": messages,
        "Cluster": labels
    })

    print(df)