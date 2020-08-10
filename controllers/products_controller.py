from flask import Blueprint, Flask, render_template, request, redirect

from models.product import Product
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
    brand = brand_repository.select_all()
    stock = stock_repository.select_all()
    return render_template("/products/new.html", brand=brand, stock=stock)
    













# DELETE
@products_blueprint.route("/products<id>/delete", methods=["POST"]
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")