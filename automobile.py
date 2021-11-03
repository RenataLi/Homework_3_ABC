#----------------------------------------------
from car import Car


class Automobile(Car):
    def __init__(self, max_speed, fuel_consumption, fuel_capacity):
        super().__init__(fuel_consumption, fuel_capacity)
        self.max_speed = max_speed;

    def Print(self):
        print("Automobile: max_speed = ", self.max_speed, " fuel_consumption = ", self.fuel_consumption, ", fuel_capasity = ", self.fuel_capasity,
              ", Distance = ", super().Distance())
        pass

    def Write(self, ostream):
        ostream.write("Automobile: max_speed = {}  fuel_consumption = {}, fuel_capasity = {}, Distance = {}".
                      format(self.max_speed,self.fuel_consumption,self.fuel_capasity,super().Distance()))

        pass


