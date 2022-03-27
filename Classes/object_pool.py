class Thing:
    def __init__(self, id) -> None:
        self.id = id

class Pool:
    def __init__(self, size) -> None:
        self.size = size
        self.things = [Thing(i) for i in range(size)]
        self.index = 0

    def get_thing(self):
        thing = self.things[self.index]
        if self.index < self.size - 1:
            self.index += 1
        else:
            self.index = 0
        return thing

def ObjectPoolPattern(num):
    pool = Pool(3)
    for _ in range(10):
        print(str(pool.get_thing().id))