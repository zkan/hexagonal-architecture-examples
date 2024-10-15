import random

from ports.ports import StockPriceProvider


class SimpleStockPriceProvider(StockPriceProvider):
    def get_price(self, stock_symbol):
        price = random.randint(100, 500)
        return price
