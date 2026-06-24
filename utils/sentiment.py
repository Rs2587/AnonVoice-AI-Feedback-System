def analyze_sentiment(text):

    text = text.lower()

    urgent_words = [
        "ragging",
        "harassment",
        "violence",
        "abuse",
        "threat",
        "fight"
    ]

    positive_words = [
        "good",
        "excellent",
        "great",
        "helpful",
        "awesome",
        "best"
    ]

    for word in urgent_words:
        if word in text:
            return "Urgent"

    for word in positive_words:
        if word in text:
            return "Positive"

    return "Negative"