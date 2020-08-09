from db.run_sql import run_sql
from models.product import Product
from models.brand import Brand
from models.stock import Stock
import repositories.brand_repository as brand_repository
import repositories.stock_repository as stock_repository

def save(product):
    sql = "INSERT INTO products (name, brand_id, stock_id, category, size, cost_price, selling_price) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [product.name, brand.brand.id, stock.stock.id, product.category, product.size, product.cost_price, product.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id

def select_all():
    products = []
    






# select
# delete
# delete_all
# update
