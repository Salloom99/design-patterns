class Builder:
    def __init__(self) -> None:
        self.building = None

    def construct_basement(self):
        self.building.floors += 1
        print('constructing basement of ',self.building)
    
    def construct_floors(self, roofs):
        self.building.floors += roofs
        print(f'constructing {roofs} floors of ',self.building)

    def construct_roof(self):
        self.building.floors += 1
        print('constructing roof of ',self.building)


class Building:
    def __init__(self) -> None:
        self.floors = 0

class Building1(Building):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return 'building1'

class Building2(Building):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return 'building2'

class Building3(Building):
    def __init__(self) -> None:
        super().__init__()
    
    def __str__(self) -> str:
        return 'building3'


class Director:
    def __init__(self, builder) -> None:
        self.builder = builder

    def createBuilding1(self) -> Building1:
        building = Building1()
        self.builder.building = building
        self.builder.construct_basement()
        self.builder.construct_floors(3)
        self.builder.construct_roof()
        return building

    def createBuilding2(self) -> Building2:
        building = Building2()
        self.builder.building = building
        self.builder.construct_floors(4)
        self.builder.construct_roof()
        self.builder.construct_basement()
        return building

    def createBuilding3(self) -> Building3:
        building = Building3()
        self.builder.building = building
        self.builder.construct_roof()
        self.builder.construct_floors(5)
        self.builder.construct_basement()
        return building

def BuilderPattern():
    director = Director(Builder())
    building = director.createBuilding1()
    print('building1 roofs : ',str(building.floors))
    print('---------------------------------------')
    building = director.createBuilding2()
    print('building2 roofs : ',str(building.floors))
    print('---------------------------------------')
    building = director.createBuilding3()
    print('building3 roofs : ',str(building.floors))

