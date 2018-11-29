from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.purchases.models import Purchase
from application.products.models import Product

@app.route("/purchases/new/")
@login_required
def purchases_form():
    return render_template("purchases/new.html", products = Product.query.all())

@app.route("/purchases/", methods=["POST"])
@login_required
def purchases_create():
    
    t = Purchase(account_id = current_user.id, product_id = request.form.get("purchase"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("purchases_form"))



