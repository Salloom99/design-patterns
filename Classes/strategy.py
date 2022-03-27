class Strategy:
    def __init__(self) -> None:
        pass

    def do():
        pass

class Something:
    def __init__(self, strategy) -> None:
        self.strategy = strategy
    
    def do(self):
        self.strategy.do()

    def alter_strategy(self, strategy):
        self.strategy = strategy

class FstStrategy(Strategy):
    def do():
        print('1st strategy')

class SndStrategy(Strategy):
    def do():
        print('2nd strategy')

def StrategyPattern():
    something = Something(FstStrategy)
    something.do()
    something.alter_strategy(SndStrategy)
    something.do()