from flask import Flask

from routes.feedback_routes import feedback_bp
from routes.admin_routes import admin_bp
from routes.status_routes import status_bp

from models.feedback import init_db

app = Flask(__name__)

app.secret_key = "anonvoice_secret_key"

init_db()

app.register_blueprint(feedback_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(status_bp)

if __name__ == "__main__":
    app.run(debug=True)