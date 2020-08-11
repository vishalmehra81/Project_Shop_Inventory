from db.run_sql import run_sql
from models.brand import Brand

def save(brand):
    sql = "INSERT INTO brands (name, distributor, contact) VALUES (%s,%s,%s) RETURNING id"
    values = [brand.name, brand.distributor, brand.contact]
    results = run_sql(sql, values)
    id = results[0]['id']
    brand.id = id

def select_all():
    brands = []
    sql = "SELECT * FROM brands"
    results= run_sql(sql)
    for result in results:
        brand = Brand(result["name"],result["distributor"], result["contact"],result["id"])
        brands.append(brand)
    return brands

def select(id):
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    brand = Brands(result["name"], result["id"])
    return brand

def delete_all():
    sql = "DELETE FROM brands"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(brand):
    sql = "UPDATE brands SET name = %s WHERE id = %s"
    values = [brand.name, brand.id]
    run_sql(sql, values) 
