class Stream:
    def __init__(self, data =None) -> None:
        self.data = data

    def get_data(self):
        print(self.data)

class RealStream(Stream):
    def __init__(self) -> None:
        super().__init__(data='A HUGE SIZED DATA..!!')
        print('data created')
        

class ProxyStream(Stream):
    def get_data(self):
        self.real_stream = RealStream()
        self.real_stream.get_data()

    data = property(get_data)


def ProxyPattern():
    stream = RealStream()
    print('I didnt call get data on first yet')
    stream.get_data()
    another_stream = ProxyStream()
    print('I didnt call get data on second stream yet')
    another_stream.get_data()
