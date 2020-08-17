from db.run_sql import run_sql
from models.product import Product
from models.brand import Brand
from models.stock import Stock
import repositories.brand_repository as brand_repository
import repositories.stock_repository as stock_repository

def save(product):
    sql = "INSERT INTO products (name, brand_id, stock_id, category, size, cost_price, selling_price) VALUES (%s,%s,%s,%s,%s,%s,%s) RETURNING id"
    values = [product.name, product.brand.id, product.stock.id, product.category, product.size, product.cost_price, product.selling_price]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    

def select_all():
    products = []
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    for result in results:
        brand = brand_repository.select(result["brand_id"])
        stock = stock_repository.select(result["stock_id"])
        product = Product(result["name"],brand, stock, result["category"],result["size"], result["cost_price"], result["selling_price"])
        products.append(product)
    return products

def select(id):
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    brand = brand_repository.select(result["brand_id"])
    stock = stock_repository.select(result["stock-id"])
    product = Product(result["name"], brand, stock, result["category"]), result["size"], result["cost_price"], result["selling_price"]
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, brand_id, stock_id, category, size, cost_price, selling_price) VALUES (%s,%s,%s,%s,%s,%s,%s) WHERE id = %s"
    values = [product.name, brand.brand.id, stock.stock.id, product.category, product.size, product.cost_price, product.selling_price]
    run_sql(sql, values)




