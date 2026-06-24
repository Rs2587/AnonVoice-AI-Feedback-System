import matplotlib
matplotlib.use("Agg")


import matplotlib.pyplot as plt
import pandas as pd
from utils.cluster_helper import get_clusters

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    send_file
)

from models.feedback import (
    get_feedback,
    search_feedback,
    delete_feedback,
    update_status,
    update_comment
)

from utils.encryption import decrypt_message

admin_bp = Blueprint("admin", __name__)

USERNAME = "admin"
PASSWORD = "admin123"


@admin_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["admin"] = True

            return redirect("/admin")

    return render_template("login.html")


@admin_bp.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


@admin_bp.route("/status/<int:id>/<status>")
def change_status(id, status):

    if not session.get("admin"):
        return redirect("/login")

    update_status(id, status)

    return redirect("/admin")

@admin_bp.route(
    "/comment/<int:id>",
    methods=["POST"]
)
def add_comment(id):

    if not session.get("admin"):
        return redirect("/login")

    comment = request.form["comment"]

    update_comment(
        id,
        comment
    )

    return redirect("/admin")


@admin_bp.route("/admin")
def admin_dashboard():

    if not session.get("admin"):
        return redirect("/login")

    keyword = request.args.get("search")

    if keyword:
        feedbacks = search_feedback(keyword)
    else:
        feedbacks = get_feedback()

    decrypted_feedbacks = []

    category_count = {}
    sentiment_count = {}

    for row in feedbacks:

        try:
            message = decrypt_message(row[3])
        except:
            message = row[3]

        category = row[2]
        sentiment = row[4]
        status = row[5]

        category_count[category] = (
            category_count.get(category, 0) + 1
        )

        sentiment_count[sentiment] = (
            sentiment_count.get(sentiment, 0) + 1
        )
        
        decrypted_feedbacks.append({
            "id": row[0],
            "anonymous_id": row[1],
            "category": category,
            "message": message,
            "sentiment": sentiment,
            "status": status,
            "admin_comment": row[6],
            "created_at": row[7]
        })
    top_category = "None"

    if category_count:
        top_category = max(
            category_count,
            key=category_count.get
        )

    if category_count:

        plt.figure(figsize=(5, 5))

        plt.pie(
            category_count.values(),
            labels=category_count.keys(),
            autopct="%1.1f%%"
        )

        plt.title("Complaint Categories")

        plt.savefig(
            "static/charts/category_chart.png"
        )

        plt.close()

    if sentiment_count:

        plt.figure(figsize=(5, 5))

        plt.pie(
            sentiment_count.values(),
            labels=sentiment_count.keys(),
            autopct="%1.1f%%"
        )

        plt.title("Sentiment Distribution")

        plt.savefig(
            "static/charts/sentiment_chart.png"
        )

        plt.close()

    clusters = get_clusters()
    
    return render_template(
        "admin_dashboard.html",
        feedbacks=decrypted_feedbacks,
        top_category=top_category,
        clusters=clusters
    )

@admin_bp.route("/export/excel")
def export_excel():

    if not session.get("admin"):
        return redirect("/login")

    feedbacks = get_feedback()

    rows = []

    for row in feedbacks:

        try:
            message = decrypt_message(row[3])
        except:
            message = row[3]

        rows.append({  
            "Anonymous ID": row[1],
            "Category": row[2],
            "Feedback": message,
            "Sentiment": row[4],
            "Status": row[5],
            "Admin Comment": row[6],
            "Created At": row[7]
        })

    df = pd.DataFrame(rows)

    file_name = "feedback_report.xlsx"

    df.to_excel(file_name, index=False)

    return send_file(
        file_name,
        as_attachment=True
    )


@admin_bp.route("/export/pdf")
def export_pdf():

    if not session.get("admin"):
        return redirect("/login")

    feedbacks = get_feedback()

    pdf_file = "feedback_report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    elements = []

    styles = getSampleStyleSheet()

    elements.append(
        Paragraph(
            "Anonymous Student Feedback Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    data = [[
        "Anonymous ID",
        "Category",
        "Sentiment",
        "Status"
    ]]

    for row in feedbacks:

        data.append([
            row[1],
            row[2],
            row[4],
            row[5]
        ])

    table = Table(data)

    table.setStyle(
        TableStyle([
            ("GRID", (0,0), (-1,-1), 1, colors.black),
            ("BACKGROUND", (0,0), (-1,0), colors.lightgrey)
        ])
    )

    elements.append(table)

    doc.build(elements)

    return send_file(
        pdf_file,
        as_attachment=True
    )


@admin_bp.route("/delete/<int:id>")
def delete(id):

    if not session.get("admin"):
        return redirect("/login")

    delete_feedback(id)

    return redirect("/admin")

