import pdb
from models.brand import Brand
from models.product import Product
from models.stock import Stock

import repositories.brand_repository as brand_repository
import repositories.product_repository as product_repository
import repositories.stock_repository as stock_repository

# brand_repository.delete_all()
# product_repository.delete_all()
# stock_repository.delete_all()

brand1 = Brand("AGV")
brand_repository.save(brand1)

brand2 = Brand("Airoh")
brand_repository.save(brand2)

brand3 = Brand("LS2")
brand_repository.brand(brand3)

brand4 = Brand("Schuberth")
brand_repository.save(brand4)






pdb.set_trace()