from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.stock import Stock
import repositories.stock_repository as stock_repository

stocks_blueprint = Blueprint("stocks", __name__)