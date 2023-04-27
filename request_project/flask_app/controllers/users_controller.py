from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users_models import User
from flask_app.models import works_models
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


# =============Login Page Registration RENDER============
@app.route("/")
def index():
    return render_template("index.html")


# ============User-Reg Page Registration METHOD============
@app.route("/user/reg", methods=["POST"])
def reg_user():
    if not User.validate(request.form):
        return redirect("/")
    hash = bcrypt.generate_password_hash(request.form["password"])
    user_data = {
        **request.form,
        "password": hash
    }
    user_id = User.create_user(user_data)
    session["user_id"] = user_id
    return redirect("/dash")


# ============User Dash============
@app.route("/dash")
def dash():
    # guard
    if "user_id" not in session:
        return redirect("/")
    logged_in_user = User.get_user(session["user_id"])


#  =========================return all the sightings====================
    all_works = works_models.Work.get_all()
    return render_template("dash.html", logged_in_user=logged_in_user, all_works=all_works)


# ============LOGIN USER=================
@app.route("/user/login", methods=["POST"])
def login():
    user_db = User.get_user_by_email(request.form["email"])
    if not user_db:
        flash("Invalid Email", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_db.password, request.form["password"]):
        flash("Invalid Password", "log")
        return redirect("/")
    session["user_id"] = user_db.id
    return redirect("/dash")


# =============LOGOUT USER=================

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
