import json
import requests


class CurrencyConverter:

    def __init__(self, url):
        response = requests.get(url)
        data = response.json()

        self.data = data
        self.rate = self.data['result']
        self.date = self.data['date']
        self.currcodelist = list(self.data['query'].values())
        self.fromcurr = self.currcodelist[0]
        self.tocurr = self.currcodelist[1]

    def convert(self, from_amount):
        num = from_amount.replace(",", "")
        val = int(float(num))
        if self.rate is None:
            return "Please enter a valid currency code"
        elif val >= 0:
            to_amount = val * self.rate
            result = round(to_amount, 2)
            return f"{num} {self.fromcurr} converts to {result} {self.tocurr} as of {self.date}"
        else:
            return "Please enter a valid number 0 or above"
