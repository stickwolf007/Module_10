import threading
import time

total_enemies = 100


class Knight(threading.Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = total_enemies
        self.victory = False

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power
            if self.enemies < 0:
                self.enemies = 0
            print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов. \n")
        self.victory = True
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")