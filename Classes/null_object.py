class Thing:
    def __init__(self) -> None:
        pass

    def do(self):
        pass

class ThingA(Thing):
    def __init__(self) -> None:
        super().__init__()

    def do(self):
        print("I'm thing_a and I'm doing what thing_a should do")

class ThingB(Thing):
    def __init__(self) -> None:
        super().__init__()

    def do(self):
        print("I'm thing_b and I'm doing what thing_b should do")

class NOthing(Thing):
    def __init__(self) -> None:
        super().__init__()

    def do(self):
        print("I'm nothing and I'm doing nothing")

def NullObjectPattern():
    thing = ThingA()
    thing.do()
    thing = ThingB()
    thing.do()
    thing = NOthing()
    thing.do()

