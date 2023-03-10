from unittest import TestCase

from converterclass import CurrencyConverter

url1 = 'https://api.exchangerate.host/convert?from=USD&to=USD'
class1 = CurrencyConverter(url1)

url2 = 'https://api.exchangerate.host/convert?from=GBP&to=GBP'
class2 = CurrencyConverter(url2)

url3 = 'https://api.exchangerate.host/convert?from=EUR&to=EUR'
class3 = CurrencyConverter(url3)


class ConverterTestCase(TestCase):
    def setUp(self):
        """Run before all test"""

    def test_currencyconverter(self):
        self.assertEqual(class1.convert(1), 1)
        self.assertEqual(class2.convert(1), 1)
        self.assertEqual(class3.convert(1), 1)
