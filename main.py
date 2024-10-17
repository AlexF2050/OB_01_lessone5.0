class Warrior(): # Класс персонажа
    def __init__(self, name, power, endurance, hair_color): #конструктор класса Warrior с параметрами name, power, hair_color
        self.name = name # имя персонажа
        self.power = power # уровень силы персонажа
        self.endurance = endurance # уровень силы персонажа
        self.hair_color = hair_color # цвет волос

    def sleep(self):
        print(f"{self.name} лёг отдохнуть") # выводим сообщение
        self.endurance += 2# увеличиваем уровень силы персонажа на 2

    def eat(self):
        print(f"{self.name} сел кушать") # выводим сообщение
        self.power += 1

    def nit(self):
        print(f"{self.name} спасает кого-то") # выводим сообщение
        self.endurance -= 6# уменьшаем уровень силы персонажа на 6

    def walk(self):
        print(f"{self.name} гуляет") # выводим сообщение

    def info(self):
        print(f"имя воина - {self.name}") # выводим сообщение
        print(f"цвет волос воина - {self.hair_color}") # выводим сообщение
        print(f"сила воина  - {self.power}") # выводим сообщение
        print(f"выносливость воина  - {self.endurance}")  # выводим сообщение