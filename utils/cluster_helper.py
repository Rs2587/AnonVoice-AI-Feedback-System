import sqlite3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from utils.encryption import decrypt_message


def get_clusters():

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

    conn.close()

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
        return {}

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

    clusters = {}

    for msg, label in zip(
        messages,
        labels
    ):

        if label not in clusters:
            clusters[label] = []

        clusters[label].append(msg)

    return clusters