class Warrior(): # Класс персонажа
    def __init__(self, name, power, endurance, hair_color): #конструктор класса Warrior с параметрами name, power, hair_color
        self.name = name # имя персонажа = характеристика
        self.power = power # уровень энергии силы' персонажа = характеристика
        self.endurance = endurance # уровень выносливости' персонажа= характеристика
        self.hair_color = hair_color # цвет волос = характеристика
#Методы класса Warrior
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
# Создаём Объект для класса Warrior_____________________________________________________________________________________
war1 = Warrior("ZeroBot", 88, 77, "черно-серебристый") # создаём объект класса Warrior
war2 = Warrior("NeroBaz", 55, 95, "белый") # создаём объект класса Warrior

print(war2.name) # выводим сообщение
print(war2.power) # выводим сообщение
print(war2.endurance) # выводим сообщение
print(war2.hair_color) # выводим сообщение
print("       ")

print(war2.endurance) # выводим сообщение
print(war2.power) # выводим сообщение
war2.sleep()  # выводим сообщение
war2.eat()  # выводим сообщение
print(war2.endurance) # выводим сообщение
print(war2.power)
print("       ")

war1.sleep()  # выводим сообщение
war1.eat()  # выводим сообщение
war1.nit()  # выводим сообщение
war1.walk()  # выводим сообщение
war1.info()  # выводим сообщение
print("       ")

war2.sleep()  # выводим сообщение
war2.eat()  # выводим сообщение
war2.nit()  # выводим сообщение
war2.walk()  # выводим сообщение
war2.info()  # выводим сообщение
