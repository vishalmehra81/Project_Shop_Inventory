from flask import Blueprint, Flask, render_template, request, redirect

from models.brand import Brand
import repositories.brand_repository as brand_repository

brands_blueprint = Blueprint("brands", __name__)
