from flask import Flask, render_template
from flask import Blueprint
from models.brand import Brand
import repositories.brand_repository as brand_repository

brands_blueprint = Blueprint(" Brands", __name__)
