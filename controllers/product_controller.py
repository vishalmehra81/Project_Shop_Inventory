from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.brand_repository as brand_repository
import repositories.stock_repository as stock_repository

products_blueprint = Blueprint("products", __name__)