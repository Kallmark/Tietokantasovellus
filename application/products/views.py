from application import app, db
from flask import redirect, render_template, request, url_for
from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products", methods=["GET"])
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
def products_form():
    return render_template("products/new.html", form = ProductForm())


@app.route("/products/", methods=["POST"])
def products_create():
    form = ProductForm(request.form)

    t = Product(name = form.name.data, amount = form.amount.data, price =  form.price.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))
