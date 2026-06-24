import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_NAME = os.path.join(
    BASE_DIR,
    "database",
    "feedback.db"
)


def init_db():

    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anonymous_id TEXT,
        category TEXT,
        message TEXT,
        sentiment TEXT,
        status TEXT DEFAULT 'Pending',
        admin_comment TEXT DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_feedback(
    anonymous_id,
    category,
    message,
    sentiment
):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        INSERT INTO feedback(
            anonymous_id,
            category,
            message,
            sentiment,
            status,
            admin_comment
        )
        VALUES(?,?,?,?,?,?)
        """,
        (
            anonymous_id,
            category,
            message,
            sentiment,
            "Pending",
            ""
        )
    )

    conn.commit()
    conn.close()


def get_feedback():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT *
        FROM feedback
        ORDER BY created_at DESC
        """
    )

    data = cursor.fetchall()

    conn.close()

    return data


def search_feedback(keyword):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT *
        FROM feedback
        WHERE category LIKE ?
        OR message LIKE ?
        OR sentiment LIKE ?
        OR status LIKE ?
        OR admin_comment LIKE ?
        ORDER BY created_at DESC
        """,
        (
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%",
            f"%{keyword}%"
        )
    )

    data = cursor.fetchall()

    conn.close()

    return data


def update_status(feedback_id, status):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        UPDATE feedback
        SET status=?
        WHERE id=?
        """,
        (
            status,
            feedback_id
        )
    )

    conn.commit()
    conn.close()


def update_comment(feedback_id, comment):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        UPDATE feedback
        SET admin_comment=?
        WHERE id=?
        """,
        (
            comment,
            feedback_id
        )
    )

    conn.commit()
    conn.close()


def delete_feedback(feedback_id):

    conn = sqlite3.connect(DB_NAME)

    conn.execute(
        """
        DELETE FROM feedback
        WHERE id=?
        """,
        (feedback_id,)
    )

    conn.commit()
    conn.close()


def get_feedback_by_anonymous_id(anonymous_id):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.execute(
        """
        SELECT *
        FROM feedback
        WHERE anonymous_id=?
        """,
        (anonymous_id,)
    )

    data = cursor.fetchone()

    conn.close()

    return data

