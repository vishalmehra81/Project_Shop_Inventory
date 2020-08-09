from flask import Blueprint, Flask, render_template, request, redirect

from models.stock import Stock
import repositories.stock_repository as stock_repository

stocks_blueprint = Blueprint("stocks", __name__)