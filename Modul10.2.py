from threading import Thread
import time


class Knight(Thread):
    total_enemies = 100
    days = 0

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.total_enemies > 0:
            self.total_enemies = self.total_enemies - self.power
            time.sleep(1)
            self.days += 1
            print(f"{self.name} сражается {self.days} дней(дня)..., осталось {self.total_enemies} воинов.\n")
        print(f'{self.name} одержал победу спустя {self.days} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
