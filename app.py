from flask import Flask, Blueprint, render_template, redirect, url_for
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/admin")
def admin():
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True, port=8000)

