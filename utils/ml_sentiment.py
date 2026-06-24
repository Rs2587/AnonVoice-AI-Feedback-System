import pickle

with open(
    "sentiment_model.pkl",
    "rb"
) as f:

    model = pickle.load(f)


def predict_sentiment(text):

    prediction = model.predict([text])

    return prediction[0]