import threading
from time import sleep


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        bad = 100
        print(self.name + ', на нас напали!')
        day = 0
        while bad > 0:
            sleep(10)
            bad -= self.power
            if bad < 0:
                bad = 0
            day += 1
            print(f'{self.name} сражается {day} день(дня)..., осталось {bad} воинов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 20)
second_knight = Knight("Sir Galahad", 30)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')
