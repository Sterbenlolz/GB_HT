import time

class TrafficLight():
    def running(self):
        while True:
            self.__color = 'Красный'
            print('Загорелся {} свет!'.format(self.__color.casefold()))
            time.sleep(7)
            self.__color = 'Желтый'
            print('Загорелся {} свет!'.format(self.__color.casefold()))
            time.sleep(2)
            self.__color = 'Зеленый'
            print('Загорелся {} свет!'.format(self.__color.casefold()))
            time.sleep(9)
            self.__color = 'Желтый'
            print('Загорелся {} свет!'.format(self.__color.casefold()))
            time.sleep(2)

TrafficLight().running()