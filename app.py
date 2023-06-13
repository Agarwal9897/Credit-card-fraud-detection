# save this as app.py
from flask import Flask, escape, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")


@app.route('/logistic_regression', methods=['GET', 'POST'])
def logistic_regression():
    if request.method ==  'POST':
        model = pickle.load(open('lgr.pkl', 'rb'))
        avg_amount_days = float(request.form['avg_amount_days'])
        transaction_amount = float(request.form['transaction_amount'])
        daily_chbk_avg_amt = float(request.form['daily_chbk_avg_amt'])
        avg_chbk_amt = float(request.form['avg_chbk_amt'])
        chbk_freq = float(request.form['chbk_freq'])

        prediction = model.predict([[avg_amount_days, transaction_amount, daily_chbk_avg_amt, avg_chbk_amt, chbk_freq]])

        # print(prediction)

        if(prediction==0):
            prediction="NOT A FRAUD"
        else:
            prediction="FRAUD"


        return render_template("logistic_regression.html", prediction_text="THIS IS {}".format(prediction))
    else:
        return render_template("logistic_regression.html")

@app.route('/random_forest', methods=['GET', 'POST'])
def random_forest():
    if request.method ==  'POST':
        model = pickle.load(open('lgr.pkl', 'rb'))
        avg_amount_days = float(request.form['avg_amount_days'])
        transaction_amount = float(request.form['transaction_amount'])
        daily_chbk_avg_amt = float(request.form['daily_chbk_avg_amt'])
        avg_chbk_amt = float(request.form['avg_chbk_amt'])
        chbk_freq = float(request.form['chbk_freq'])

        prediction = model.predict([[avg_amount_days, transaction_amount, daily_chbk_avg_amt, avg_chbk_amt, chbk_freq]])

        # print(prediction)

        if(prediction==0):
            prediction="NOT A FRAUD"
        else:
            prediction="FRAUD"

        return render_template("random_forest.html", prediction_text="THIS IS {}".format(prediction))
    else:
        return render_template("random_forest.html")

@app.route('/decision_tree', methods=['GET', 'POST'])
def decision_tree():
    if request.method ==  'POST':
        model = pickle.load(open('lgr.pkl', 'rb'))
        avg_amount_days = float(request.form['avg_amount_days'])
        transaction_amount = float(request.form['transaction_amount'])
        daily_chbk_avg_amt = float(request.form['daily_chbk_avg_amt'])
        avg_chbk_amt = float(request.form['avg_chbk_amt'])
        chbk_freq = float(request.form['chbk_freq'])

        prediction = model.predict([[avg_amount_days, transaction_amount, daily_chbk_avg_amt, avg_chbk_amt, chbk_freq]])

        # print(prediction)

        if(prediction==0):
            prediction="NOT A FRAUD"
        else:
            prediction="FRAUD"

        return render_template("decision_tree.html", prediction_text="THIS IS {}".format(prediction))
    else:
        return render_template("decision_tree.html")
if __name__ == "__main__":
    app.run(debug=True)