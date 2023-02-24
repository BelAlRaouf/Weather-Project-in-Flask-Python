from flask import Flask, render_template
import pandas as pd

app = Flask("website")


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    df = pd.read_csv()
    temperature = 23
    return {'station': station,
            'date': date,
            'temperature': temperature}


app.run(debug=True)
