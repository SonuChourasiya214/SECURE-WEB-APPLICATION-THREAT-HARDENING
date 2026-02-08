from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from ..models import db, User
from ..security.hashing import hash_password, verify_password
from ..security.validators import validate_username, validate_password

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and verify_password(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard.dashboard"))
        flash("Invalid credentials")
    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not validate_username(username) or not validate_password(password):
            flash("Weak credentials")
            return redirect(url_for("auth.register"))

        user = User(username=username, password=hash_password(password))
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect(url_for("auth.login"))

    return render_template("register.html")

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
