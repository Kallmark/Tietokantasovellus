from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user
from application import app, db, login_required
from application.auth.models import User
from application.roles.models import Role
from application.auth.forms import LoginForm, RegisterForm, EditForm, Edit_UserForm
from application.products.models import Product
from application.purchases.models import Purchase

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/register", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
      return render_template("auth/registerform.html", form = form)
    
    user = User.query.filter_by(username=form.username.data).first()
    if user:
        return render_template("auth/registerform.html", form = form, error = "Username already taken!")
    
    user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    role = Role()
    role.account_id = user.id

    db.session().add(role)
    db.session().commit()

    login_user(user)

    return redirect(url_for("index"))

@app.route("/auth/profile")
@login_required("ANY")
def profile_look():
    
    return render_template("auth/profile.html", user = User.query.filter_by(id = current_user.id).first())

@app.route("/profile/edit/<int:id>", methods = ["GET", "POST"])
@login_required("ANY")
def profile_edit(id):

    user = current_user

    if current_user.id != id:
        return redirect(url_for('profile_look'))

    #GET

    if request.method == "GET":
        form = EditForm(obj = user)
        return render_template("auth/edit.html", form = form, user_id = id)

    #POST

    form = EditForm(request.form)

    if not form.validate():
        return render_template("auth/edit.html", form = form, user_id = id, error = "Something went wrong!")

    if str(user.password) != str(form.old_password.data):
        return render_template("auth/edit.html", form = form, user_id = id, error = "Old password didn't match with the given password!")

    user.name = form.name.data
    user.username = form.username.data
    user.password = form.new_password.data

    db.session().commit()
  
    return redirect(url_for("profile_look"))

@app.route("/users", methods=["GET"])
@login_required(role="ADMIN")
def users_list():
    return render_template("auth/list.html", users = User.query.all())

@app.route("/users/edit/<int:id>", methods=["GET","POST"])
@login_required(role="ADMIN")
def user_edit(id):

    user = User.query.get(id)

    #GET

    if request.method == "GET":
        form = Edit_UserForm(obj = user)
        return render_template("auth/edit_user.html", form = form, user_id = id)

    #POST

    form = Edit_UserForm(request.form)

    if not form.validate():
        return render_template("auth/list.html", form = form)

    user.balance = form.balance.data

    db.session().commit()
  
    return redirect(url_for("users_list"))

@app.route("/users/delete/<int:id>", methods=["GET"])
@login_required(role="ADMIN")
def users_delete(id):

    user = User.query.get(id)

    purchases = user.purchases


    for purchase in purchases:
        db.session.delete(purchase)

    roles = user.roles

    for role in roles:
        db.session.delete(role)


    db.session().delete(user)
    db.session().commit()
  
    return redirect(url_for("users_list"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


