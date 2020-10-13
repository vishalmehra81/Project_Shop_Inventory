from db.run_sql import run_sql
from models.stock import Stock


def save(stock):
    sql = "INSERT INTO stocks (qty) VALUES (%s) RETURNING id "
    values = [stock.qty]
    results = run_sql(sql, values)
    id = results[0]['id']
    stock.id = id


def select_all():
    stocks = []
    sql = "SELECT * FROM stocks"
    results = run_sql(sql)
    for result in results:
        stock = Stock(result["qty"], result["id"])
        stocks.append(stock)
    return stocks


def select(id):
    sql = "SELECT * FROM stocks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    stock = Stock(result["qty"], result["id"])
    return stock


def delete_all():
    sql = "DELETE FROM stocks"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM stocks WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update():
    sql = "UPDATE stocks SET qty = %s WHERE id = %s "
    run_sql(sql)
