from flask import Blueprint, Flask, render_template, request, redirect

from models.stock import Stock
import repositories.stock_repository as stock_repository

stocks_blueprint = Blueprint("stocks", __name__)

# INDEX
@stocks_blueprint.route("/stocks")
def stocks():
    stocks = stock_repository.select_all()
    return render_template("stocks/index.html", stocks=stocks)

# NEW
@stocks_blueprint.route("/stocks/new")
def new_stock():
    return render_template("stocks/new.html")

# CREATE
@stocks_blueprint.route("/stocks", methods=["POST"])
def create_stock():
    qty = request.form["qty"]
    new_stock = Stock(qty)
    stock_repository.save(new_stock)
    return redirect("/stocks")

# EDIT
@stocks_blueprint.route("/stocks/<id>/edit")
def edit_stock(id):
    brand = brand_repository.select(id)
    return render_template("stocks/edit.html", stock=stock)

# UPDATE
@stocks_blueprint.route("/stocks/<id>", methods=["POST"])
def update_stock(id):
    qty = request.form["qty"]
    stock = Stock(qty, id)
    stock_repository.update(stock)
    return redirect("/stocks")

# DELETE
@stocks_blueprint.route("/stocks/<id>/delete", methods=["POST"])
def delete_stock(id):
    stock_repository.delete(id)
    return redirect("/stocks")