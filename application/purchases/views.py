from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.purchases.models import Purchase

@app.route("/purchases/new/")
@login_required
def purchases_form():
    return render_template("purchases/new.html")

@app.route("/purchases/", methods=["POST"])
@login_required
def purchases_create():

    #toistaiseksi eri form
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("purchases/new.html", form = form)
    
    t = Purchase(account_id = current_user.id, product_id = 0)

    db.session().add(t)
    db.session().commit()
  




