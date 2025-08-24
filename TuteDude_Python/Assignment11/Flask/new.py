# IMPORTING FLASK MODULE
from flask import  Flask, render_template, request, redirect, url_for

# INTERACTION WITH FLASK
app = Flask(__name__)

# MAPPING URL TO FUNCTION
@app.route("/", methods=["GET", "POST"])
@app.route("/register", methods=["GET", "POST"])

#INPUTS
def homepage():
    return render_template("register.html")


@app.route("/confirmation", methods=["GET", "POST"])
def success():
    if request.method == "POST":
        name = request.form.get("name")
        city = request.form.get("city")
        email = request.form.get("email")
        phone = request.form.get("phone")
        return render_template("confirm.html", name=name, city=city, email=email, phone=phone)




#MAIN FUNCTION
if __name__ == "__main__":
    app.run(debug=True)