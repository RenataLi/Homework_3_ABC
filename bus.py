from car import Car


class Bus(Car):
    def __init__(self, passenger_capacity, fuel_consumption, fuel_capacity):
        super().__init__(fuel_consumption, fuel_capacity)
        self.passenger_capacity = passenger_capacity
    def Print(self):
        print("Bus: passenger_capacity = ", self.passenger_capacity, " fuel_consumption = ", self.fuel_consumption,
              ", fuel_capasity = ", self.fuel_capasity,", Distance = ", super().Distance())
        pass

    def Write(self, ostream):
        ostream.write("Bus: passenger_capacity = {}  fuel_consumption = {}, fuel_capasity = {}, Distance = {}".format(
                self.passenger_capacity, self.fuel_consumption, self.fuel_capasity,super().Distance()))
        pass

