from flask import Blueprint, Flask, render_template, request, redirect

from models.product import Product
from models.stock import Stock
import repositories.product_repository as product_repository
import repositories.brand_repository as brand_repository
import repositories.stock_repository as stock_repository

products_blueprint = Blueprint("products", __name__)

# INDEX
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template ("products/index.html", products=products)

# NEW
@products_blueprint.route("/products/new")
def new_product():
    brands = brand_repository.select_all()
    stocks = stock_repository.select_all()
    return render_template("/products/new.html", brands=brands, stocks=stocks)

# CREATE
@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    brand_id = request.form["brand_id"]
    brand = brand_repository.select(brand_id)
    new_stock = Stock(request.form["qty"])
    stock_repository.save(new_stock)
    category = request.form["category"]
    size = request.form["size"]
    cost_price = request.form["cost_price"]
    selling_price = request.form["selling_price"]
    new_product = Product(name, brand, new_stock, category, size, cost_price, selling_price)
    product_repository.save(new_product)
    return redirect("/products")

# EDIT
@products_blueprint.route("/products/<id>/edit")
def edit_product():
    product = product_repository.select(id)
    brand = brand_repository.select_all()
    stock = stock_repository.select_all()
    return render_template("products/edit.html", product=product, brand=brand, stock=stock)

# UPDATE
@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    brand_id = request.form["brand_id"]
    brand = brand_repository.select(brand_id)
    stock_id = request.form["stock_id"]
    stock = stock_repository.select(stock_id)
    category = request.form["category"]
    size = request.form["size"]
    cost_price = request.form["cost_price"]
    selling_price = request.form["selling_price"]
    product = Product(name, brand, stock, category, size, cost_price, selling_price, id)
    product_repository.update(product)
    return redirect("/products")

# DELETE
@products_blueprint.route("/products<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")

