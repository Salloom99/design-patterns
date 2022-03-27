class Abstraction:
    def __init__(self) -> None:
        pass

    def function(self):
        pass


class Implementation:
    def __init__(self, abstraction: Abstraction) -> None:
        self.abstraction = abstraction

    def function(self):
        self.abstraction.function()
    

class Abstraction1(Abstraction):
    def __init__(self) -> None:
        super().__init__()
    
    def function(self):
        print('calling func from abstraction 1')



class Abstraction2(Abstraction):
    def __init__(self) -> None:
        super().__init__()

    def function(self):
        print('calling func from abstraction 2')


class Implementation1(Implementation):
    def __init__(self, abstraction) -> None:
        super().__init__(abstraction)

    def function(self):
        self.abstraction.function()
        print('__and refining calling func from implementation 1')

class Implementation2(Implementation):
    def __init__(self, abstraction) -> None:
        super().__init__(abstraction)

    def function(self):
        self.abstraction.function()
        print('__and refining calling func from implementation 2')


def BridgePattern():
    obj1 = Implementation1(Abstraction2())
    obj2 = Implementation2(Abstraction1())

    print('obj1 : ')
    obj1.function()
    print('obj2 : ')
    obj2.function()