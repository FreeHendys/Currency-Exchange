from flask import Flask, render_template, request, redirect, flash
from converter import CurrencyConverter
from forms import CurrencyForm
from secret import secretkey

app = Flask(__name__)
app.config['SECRET_KEY'] = secretkey


@app.route('/', methods=["GET", "POST"])
def curr_form():
    """Form to submit currency codes and amount"""
    form = CurrencyForm()
    if form.validate_on_submit():
        from_currency = form.fromcurr.data
        to_currency = form.tocurr.data
        amount = form.amount.data
        converter = CurrencyConverter(from_currency, to_currency)
        results = converter.convert(amount)
        return render_template("converter.html", form=form, result=results)
    else:
        return render_template("converter.html", form=form)
