class Truck:
    def __init__(self):
        self.lifting_capacity = 0;
        self.fuel_consumption = 0
        self.fuel_capasity = 0;
    def ReadStrArray(self,strArray,i):
        # должно быт как минимум два непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        self.lifting_capacity = int(strArray[i])
        self.fuel_capasity = int(strArray[i + 1])
        self.fuel_consumption = int(strArray[i + 2])
        i += 3
        # print("Rectangle: x = ", self.x, " y = ", self.y)
        return i

    def Print(self):
        print("Truck: lifting_capacity = ", self.lifting_capacity, " fuel_consumption = ", self.fuel_consumption, ", fuel_capasity = ", self.fuel_capasity,
              ", Distance = ", self.Distance())
        pass

    def Write(self, ostream):
        ostream.write("Truck: lifting_capacity = {}  fuel_consumption = {}, fuel_capasity = {}, Distance = {}".format(self.lifting_capacity, self.fuel_consumption, self.fuel_capasity,self.Distance()))
        pass

    def Distance(self):
        return self.fuel_capasity / self.fuel_consumption
        pass