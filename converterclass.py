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
        if val >= 0 and self.fromcurr in currencycodes and self.tocurr in currencycodes:
            to_amount = val * self.rate
            result = round(to_amount, 2)
            return f"{num} {self.fromcurr} converts to {result} {self.tocurr} as of {self.date}"
        elif self.fromcurr not in currencycodes or self.tocurr not in currencycodes:
            return "Please enter a valid currency code"
        else:
            return "Please enter a valid number 0 or above"


currencycodes = ["AED",
                 "AFN",
                 "ALL",
                 "AMD",
                 "ANG",
                 "AOA",
                 "ARS",
                 "AUD",
                 "AWG",
                 "AZN",
                 "BAM",
                 "BBD",
                 "BDT",
                 "BGN",
                 "BHD",
                 "BND",
                 "BOB",
                 "BRL",
                 "BSD",
                 "BTN",
                 "BWP",
                 "BYR",
                 "BZD",
                 "CAD",
                 "CHF",
                 "CLP",
                 "CNY",
                 "COP",
                 "CRC",
                 "CZK",
                 "DKK",
                 "DOP",
                 "DZD",
                 "EGP",
                 "ETB",
                 "EUR",
                 "FJD",
                 "GBP",
                 "GEL",
                 "GHS",
                 "GMD",
                 "GTQ",
                 "GYD",
                 "HKD",
                 "HNL",
                 "HRK",
                 "HUF",
                 "IDR",
                 "ILS",
                 "INR",
                 "ISK",
                 "JEP",
                 "JMD",
                 "JOD",
                 "JPY",
                 "KES",
                 "KGS",
                 "KHR",
                 "KRW",
                 "KWD",
                 "KYD",
                 "KZT",
                 "LBP",
                 "LKR",
                 "LTL",
                 "LVL",
                 "MAD",
                 "MDL",
                 "MGA",
                 "MKD",
                 "MMK",
                 "MNT",
                 "MOP",
                 "MUR",
                 "MVR",
                 "MXN",
                 "MYR",
                 "MZN",
                 "NAD",
                 "NGN",
                 "NIO",
                 "NOK",
                 "NPR",
                 "NZD",
                 "OMR",
                 "PEN",
                 "PGK",
                 "PHP",
                 "PKR",
                 "PLN",
                 "PYG",
                 "QAR",
                 "RON",
                 "RSD",
                 "RUB",
                 "RWF",
                 "SAR",
                 "SCR",
                 "SEK",
                 "SGD",
                 "STD",
                 "SYP",
                 "THB",
                 "TND",
                 "TRY",
                 "TTD",
                 "TWD",
                 "TZS",
                 "UAH",
                 "UGX",
                 "USD",
                 "UYU",
                 "VEF",
                 "VND",
                 "VUV",
                 "WST",
                 "XAF",
                 "XBT",
                 "XCD",
                 "XOF",
                 "XPF",
                 "ZAR",
                 "ZMW",]
