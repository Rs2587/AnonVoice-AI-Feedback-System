
from flask import Blueprint, render_template, request

from models.feedback import save_feedback
from utils.anonymizer import generate_anonymous_id
from utils.encryption import encrypt_message
from utils.ml_sentiment import predict_sentiment
from utils.category_predictor import predict_category

feedback_bp = Blueprint("feedback", __name__)


@feedback_bp.route("/")
def home():
    return render_template("submit_feedback.html")


@feedback_bp.route("/submit", methods=["POST"])
def submit_feedback():
    message = request.form["message"]
    
    category = predict_category(
    message
    )
    

    anonymous_id = generate_anonymous_id()

    sentiment = predict_sentiment(message)

    encrypted_message = encrypt_message(message)

    save_feedback(
        anonymous_id,
        category,
        encrypted_message,
        sentiment
    )

    return render_template(
        "submission_success.html",
        anonymous_id=anonymous_id,
        sentiment=sentiment,
        category=category
)
