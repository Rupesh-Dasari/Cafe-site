from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# ✅ Café Menu with images
menu = [
    {"name": "Coffee", "price": 50, "image": "https://cdn.pixabay.com/photo/2017/04/23/20/24/coffee-2255200_1280.jpg"},
    {"name": "Tea", "price": 30, "image": "https://cdn.pixabay.com/photo/2016/11/29/09/08/beverage-1869598_1280.jpg"},
    {"name": "Sandwich", "price": 70, "image": "https://cdn.pixabay.com/photo/2014/10/19/20/59/sandwich-494706_1280.jpg"},
    {"name": "Burger", "price": 120, "image": "https://cdn.pixabay.com/photo/2016/03/05/19/02/hamburger-1238246_1280.jpg"},
    {"name": "Pizza", "price": 200, "image": "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_1280.jpg"},
]

orders = []  # stores all orders (no database)

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

@app.route("/order", methods=["POST"])
def order():
    selected_items = request.form.getlist("items")
    order_list = []
    total = 0

    for item in menu:
        if item["name"] in selected_items:
            order_list.append(item)
            total += item["price"]

    order_details = {
        "items": order_list,
        "total": total,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    orders.append(order_details)
    return render_template("bill.html", order=order_details)

@app.route("/reports")
def reports():
    return render_template("reports.html", orders=orders)

if __name__ == "__main__":
    app.run(debug=True)
