from adapters.simple_trade_repository import SimpleTradeRepository
from domains.trade import Trade


def test_trade_save():
    trade = Trade(stock_symbol="AAPL", quantity=10, price=200)

    trade_repository = SimpleTradeRepository()
    saved_trade = trade_repository.save(trade)

    assert saved_trade.stock_symbol == trade.stock_symbol
    assert saved_trade.quantity == trade.quantity
    assert saved_trade.price == trade.price
    assert saved_trade.status == trade.status
