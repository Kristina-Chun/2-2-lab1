
import doctest


class Car:
    def __init__(self, color: str, max_gas_tank_volume: float, current_gas_tank_volume: float, max_speed: int):
        '''
        создание и подготовка к работе объекта "Машина"

        :param color: цвет машины
        :param max_gas_tank_volume: максимальный объём бензобака
        :param current_gas_tank_volume:  текущий объём бензобака
        :param max_speed: максимальная скорость км/ч

        Примеры
        >>> car = Car('green', 50.7, 45.5, 180)
        '''
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть типом str")
        self.color = color
        if not isinstance(max_gas_tank_volume, (int, float)):
            raise TypeError("Объём бензобака должен быть типа int или float")
        self.max_gas_tank_volume = max_gas_tank_volume
        if not isinstance(current_gas_tank_volume, (int, float)):
            raise TypeError("Текущий объём бензобака должен быть типа int или float")
        if current_gas_tank_volume > max_gas_tank_volume:
            raise TypeError("Текущий объём бензобака не может превышать максимальный объём")
        self.current_gas_tank_volume = current_gas_tank_volume
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Объём бензобака должен быть типа int или float")
        self.max_speed = max_speed

    def gas_tank_is_empty(self) -> bool:
        '''
        функция которая проверяет является ли бензобак пустым

        :return: Является ли бензобак пустым

        Примеры:
        >>> car = Car('green', 50.7, 45.5, 180)
        >>> car.gas_tank_is_empty()
        '''

    def crash_by_pole(self) -> bool:
        '''
        Функцию которая позволяет уйти в закат

        :return: Успешно ли разбита машина

        Примеры:
        >>> car = Car('green', 50.7, 45.5, 180)
        >>> car.crash_by_pole()
        '''


class SmartPhone:
    def __init__(self, brand: str, year_of_release: int):
        '''
        Создание и подготовка к работе объекта "Телефон"

        :param brand: бренд телефона
        :param year_of_release:  год выпуска

        Примеры:
        >>> myPhone = SmartPhone('apple', 2019)
        '''
        if not isinstance(brand, str):
            raise TypeError("Тип бренда должен быть str")
        self.brand = brand
        if not isinstance(year_of_release, int):
            raise  TypeError("Тип года должен быть int")
        if year_of_release < 2000:
            raise ValueError("Год должен быть не меньше 2000")
        self.year_of_release = year_of_release

    def call(self, target_phone_number: str) -> bool:
        '''
        Функция звонка на указанный номер

        :param target_phone_number: целевой номер звонка
        :return: успешность дозвона

        Примеры:
        >>> myPhone = SmartPhone('apple', 2019)
        >>> myPhone = myPhone.call('123456')
        '''

    def check_network(self) -> bool:
        '''
        Функция проверяет наличие сети

        :return: результат - успешный - True или не успешный - False

        Примеры:
        >>> myPhone = SmartPhone('apple', 2019)
        >>> myPhone.check_network()
        '''


class Point:
    def __init__(self, x: float, y: float):
        '''
        Создание и подготовка объекта "Точка на плоскости"

        :param x: координата икс
        :param y: координата игрек

        Примеры:
        >>> point = Point(1, 2.5)
        '''
        if not isinstance(x, (float, int)):
            raise TypeError("Координата X должна быть типа int или float")
        self.x = x
        if not isinstance(y, (float, int)):
            raise TypeError("Координата Y должна быть типа int или float")
        self.y = y

    def count_vector_length(self) -> float:
        '''
        Функция вычисления длины вектора (0, 0) (x, y)

        :return: длина вектора

        Примеры:
        >>> point = Point(1, 3.7)
        >>> point.count_vector_length()
        '''

    def change_coordinates(self, x: float, y: float):
        '''
        функция смены координат точки

        :param x: новая координата x
        :param y: новая кордината y

        :return:

        Примеры:
        >>> point = Point(3.75, 6.32)
        >>> point.change_coordinates(2, 3)
        '''


if __name__ == "__main__":
    doctest.testmod()
