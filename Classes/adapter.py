class Target:
    def __init__(self) -> None:
        pass

    def specific_func():
        print('old implementation')

class Adapter(Target):
    def __init__(self, adaptee) -> None:
        self.adaptee = adaptee

    def specific_func(self):
        self.adaptee.another_func()

class Adaptee:
    def another_func():
        print('new implementation')

def AdapterPattern():
    adaptee = Adaptee
    adaptee.another_func() # wrong signature right implementation
    something = Target 
    something.specific_func() # you wanna call specific func on something but the implementation of another func
    something = Adapter(Adaptee)
    something.specific_func()