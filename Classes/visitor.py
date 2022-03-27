class Visitor:
    def __init__(self, form) -> None:
        self.form = form

    def visit(self, element):
        print(self.form,str(element.value))

class Element:
    def __init__(self, value) -> None:
        self.value = value

    def accept(self, visitor):
        visitor.visit(self)


class Data:
    def __init__(self, elements) -> None:
        self.elements = elements
    
    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)

def VisitorPattern():
    data = Data([Element(x) for x in range(1,9)])
    print('One visitor :')
    data.accept(Visitor('value is :'))
    print('Another visitor :')
    data.accept(Visitor('_'))

if __name__ == '__main__':
    VisitorPattern()