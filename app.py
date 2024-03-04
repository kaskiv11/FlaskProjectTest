from flask import Flask, render_template

app = Flask(__name__)

pizza_shop_info = {
    'name': 'My New Pizza',
    'image': 'https://www.allrecipes.com/thmb/iXKYAl17eIEnvhLtb4WxM7wKqTc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/240376-homemade-pepperoni-pizza-Beauty-3x4-1-6ae54059c23348b3b9a703b6a3067a44.jpg'
}

menu_shop = [
    {'name': 'Margherita', 'description': 'Margherita classic tomatoes', 'price': 80.22},
    {'name': 'Three cheeses', 'description': 'Three cheeses classic', 'price': 90.22}
]

@app.route('/')
def hello_world():
    return render_template('index.html', pizza_shop_info=pizza_shop_info)

@app.route('/menu')
def index():
    return render_template('menu.html', menu_shop=menu_shop)

if __name__ == "__main__":
    app.run(debug=True)
