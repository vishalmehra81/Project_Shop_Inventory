import pdb

from models.product import Product
import repositories.product_repository as product_repository

from models.brand import Brand
import repositories.brand_repository as brand_repository

from models.stock import Stock
import repositories.stock_repository as stock_repository


product_repository.delete_all()
brand_repository.delete_all()
stock_repository.delete_all()

brand_1 = Brand("AGV","J&S Accessories Ltd","0141 033 4080")
brand_repository.save(brand_1)

brand_2 = Brand("Airoh", "Infinity Motorcycles", "0141 288 0909") 
brand_repository.save(brand_2)

brand_3 = Brand("LS2", "Portman Motors", "0141 169 8564")
brand_repository.save(brand_3)

brand_4 = Brand("Schuberth", "Dales Distribution", "0141 070 8797") 
brand_repository.save(brand_4)

brand_5 = Brand("Nolan", "J&S Accessories Ltd", "0141 033 4080")
brand_repository.save(brand_5)

brand_6 = Brand("Alpinestars", "Dales Distribution", "0141 070 8797") 
brand_repository.save(brand_6)

brand_7 = Brand("Oxford","J&S Accessories Ltd","0141 033 4080")
brand_repository.save(brand_7)

brand_8 = Brand("RST","J&S Accessories Ltd","0141 033 4080")
brand_repository.save(brand_8)

brand_9 = Brand("Furygan", "Portman Motors", "0141 169 8564")
brand_repository.save(brand_9)

brand_10 = Brand("Richa", "Portman Motors", "0141 169 8564")
brand_repository.save(brand_10)

brand_11 = Brand("Sidi","Infinity Motorcycles", "0141 288 0909") 
brand_repository.save(brand_11)

brand_12 = Brand("Spada","Infinity Motorcycles", "0141 288 0909") 
brand_repository.save(brand_12)

stock_1 = Stock(5)
stock_repository.save(stock_1)

stock_2 = Stock(4)
stock_repository.save(stock_2)

stock_3 = Stock(3)
stock_repository.save(stock_3)

stock_4 = Stock(0)
stock_repository.save(stock_4)

stock_5 = Stock(4)
stock_repository.save(stock_5)

stock_6 = Stock(2)
stock_repository.save(stock_6)

stock_7 = Stock(3)
stock_repository.save(stock_7)

stock_8 = Stock(5)
stock_repository.save(stock_8)

stock_9 = Stock(7)
stock_repository.save(stock_9)

stock_10 = Stock(8)
stock_repository.save(stock_10)

stock_11 = Stock(9)
stock_repository.save(stock_11)

stock_12 = Stock(10)
stock_repository.save(stock_12)

stock_13 = Stock(0)
stock_repository.save(stock_13)

stock_14 = Stock(5)
stock_repository.save(stock_14)

stock_15 = Stock(7)
stock_repository.save(stock_15)

stock_16 = Stock(8)
stock_repository.save(stock_16)

stock_17 = Stock(1)
stock_repository.save(stock_17)

stock_18 = Stock(7)
stock_repository.save(stock_18)

stock_19 = Stock(4)
stock_repository.save(stock_19)

stock_20 = Stock(2)
stock_repository.save(stock_20)

product_1 = Product("Atlante White/Blue/Red ", brand_1, stock_1, "Helmet", "XL", 300.99, 359.99)
product_repository.save(product_1)

product_2 = Product("Commander - Matt Orange Fluo", brand_2, stock_2, "Helmet", "XL", 250.99, 289.99)
product_repository.save(product_2)

product_3 = Product("Subverter - Power Chrome/Blue", brand_3, stock_3, "Helmet", "L", 170.99, 199.99)
product_repository.save(product_3)

product_4 = Product("C4 - Legacy Yellow", brand_4, stock_4, "Helmet", "M", 319.99, 649.99)
product_repository.save(product_4)

product_5 = Product("N53 - Portland LED Yellow 060", brand_5, stock_5, "Helmet", "L", 139.99, 161.99)
product_repository.save(product_5)

product_6 = Product("Dyno V2 Leather Jacket - Navy", brand_6, stock_6, "Clothing", "XL", 301.99, 379.99)
product_repository.save(product_6)

product_7 = Product("Girona 1.0 Ladies Textile Jacket - Purple", brand_7, stock_7, "Clothing", "M", 81.99, 119.99)
product_repository.save(product_7)

product_8 = Product("IOM TT Brandish Leather Jacket - Oxblood", brand_8, stock_8, "Clothing", "XL", 199.99, 269.99)
product_repository.save(product_8)

product_9 = Product("Debbie Ladies Leather Jacket - Bordeaux", brand_9, stock_9, "Clothing", "L", 198.99, 287.99)
product_repository.save(product_9)

product_10 = Product("Kelly Ladies Leather Trousers - Black", brand_10, stock_10, "Clothing", "M", 86.99, 119.99)
product_repository.save(product_10)

product_11 = Product(" SMX-6 v2 Drystar® Boots - Black", brand_6, stock_11, "Boots", "M", 199.99, 219.99)
product_repository.save(product_11)

product_12 = Product("Rainseal Over Boots - Black", brand_7, stock_12, "Boots", "L", 15.99, 21.99)
product_repository.save(product_12)

product_13 = Product("Raid WP Boots - Brown", brand_8, stock_13, "Boots", "M", 139.99, 143.99)
product_repository.save(product_13)

product_14 = Product("Melbourne D3O WP Boots - Black", brand_9, stock_14, "Boots", "L", 149.99, 189.99)
product_repository.save(product_14)

product_15 = Product("Crossfire 3 SRS Boots - Blue/Yellow", brand_11, stock_15, "Boots", "L", 250.99, 359.99)
product_repository.save(product_15)

product_16 = Product("Apex V2 Drystar® Glove - Black", brand_6, stock_16, "Gloves", "M", 54.99, 84.99)
product_repository.save(product_16)

product_17 = Product("RP-4 Gloves - Black/White", brand_7, stock_17, "Gloves", "L", 25.99, 49.99)
product_repository.save(product_17)

product_18 = Product("Volt Gloves - Black/Red", brand_8, stock_18, "Gloves", "M", 35.99, 49.99)
product_repository.save(product_18)

product_19 = Product("Volt Gloves - Black/Red", brand_9, stock_19, "Gloves", "L", 43.99, 56.99)
product_repository.save(product_19)

product_20 = Product("Freeride WP Glove - Tan", brand_12, stock_20, "Gloves", "L", 34.99, 45.99)
product_repository.save(product_20)


pdb.set_trace()