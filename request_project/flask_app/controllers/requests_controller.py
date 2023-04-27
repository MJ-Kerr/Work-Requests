from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users_models import User
from flask_app.models.requests_models import request


# ===============create page==============
@app.route("/requests/new")
def new_request():
    logged_in_user = User.get_user(session["user_id"])
    return render_template("new_request.html", logged_in_user=logged_in_user)


# ===============create method==============
@app.route("/requests/create", methods=["POST"])
def create_request():
    if not request.validate(request.form):
        return redirect("/requests/new")

    request.create_request(request.form)
    return redirect("/dash")


# ============= Get one request =============
@app.route("/requests/<int:id>")
def get_request(id):
    request = request.get_request(id)
    return render_template("request_card.html", request=request)


# ============= Update request Render=============
@app.route("/update/<int:id>")
def update_request(id):
    request = request.get_request(id)
    return render_template("update_request.html", request=request)


# ============= Update request =============
@app.route("/requests/update", methods=["POST"])
def update_requests():
    if not request.validate(request.form):
        return redirect(f"/update/{request.form['id']}")
    request.update(request.form)
    return redirect("/dash")


# ============= Delete request =============
@app.route("/requests/delete/<int:id>", methods=["POST"])
def delete_request(id):
    request.delete({'request_id': id})
    return redirect("/dash")
