from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.purchases.models import Purchase
from application.products.models import Product
from application.auth.models import User

@app.route("/purchases/new/")
@login_required("ANY")
def purchases_form():
    return render_template("purchases/new.html", products = Product.query.all())

@app.route("/purchases/", methods=["POST"])
@login_required("ANY")
def purchases_create():
    
    t = Purchase(account_id = current_user.id, product_id = request.form.get("product"))
    purchaser = User.query.filter_by(id = current_user.id).first()
    purchased_product = Product.query.filter_by(id = request.form.get("product")).first()
    purchaser.balance = purchaser.balance - purchased_product.price
    purchased_product.amount = purchased_product.amount - 1

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("purchases_form"))

#statistics for all users. shows most purchased products and top three users by purchase count. 
@app.route("/statistics", methods=["GET"])
@login_required(role="ANY")
def purchases_stats():


    products = Purchase.most_purchased_products()
    users = Purchase.top_five_customers()

    return render_template("purchases/stats.html", products = products, users = users)



