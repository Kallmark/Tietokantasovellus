from flask import render_template, request, redirect, url_for
from flask_login import login_user, login_required, current_user, logout_user
from application import app
from application.auth.models import User
from application.auth.forms import LoginForm
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
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/profile")
@login_required
def profile_look():
    
    return render_template("auth/profile.html", user = User.query.filter_by(id = current_user.id).first())

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  
