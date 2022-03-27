class A:
    def __init__(self, value) -> None:
        self.value = value
        self.b = None

    def __str__(self):
        return f'a{self.value}'


class B:
    def __init__(self, list_of_a, value) -> None:
        self.value = value
        self.list_of_a = list_of_a
        self.t = None

    def link_to_a(self):
        for a in self.list_of_a:
            a.b = self

    def __str__(self):
        return f'b{self.value}'

class T:
    def __init__(self, a, b, value) -> None:
        self.value = value
        self.a = a
        self.b = b

    def link_to_b(self):
        self.b.t = self

    def __str__(self):
        return f't{self.value}'

class Facade_T:
    def __init__(self) -> None:
        self.t = None

    def create_T(self) -> T:
        a = A(0)
        b = B([A(num) for num in range(1,6)],0)
        b.link_to_a()
        t = T(a,b,0)
        t.link_to_b()
        self.t = t
        return t

    def print_T(self):
        print(self.t,'linked to',self.t.b,'linked to',self.t.a)
        print(self.t.b,'linked to',self.t.b.t)
        print(self.t.b,'has',end=' ')
        for a in self.t.b.list_of_a:
            print(a,end=',')


def FacadePattern():
    facade = Facade_T()
    t = facade.create_T()
    facade.print_T()


