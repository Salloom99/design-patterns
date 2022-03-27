import operator

class Parser:
    def __init__(self, expression = None) -> None:
        self.expression = expression

    def parse(self):
        self.expression.nonterminal.parse


class Base:
    def __init__(self) -> None:
        pass

class Terminal(Base):
    def __init__(self, value) -> None:
        self.value = value

    def get_value(self):
        return int(self.value)

class NonTerminal(Base):
    def __init__(self, operator, first_terminal, second_terminal) -> None:
        self.operator = operator
        self.first_terminal = Terminal(first_terminal)
        self.second_terminal = Terminal(second_terminal)

    def get_value(self):
        return eval(f'{self.first_terminal.get_value()}{self.operator}{self.second_terminal.get_value()}')


class Expression:
    def __init__(self, string, parser: Parser) -> None:
        self.string = string
        self.base = NonTerminal(string[1],string[0],string[2])
        self.parser = parser
        self.parser.expression = self

    def get_value(self):
        return self.base.get_value()

def InterpreterPattern():
    expression = Expression('5*3',Parser())
    print(expression.string,end='=')
    print(expression.get_value())