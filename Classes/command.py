class Receiver:
    def __init__(self, state):
        self.state = state

    def excute(self, command):
        self.state = 'my state is '+ command

class Sender:
    def __init__(self, receiver, commands):
        self.receiver = receiver
        self.commands = commands

    def send(self, command):
        self.commands[command].do(self.receiver)

    def undoSend(self, command):
        self.commands[command].undo(self.receiver)

class Command:
    def __init__(self):
        pass

    def do(receiver):
        receiver.excute('on')

    def undo(receiver):
        receiver.excute('off')

def CommandPattern():
    receiver = Receiver(' ')
    controller = Sender(receiver, [Command,Command,Command])
    controller.send(0)
    print(receiver.state)
    controller.undoSend(0)
    print(receiver.state)