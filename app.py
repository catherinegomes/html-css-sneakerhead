from flask import Flask, render_template, url_for
import jinja2
import requests, os

app = Flask(__name__, static_folder = 'Resources', template_folder ='templates')
@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html", text = 'Sneaker Head Home')

@app.route("/scatter.html")
def scatter():
    return render_template("scatter.html", text = 'Top 3 Brands by Scatter')

@app.route("/percentile.html")
def bubble():
    return render_template("percentile.html", text = 'Top 3 Brands by Percentile')

@app.route("/oregon.html")
def oregon():
    return render_template("oregon.html", text = 'Oregon')

@app.route("/ny.html")
def new_york():
    return render_template("ny.html", text = 'New York')

@app.route("/fl.html")
def florida():
    return render_template("fl.html", text = 'Florida')

@app.route("/tx.html")
def texas():
    return render_template("tx.html", text = 'Texas')

@app.route("/ca.html")
def california():
    return render_template("ca.html", text = 'California')

@app.route("/comparison.html")
def comparison():
    return render_template("comparison.html", text = 'Compare visualizations')

@app.route("/data.html")
def data():
    return render_template("StockX-Data-2019.html", text = 'See all data')

if __name__ == "__main__":
    app.run(debug=True)