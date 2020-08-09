from flask import Flask

from controllers.brand_controller import brands_blueprint
from controllers.product_controller import products_blueprint
from controllers.stock_controller import stocks_blueprint

app = Flask(__name__)

app.register_blueprint(brands_blueprint)
app.register_blueprint(products_blueprint)
app.register_blueprint(stocks_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)