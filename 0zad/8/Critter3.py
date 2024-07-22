import random

class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def _pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print(f"Меня зовут {self.name}, и сейчас я чувствую себя {self.mood}.\n")
        self._pass_time()

    def eat(self, food=4):
        print("Мррр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self._pass_time()

    def play(self, fun=4):
        print("Yиии!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self._pass_time()

    def __str__(self):
        return f"Имя: {self.name}, Голод: {self.hunger}, Скука: {self.boredom}"

def main():
    critters = []
    num_critters = int(input("Сколько зверюшек вы хотите завести на зооферме? "))

    for i in range(num_critters):
        name = input(f"Как вы назовете зверюшку №{i + 1}? ")
        hunger = random.randint(0, 10)
        boredom = random.randint(0, 10)
        critter = Critter(name, hunger, boredom)
        critters.append(critter)

    choice = None
    while choice != "0":
        print(
            """
Зооферма
0 - Выйти
1 - Узнать о самочувствии всех зверюшек
2 - Покормить всех зверюшек
3 - Поиграть со всеми зверюшками
"""
        )
        choice = input("Ваш выбор: ")
        print()

        # ВЫХОД
        if choice == "0":
            print("До свидания.")

        # БЕСЕДА СО ВСЕМИ ЗВЕРЮШКАМИ
        elif choice == "1":
            for critter in critters:
                critter.talk()

        # КОРМЛЕНИЕ ВСЕХ ЗВЕРЮШЕК
        elif choice == "2":
            food_amount = int(input("Сколько еды дать каждой зверюшке? "))
            for critter in critters:
                critter.eat(food_amount)

        # ИГРА СО ВСЕМИ ЗВЕРЮШКАМИ
        elif choice == "3":
            fun_time = int(input("Сколько времени играть с каждой зверюшкой? "))
            for critter in critters:
                critter.play(fun_time)

        # НЕПОНЯТНЫЙ ПОЛЬЗОВАТЕЛЬСКИЙ ВВОД
        else:
            print(f"Извините, в меню нет пункта {choice}")

main()

input("\n\nНажмите Enter, чтобы выйти.")
