from car import Car


class Truck(Car):
    def __init__(self, lifting_capacity, fuel_consumption, fuel_capacity):
        super().__init__(fuel_consumption, fuel_capacity)
        self.lifting_capacity = lifting_capacity
    def Print(self):
        print("Truck: lifting_capacity = ", self.lifting_capacity, " fuel_consumption = ", self.fuel_consumption, ", fuel_capasity = ", self.fuel_capasity,
              ", Distance = ", super().Distance())
        pass

    def Write(self, ostream):
        ostream.write("Truck: lifting_capacity = {}  fuel_consumption = {}, fuel_capasity = {}, Distance = {}".format(self.lifting_capacity, self.fuel_consumption, self.fuel_capasity,super().Distance()))
        pass
