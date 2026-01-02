from flask import Blueprint, flash, g
from flask import redirect, render_template, request
from flask import url_for

from werkzeug.exceptions import abort

from flaskr.blueprints.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)


@bp.route("/")
def index():
    db = get_db()
    posts = db.execute(
        "SELECT p.id, title, body, created, author_id, username "
        "FROM post p JOIN user u ON p.author_id = u.id "
        "ORDER BY created DESC"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)
