import os
from time import sleep
os.system("clear")

class Kettle():
    def turn_on(self):
        for i in range(1, 20):
            if i == 2:
                self.__boil()
            elif i == 4:
                self.__check_temperature()
            elif i == 6:
                self.__beep()
            elif i == 8:
                self._turn_off()
            sleep(2)

    def __boil(self):
        print("Разогревание воды")

    def __check_temperature(self):
        print("Проверяем температуру воды")

    def __beep(self):
        print("Подаем звуковой сигнал")

    def _turn_off(self):
        print("Автоматическое отключение")

my_kettle = Kettle()
my_kettle.turn_on() 

