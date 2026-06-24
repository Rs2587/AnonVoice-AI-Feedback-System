from flask import (
    Blueprint,
    render_template,
    request
)

from models.feedback import (
    get_feedback_by_anonymous_id
)

status_bp = Blueprint(
    "status",
    __name__
)


@status_bp.route("/check-status")
def check_status_page():

    return render_template(
        "check_status.html"
    )


@status_bp.route(
    "/track",
    methods=["POST"]
)
def track_complaint():

    anonymous_id = request.form[
        "anonymous_id"
    ]

    complaint = (
        get_feedback_by_anonymous_id(
            anonymous_id
        )
    )

    return render_template(
        "status_result.html",
        complaint=complaint
    )