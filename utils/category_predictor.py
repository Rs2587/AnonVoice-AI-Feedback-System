import pickle

with open(
    "category_model.pkl",
    "rb"
) as f:

    model = pickle.load(f)


def predict_category(text):

    prediction = model.predict(
        [text]
    )

    return prediction[0]