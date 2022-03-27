class Observer:
    def __init__(self, id):
        self.id = id

    def notify(self):
        print(self.id + ' notified')

class Observable:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyAll(self):
        for observer in self.observers:
            observer.notify()

def ObserverPattern():
    print('Observer : ')

    observable = Observable()
    observable.addObserver(Observer('1st'))
    observable.addObserver(Observer('2nd'))
    observable.addObserver(Observer('3rd'))
    observable.notifyAll()

if __name__ == '__main__':
    ObserverPattern()