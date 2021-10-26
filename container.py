import automobile
import truck
import bus

#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    #def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "cars:")
        for car in self.store:
            car.Print()
        self.Sort()
        print("Sorted container:\n")
        for car in self.store:
            car.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for car in self.store:
            car.Write(ostream)
            ostream.write("\n")
        self.Sort()
        ostream.write("Sorted container:\n")
        for car in self.store:
            car.Write(ostream)
            ostream.write("\n")
        pass

    def Sort(self):
        size = len(self.store)
        #временная переменная для обмена элементов местами
        # Сортировка  массива  пузырьком
        for i in range(size - 1):
            for j in range(size-i-1):
                if self.store[j].Distance() > self.store[j+1].Distance():
                    tmp = self.store[j]
                    self.store[j] = self.store[j+1]
                    self.store[j+1] = tmp
