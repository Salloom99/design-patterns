class PcsCreator:
    def __init__(self):
        self.pcs = {}

    def get_pc(self, cpu, gpu):
        id = cpu + gpu
        return self.pcs.get(id)
    
    def is_new_pc(self,cpu,gpu) -> bool:
        id = cpu + gpu
        return self.pcs.get(id) == None

    def add_new_pc(self, pc):
        id = pc.cpu + pc.gpu
        self.pcs[id] = pc

    def remove_old_pc(self, pc):
        id = pc.cpu + pc.gpu
        self.pcs.pop(id)


class PC():
    pcs_creator = PcsCreator()

    def __init__(self,cpu, gpu) -> None:
        self.id = object.__new__(PC)
        self.cpu = cpu
        self.gpu = gpu

    def __new__(cls, cpu, gpu):
        if cls.pcs_creator.is_new_pc(cpu, gpu):
            instance = super(PC,cls).__new__(cls)
            instance.id = object.__new__(PC)
            instance.cpu = cpu
            instance.gpu = gpu
            cls.pcs_creator.add_new_pc(instance)
            print('creating new instance')
            return instance
        else:
            print('using old instance')
            return cls.pcs_creator.get_pc(cpu, gpu)
    
    def __del__(self):
        print(self.id)
        # PC.pcs_creator.remove_old_pc(self)



   


def FlyweightPattern():
    pc = PC('ryzen','amd')
    print(pc.id)
    pc = PC('ryzen','amd')
    print(pc.id)
    pc = PC('ryzen','rtx')
    print(pc.id)
    pc = PC('intel','rtx')
    print(pc.id)
    pc = PC('intel','rtx')
    print(pc.id)


