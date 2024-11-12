
import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            deposit_1 = random.randint(50, 500)
            with self.lock:
                self.balance += deposit_1
                print(f"\rПополнение: {deposit_1}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            take_1 = random.randint(50, 500)
            print(f"\rЗапрос на {take_1}")
            with self.lock:
                if take_1 > self.balance:
                    print("Запрос отклонён, недостаточно средств")
                else:
                    self.balance -= take_1
                    print(f"Снятие: {take_1}. Баланс: {self.balance}")
            time.sleep(0.001)


# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
