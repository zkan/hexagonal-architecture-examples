from adapters.simple_stock_price_provider import SimpleStockPriceProvider
from adapters.simple_trade_repository import SimpleTradeRepository
from services.trade_service import TradeService


from ports.ports import StockPriceProvider
from ports.ports import TradeRepository


class MyStockPriceProvider(StockPriceProvider):
    def get_price(self, stock_symbol):
        return 99


class MyTradeRepository(TradeRepository):
    def __init__(self):
        self.trades = []

    def save(self, trade):
        self.trades.append(trade)
        return trade

    def get_trades(self):
        return self.trades


def test_service():
    stock_price_provider = MyStockPriceProvider()
    trade_repository = MyTradeRepository()

    trade_service = TradeService(stock_price_provider, trade_repository)

    assert trade_service.get_trades() == []