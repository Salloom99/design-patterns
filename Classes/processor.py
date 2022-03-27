
class Processor:
    def __init__(self, id):
        self.id = id

class Chain:

    def __init__(self, *processors):
        self.processor = processors[0]
        prevProcessor = processors[0]
        for currProcessor in processors[1:]:
            prevProcessor.processor = currProcessor
            prevProcessor = currProcessor
        return

    def process(self, arg):
        self.processor.process(arg)


class AfterProcessor(Processor):
    def __init__(self, id, processor = None):
        super().__init__(id)
        self.processor = processor

    def process(self, arg):
        if self.processor != None:
            self.processor.process(arg)
        print(self.id + ' : processing after : ' +arg +'\n')


class BeforeProcessor(Processor):
    def __init__(self, id,processor = None):
        super().__init__(id)
        self.processor = processor

    def process(self, arg):
        print(self.id + ' : processing before : ' +arg+'\n')
        if self.processor != None:
            self.processor.process(arg)

def ChainOfResponsibilityPattern():
    print('Chain of responsibility : ')

    processor = Chain(BeforeProcessor('1b'),AfterProcessor('1a'),AfterProcessor('2a'),BeforeProcessor('2b'),AfterProcessor('3a'))
    processor.process('Salem')

    print(' ')