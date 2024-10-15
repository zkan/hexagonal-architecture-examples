from domains.trade import Trade


class TradeService:
    def __init__(self, price_provider, trade_repository):
        self.price_provider = price_provider
        self.trade_repository = trade_repository

    def place_trade(self, stock_symbol, quantity):
        price = self.price_provider.get_price(stock_symbol)
        trade = Trade(stock_symbol, quantity, price)
        trade.execute()
        self.trade_repository.save(trade)
        return trade
