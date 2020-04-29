from flask import Blueprint, render_template, request
from app.order_service import restaurant_list
order_routes = Blueprint("order_routes", __name__)

@order_routes.route("/order")
def order_home():
    print("VISITED THE Georgetown Ordering Service...")

    return render_template("order_home.html")

@order_routes.route("/order/page", methods=["GET", "POST"])
def order_page():
    print("GENERATING A Order FORECAST...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        'zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        'zip_code = request.args["zip_code"]

    results = restaurant_list
    print(results)
    return render_template("order_page.html")