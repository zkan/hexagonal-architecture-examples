from ports.ports import TradeRepository


class SimpleTradeRepository(TradeRepository):
    def __init__(self):
        self.trades = []

    def save(self, trade):
        self.trades.append(trade)
        print(f"Trade saved: {trade.stock_symbol}, {trade.quantity} shares at ${trade.price}")
