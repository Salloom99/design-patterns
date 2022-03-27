class State:
    def __init__(self, value) -> None:
        self.value = value

    def do(self):
        pass


class OffState(State):
    def do(self):
        print('I cant do anything')


class OnState(State):
    def do(self):
        print("I'm doing my thing")


class Thing:
    def __init__(self, init_state) -> None:
        self.state = init_state

    def change_state(self, new_state):
        self.state = new_state
        print('my state has been changed')

    def do(self):
        self.state.do()

    def print_state(self):
        print(self.state.value)

def StatePattern():
    thing = Thing(OffState('off'))
    thing.do()
    thing.change_state(OnState('on'))
    thing.do()