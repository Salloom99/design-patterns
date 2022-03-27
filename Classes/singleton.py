class OneObject:
    _instance = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = object.__new__(cls,)
        return cls._instance

    def __init__(self, value):
        self.value = value


    def modify(cls, value):
        print('instance modified to '+ value,end=' ')
        cls._instance.value = value

def Singleton():
    a = OneObject('1')
    print('a instance : ' + a.value)
    b = OneObject('2')
    print('b instance : ' + b.value)
    a.modify('3'), print(' a modified')
    print('a instance : ' + a.value)
    print('b instance : ' + b.value)
    b.modify('4'), print(' b modified')
    print('a instance : ' + a.value)
    print('b instance : ' + b.value)
