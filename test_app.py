from unittest import TestCase
from datetime import date
from app import app
from converter import CurrencyConverter

url1 = 'https://api.exchangerate.host/convert?from=USD&to=USD'
class1 = CurrencyConverter(url1)

url2 = 'https://api.exchangerate.host/convert?from=GBP&to=GBP'
class2 = CurrencyConverter(url2)

url3 = 'https://api.exchangerate.host/convert?from=EUR&to=EUR'
class3 = CurrencyConverter(url3)

today = date.today()


class ConverterTestCase(TestCase):
    def test_currencyconverter(self):
        """Test to check inputs off all values such as Amount, From Currency, To Currency"""
        self.assertEqual(class1.convert(
            "1"), f'1 USD converts to 1 USD as of {today}')
        self.assertEqual(class2.convert(
            "1"), f'1 GBP converts to 1 GBP as of {today}')
        self.assertEqual(class3.convert(
            "1"), f'1 EUR converts to 1 EUR as of {today}')

    def test_currency_form(self):
        with app.test_client() as client:
            res = client.post(
                '/', data={'from_amount': "1", "fromcurrcode": "USD", "tocurrcode": "USD"})
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn(
                f'<p> 1 USD converts to 1 USD as of {today} </p>', html)
