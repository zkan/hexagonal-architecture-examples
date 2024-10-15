from domains.trade import Trade


def test_trade_defaults():
    trade = Trade(stock_symbol="AAPL", quantity=10, price=200)

    assert trade.stock_symbol == "AAPL"
    assert trade.quantity == 10
    assert trade.price == 200
    assert trade.status == "Pending"
