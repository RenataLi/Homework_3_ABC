
class Car:
    def __init__(self,fuel_capasity, fuel_consumption):
        self.fuel_consumption = fuel_consumption;
        self.fuel_capasity = fuel_capasity;

    def Distance(self):
        return int(self.fuel_capasity)/int(self.fuel_consumption)
    pass