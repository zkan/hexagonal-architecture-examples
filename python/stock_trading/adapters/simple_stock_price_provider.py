from ports.ports import StockPriceProvider


class SimpleStockPriceProvider(StockPriceProvider):
    def get_price(self, stock_symbol):
        return 100.0
