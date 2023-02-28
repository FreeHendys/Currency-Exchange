from flask import Flask, render_template, request, redirect, flash
from converterclass import CurrencyConverter
import requests
import urllib.request
import json
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def curr_convert():
    if request.method == "POST":
        from_amount = request.form['from_amount']
        fromcurr = request.form['fromcurrcode']
        tocurr = request.form['tocurrcode']
        url = f'https://api.exchangerate.host/convert?from={fromcurr}&to={tocurr}'
        converter = CurrencyConverter(url)
        results = converter.convert(from_amount)
        return render_template("converter.html", result=results)
    else:
        return render_template("converter.html")
