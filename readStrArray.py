from extenderr import *


def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0  # Индекс, задающий текущую строку в массиве
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)  # преобразование в целое
        # print("key = ", key)
        if key == 1:  # признак грузовика
            i += 1
            shape = Truck()
            i = shape.ReadStrArray(strArray,i)  # чтение прямоугольника с возвратом позиции за ним
        elif key == 2:  # признак автобуса
            i += 1
            shape = Bus()
            i = shape.ReadStrArray(strArray, i)  # чтение треугольника с возвратом позиции за ним
        elif key == 3:
            i += 1
            shape = Automobile()
            i = shape.ReadStrArray(strArray, i)
        else:
            # что-то пошло не так. Должен быть известный признак
            # Возврат количества прочитанных фигур
            return figNum
         # Количество пробелами фигур увеличивается на 1
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(shape)
    return figNum
