class Thing:
    def __init__(self) -> None:
        pass

    def func_1(self):
        pass

    def func_2(self):
        pass

    def final_func(self):
        print('doing things first')
        self.func_1()
        print('doing things then')
        self.func_2()
        print('doing things last')

class ThingA(Thing):
    def __init__(self) -> None:
        super().__init__()
    
    def func_1(self):
        print('calling func1 from A')

    def func_2(self):
        print('calling func2 from A')

class ThingB(Thing):
    def __init__(self) -> None:
        super().__init__()
    
    def func_1(self):
        print('calling func1 from B')

    def func_2(self):
        print('calling func2 from B')


def TemplateMethodPattern():
    print('thing A')
    thing = ThingA()
    thing.final_func()
    print('---------------')
    print('thing B')
    thing = ThingB()
    thing.final_func()