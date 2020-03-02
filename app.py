from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder = 'Resources')

@app.route("/")
def index():
    return render_template("index.html", text = 'Sneaker Head Home')

@app.route("/scatter")
def scatter():
    return render_template("scatter.html", text = 'Top 3 Brands by Scatter')

@app.route("/percentile")
def bubble():
    return render_template("percentile.html", text = 'Top 3 Brands by Percentile')

@app.route("/oregon")
def oregon():
    return render_template("oregon.html", text = 'Oregon')

@app.route("/ny")
def new_york():
    return render_template("ny.html", text = 'New York')

@app.route("/fl")
def florida():
    return render_template("fl.html", text = 'Florida')

@app.route("/tx")
def texas():
    return render_template("tx.html", text = 'Texas')

@app.route("/ca")
def california():
    return render_template("ca.html", text = 'California')

@app.route("/comparison")
def comparison():
    return render_template("comparison.html", text = 'Compare visualizations')

@app.route("/data")
def data():
    return render_template("StockX-Data-2019.html", text = 'See all data')

if __name__ == "__main__":
    app.run(debug=True)