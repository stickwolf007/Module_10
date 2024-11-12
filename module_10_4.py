import random
import time
from threading import Thread
from queue import Queue


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):  #
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(random.randint(3, 10))
        print(f"{self.name} покушал(-а) и ушёл(ушла)")


class Cafe:
    def __init__(self, *tables_):
        self.queue = Queue()
        self.tables = tables_

    def guest_arrival(self, *guests_1):
        for guest in guests_1:
            assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    guest.start()
                    assigned = True
                    break

            if not assigned:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def manage_guests(self):
        while not self.queue.empty() or any(table.guest for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None


                    if not self.queue.empty():
                        next_guest = self.queue.get()
                        table.guest = next_guest
                        print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        next_guest.start()

            time.sleep(0.5)



tables = [Table(number) for number in range(1, 6)]


guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]


guests = [Guest(name) for name in guests_names]


cafe = Cafe(*tables)

cafe.guest_arrival(*guests)


cafe.manage_guests()