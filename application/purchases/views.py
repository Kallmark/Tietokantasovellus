from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.purchases.models import Purchase
from application.products.models import Product
from application.auth.models import User

@app.route("/purchases/new/")
@login_required
def purchases_form():
    return render_template("purchases/new.html", products = Product.query.all())

@app.route("/purchases/", methods=["POST"])
@login_required
def purchases_create():
    
    t = Purchase(account_id = current_user.id, product_id = request.form.get("purchase"))
    purchaser = User.query.filter_by(id = current_user.id).first()
    purchased_product = Product.query.filter_by(id = request.form.get("purchase")).first()
    purchaser.balance = purchaser.balance - purchased_product.price
    purchased_product.amount = purchased_product.amount - 1

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("purchases_form"))



