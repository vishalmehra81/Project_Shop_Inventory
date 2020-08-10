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

