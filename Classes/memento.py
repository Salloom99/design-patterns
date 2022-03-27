class Memento:
    def __init__(self, type, size, color) -> None:
        self.type = type
        self.size = size
        self.color = color

class History:
    def __init__(self) -> None:
        self.mementos = []


class Shape:
    def __init__(self, history: History, type, size, color) -> None:
        self.type = type
        self.size = size
        self.color = color
        self.history = history
        self.history.mementos.append(self)
        print('shape has been created')

    def change(self, type, size, color):
        self.type = type
        self.size = size
        self.color = color

    def save(self):
        memento = Memento(self.type,self.size,self.color)
        self.history.mementos.append(memento)
        print('shape has been saved')

    def restore(self):
        try:
            memento = self.history.mementos.pop()
            if self == memento:
                memento = self.history.mementos.pop()
            self.type = memento.type
            self.size = memento.size
            self.color = memento.color
            print('shape has been restored')
        except IndexError:
            print('no more undos')

    def __str__(self):
        return f'a {self.type} with size of {self.size} has a color of {self.color}'

    def __eq__(self, memento: Memento) -> bool:
        return self.type == memento.type and self.size == memento.size and self.color == memento.color


def MementoPattern():
    shape = Shape(History(),'Circle',10,'red')
    print('---------------------------------')
    shape.save()
    print('---------------------------------')
    print(shape)
    print('---------------------------------')
    shape.change('Square',5,'blue')
    shape.save()
    print('---------------------------------')
    print(shape)
    print('---------------------------------')
    shape.change('Triangle',3,'green')
    shape.save()
    print('---------------------------------')
    print(shape)
    print('---------------------------------')
    shape.restore()
    print('---------------------------------')
    print(shape)
    print('---------------------------------')
    shape.restore()
    print('---------------------------------')
    print(shape)
    print('---------------------------------')
    