from queue import Queue

class BacktestEngine:
    def __init__(self, data_handler, strategy, portfolio, broker):
        self.events = Queue()
        self.data_handler = data_handler
        self.strategy = strategy
        self.portfolio = portfolio
        self.broker = broker

    def run(self):
        while self.data_handler.has_next():
            market_event = self.data_handler.next()
            self.strategy.on_event(market_event)

            while not self.events.empty():
                event = self.events.get()
                self._process_event(event)

    def _process_event(self, event):
        pass
