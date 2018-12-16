from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products", methods=["GET"])
@login_required(role="ANY")
def products_index():
    return render_template("products/list.html", products = Product.query.all())

@app.route("/products/new/")
@login_required(role="ADMIN")
def products_form():
    return render_template("products/new.html", form = ProductForm())


@app.route("/products/", methods=["POST"])
@login_required(role="ADMIN")
def products_create():

    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)

    t = Product(name = form.name.data, amount = form.amount.data, price =  form.price.data)

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/edit/<int:id>", methods=["GET","POST"])
@login_required(role="ADMIN")
def products_edit(id):

    product = Product.query.get(id)

    #GET

    if request.method == "GET":
        form = ProductForm(obj = product)
        return render_template("products/edit.html", form = form, product_id = id)

    #POST

    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form = form)

    product.name = form.name.data
    product.amount = form.amount.data
    product.price = form.price.data

    db.session().commit()
  
    return redirect(url_for("products_index"))

@app.route("/products/delete/<int:id>", methods=["GET"])
@login_required(role="ADMIN")
def products_delete(id):

    product = Product.query.get(id)

    #GET

    db.session().delete(product)
    db.session().commit()
  
    return redirect(url_for("products_index"))
