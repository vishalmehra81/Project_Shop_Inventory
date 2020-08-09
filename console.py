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

brand_1 = Brand("AGV")
brand_repository.save(brand_1)

brand_2 = Brand("Airoh")
brand_repository.save(brand_2)

brand_3 = Brand("LS2")
brand_repository.save(brand_3)

brand_4 = Brand("Schuberth")
brand_repository.save(brand_4)

stock_1 = Stock(5)
stock_repository.save(stock_1)

stock_2 = Stock(4)
stock_repository.save(stock_2)

stock_3 = Stock(3)
stock_repository.save(stock_3)

stock_4 = Stock(0)
stock_repository.save(stock_4)

product_1 = Product('K1-Mir 2018', 1, 4, 'Helmet', 'L', 130.99, 169.99)
product_repository.save(product_1)

product_2 = Product('Commander - Matt Orange Fluo ', 2, 3, 'Helmet', 'XL', 250.99, 289.99)
product_repository.save(product_2)


product_3 = Product('Subverter - Power Chrome/Blue', 3, 1, 'Helmet', 'L', 170.99, 199.99)
product_repository.save(product_3)


product_4 = Product('C4 - Legacy Yellow', 4, 2, 'Helmet', 'M', 319.99, 649.99)
product_repository.save(product_4)

pdb.set_trace()