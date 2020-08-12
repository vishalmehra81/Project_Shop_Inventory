from flask import Blueprint, Flask, render_template, request, redirect

from models.brand import Brand
import repositories.brand_repository as brand_repository

brands_blueprint = Blueprint("brands", __name__)

# INDEX
@brands_blueprint.route("/brands")
def brands():
    brands = brand_repository.select_all()
    return render_template("brands/index.html", brands=brands)

# NEW
@brands_blueprint.route("/brands/new")
def new_brand():
    return render_template("brands/new.html")

# CREATE
@brands_blueprint.route("/brands", methods=["POST"])
def create_brand():
    name = request.form["name"]
    distributor = request.form["distributor"]
    contact = request.form["contact"]
    new_brand = Brand(name, distributor, contact)
    brand_repository.save(new_brand)
    return redirect("/brands")

# EDIT
@brands_blueprint.route("/brands/<id>/edit")
def edit_brand(id):
    brand = brand_repository.select(id)
    return render_template("brands/edit.html", brand=brand)

# UPDATE
@brands_blueprint.route("/brands/<id>", methods=["POST"])
def update_brand(id):
    name = request.form["name"]
    distributor = request.form["distributor"]
    contact = request.form("contact")
    brand = Brand(name, distributor, contact, id)
    brand_repository.update(brand)
    return redirect("/brands")

# DELETE
@brands_blueprint.route("/brands/<id>/delete", methods=["POST"])
def delete_brand(id):
    brand_repository.delete(id)
    return redirect("/brands")