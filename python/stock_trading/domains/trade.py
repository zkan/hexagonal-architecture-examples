class Trade:
    def __init__(self, stock_symbol, quantity, price):
        self.stock_symbol = stock_symbol
        self.quantity = quantity
        self.price = price
        self.status = "Pending"

    def __str__(self):
        return f"{self.stock_symbol} | {self.quantity} | {self.price} | {self.status}"

    def execute(self):
        self.status = "Executed"
        return f"Executed trade for {self.quantity} shares of {self.stock_symbol} at ${self.price}"
