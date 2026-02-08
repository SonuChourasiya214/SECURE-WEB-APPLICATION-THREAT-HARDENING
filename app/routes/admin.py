from flask import Blueprint, abort, render_template
from flask_login import login_required, current_user
from ..models import User

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/")
@login_required
def admin_panel():
    if current_user.role != "admin":
        abort(403)
    users = User.query.all()
    return render_template("admin.html", users=users)
