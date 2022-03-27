class Iterator:
    def __init__(self, iterable) -> None:
        self.iterable = iterable
        self.index = 0

    def get_next(self):
        item = self.iterable.list[self.index]
        self.index+= 1
        return item

    def has_next(self) -> bool:
        return self.index < len(self.iterable.list)

class Iterable:
    def __init__(self, list) -> None:
        self.list = list

    def get_iterator(self) -> Iterator:
        return Iterator(self)


def IteratorPattern():
    iterable = Iterable(['1','2','3','4','5','6','7','8','9'])
    iterator = iterable.get_iterator()
    while(iterator.has_next()):
        print(iterator.get_next())


        