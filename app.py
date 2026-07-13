from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "shopapp123"

products = [
    {"id": 1, "name": "Milk", "price": 30},
    {"id": 2, "name": "Bread", "price": 40},
    {"id": 3, "name": "Eggs", "price": 60},
]

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/add/<int:product_id>")
def add_to_cart(product_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(product_id)
    session.modified = True

    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart_items = []
    total = 0

    if "cart" in session:
        for item_id in session["cart"]:
            for p in products:
                if p["id"] == item_id:
                    cart_items.append(p)
                    total += p["price"]

    return render_template("cart.html", cart_items=cart_items, total=total)

if __name__ == "__main__":
    app.run(debug=True)