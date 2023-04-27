from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.users_models import User
from flask_app.models.works_models import Work


# ===============create page==============
@app.route("/works/new")
def new_work():
    logged_in_user = User.get_user(session["user_id"])
    return render_template("new_work.html", logged_in_user=logged_in_user)


# ===============create method==============
@app.route("/works/create", methods=["POST"])
def create_work():
    if not Work.validate(request.form):
        return redirect("/works/new")

    Work.create_work(request.form)
    return redirect("/dash")


# ============= Get one work =============
@app.route("/works/<int:id>")
def get_work(id):
    work = work.get_work(id)
    return render_template("work_card.html", work=work)


# ============= Update work Render=============
@app.route("/update/<int:id>")
def update_work(id):
    work = work.get_work(id)
    return render_template("update_work.html", work=work)


# ============= Update work =============
@app.route("/works/update", methods=["POST"])
def update_works():
    if not Work.validate(request.form):
        return redirect(f"/update/{request.form['id']}")
    Work.update(request.form)
    return redirect("/dash")


# ============= Delete work =============
@app.route("/works/delete/<int:id>", methods=["POST"])
def delete_work(id):
    Work.delete({'work_id': id})
    return redirect("/dash")
