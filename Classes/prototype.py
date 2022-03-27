class Vehicle:
    def __init__(self) -> None:
        self.wheels = ''

    def clone(self):
        clonedVehicle = self.__class__()
        clonedVehicle.wheels = self.wheels
        return clonedVehicle

class Car(Vehicle):
    def __init__(self) -> None:
        self.wheels = '4'        

class Motor(Vehicle):
    def __init__(self) -> None:
        self.wheels = '3'

class Bicycle(Vehicle):
    def __init__(self) -> None:
        self.wheels = '2'

class Vehicles:
    def __init__(self) -> None:
        self.car = 'Car'
        self.motor = 'Motor'
        self.bicycle = 'Bicycle'
        self.items = {}
        self.items['Car'] = Car()
        self.items['Motor'] = Motor()
        self.items['Bicycle'] = Bicycle()

    def get(self, type) -> Vehicle:
        return self.items.get(type,None).clone()
        

def PrototypePattern():
    vehicles = Vehicles()
    car = vehicles.get(vehicles.car)
    print('car wheels : ',car.wheels)
    motor = vehicles.get('Motor')
    print('motor wheels : ',motor.wheels)
    bicycle = vehicles.get('Bicycle')
    print('bicycle wheels : ',bicycle.wheels)

    