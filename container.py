import automobile
import truck
import bus
from extenderr import *
import random
#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []
    def file_in(self, strArray):
        arrayLen = len(strArray)
        i = 0  # Индекс, задающий текущую строку в массиве
        figNum = 0
        while i < arrayLen:
            str = strArray[i]
            key = int(str)  # преобразование в целое
            if key == 1:  # признак грузовика
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                car = Truck(strArray[i],strArray[i+1],strArray[i+2])
                i+=3
            elif key == 2:  # признак автобуса
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                car = Bus(strArray[i],strArray[i+1],strArray[i+2])
                i+=3
            elif key == 3:
                i += 1
                if i >= len(strArray) - 1:
                    return 0
                car = Automobile(strArray[i], strArray[i + 1], strArray[i + 2])
                i += 3
            else:
                # что-то пошло не так. Должен быть известный признак
                # Возврат количества прочитанных фигур
                return figNum
            # Количество пробелами фигур увеличивается на 1
            if i == 0:
                return figNum
            figNum += 1
            self.store.append(car)
        return figNum

    def random_in(self, figureNimbers):
        if figureNimbers < 1:
            return False
        for i in range(figureNimbers):
            key = random.randint(1, 3)
            if key == 1:
                car = Truck(random.randint(0, 5000), random.randint(1, 50), random.randint(1, 20))
            elif key == 2:
                car = Bus(random.randint(0, 30), random.randint(1, 50), random.randint(1, 20))
            else:
                car = Automobile(random.randint(0, 200), random.randint(1, 50), random.randint(1, 20))
            self.store.append(car)

    def Print(self):
        print("Container is store", len(self.store), "cars:\n")
        for car in self.store:
            car.Print()
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
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
