from flask import Blueprint, Flask, render_template, request, redirect

from models.stock import Stock
import repositories.stock_repository as stock_repository

stocks_blueprint = Blueprint("stocks", __name__)

# INDEX
@stocks_blueprint.route("/stocks")
def stocks():
    stocks = stock_repository.select_all()
    return render_template("stocks/index.html", stocks=stocks)