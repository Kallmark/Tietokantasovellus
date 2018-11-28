from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required
from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products", methods=["GET"])
@login_required
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
@login_required
def products_form():
    return render_template("products/new.html", form = ProductForm())


@app.route("/products/", methods=["POST"])
@login_required
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)

    t = Product(name = form.name.data, amount = form.amount.data, price =  form.price.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))
