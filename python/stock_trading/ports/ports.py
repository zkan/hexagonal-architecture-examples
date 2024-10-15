from abc import ABC, abstractmethod


class StockPriceProvider(ABC):
    @abstractmethod
    def get_price(self, stock_symbol):
        raise NotImplementedError


class TradeRepository(ABC):
    @abstractmethod
    def save(self, trade):
        raise NotImplementedError
