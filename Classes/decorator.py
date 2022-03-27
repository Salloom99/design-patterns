class Core:
    def __init__(self, core):
        self.value = core
    
    def print(self):
        print(self.value)

class Decoration(Core):
    def __init__(self, decorated, decoration):
        self.decorated = decorated
        self.value = decoration[0]+decorated.value+decoration[1]


def DecoratorPattern():
    core = Core('salem')
    decorator = Decoration(Decoration(Decoration(Decoration(core,['(',')']),['{','}']),['[',']']),['"','"'])
    print(decorator.value)