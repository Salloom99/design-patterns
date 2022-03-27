class LGProduct:
    def __init__(self) -> None:
        pass

class LGMonitor(LGProduct):
    def __init__(self) -> None:
        pass

class LGRemote(LGProduct):
    def __init__(self) -> None:
        pass

class SamsungProduct:
    def __init__(self) -> None:
        pass

class SamsungMonitor(SamsungProduct):
    def __init__(self) -> None:
        pass

class SamsungRemote(SamsungProduct):
    def __init__(self) -> None:
        pass

class AbstractFactory:
    def __init__(self, monitor, remote) -> None:
        self.monitor  = monitor
        self.remote = remote

    def get_monitor(self):
        return self.monitor

    def get_remote(self):
        return self.remote

class LGFactory(AbstractFactory):
    def __init__(self) -> None:
        super().__init__(LGMonitor(), LGRemote())

class SamsungFactory(AbstractFactory):
    def __init__(self) -> None:
        super().__init__(SamsungMonitor(), SamsungRemote())

class Client:
    def __init__(self, factory: AbstractFactory) -> None:
        self.factory = factory


def AbstractFactory():
    client = Client(LGFactory())
    print(client.factory.get_monitor())
    print(client.factory.get_remote())
    client = Client(SamsungFactory())
    print(client.factory.get_monitor())
    print(client.factory.get_remote())