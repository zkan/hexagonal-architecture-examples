from adapters.simple_stock_price_provider import SimpleStockPriceProvider
from adapters.simple_trade_repository import SimpleTradeRepository
from services.trade_service import TradeService


if __name__ == "__main__":
    stock_price_provider = SimpleStockPriceProvider()
    trade_repository = SimpleTradeRepository()

    trade_service = TradeService(stock_price_provider, trade_repository)

    trade = trade_service.place_trade(stock_symbol="AAPL", quantity=30)

    print(f"Trade status: {trade.status}")
