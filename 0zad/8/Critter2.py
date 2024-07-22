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
    crit_name = input("Как вы назовете свою зверюшку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print(
            """
Моя зверюшка
0 - Выйти
1 - Узнать о самочувствии зверюшки
2 - Покормить зверюшку
3 - Поиграть со зверюшкой
"""
        )
        choice = input("Ваш выбор: ")
        print()

        # ВЫХОД
        if choice == "0":
            print("До свидания.")

        # БЕСЕДА СО ЗВЕРЮШКОЙ
        elif choice == "1":
            crit.talk()

        # КОРМЛЕНИЕ ЗВЕРЮШКИ
        elif choice == "2":
            food_amount = int(input("Сколько еды дать зверюшке? "))
            crit.eat(food_amount)

        # ИГРА СО ЗВЕРЮШКОЙ
        elif choice == "3":
            fun_time = int(input("Сколько времени играть со зверюшкой? "))
            crit.play(fun_time)

        # СЕКРЕТНЫЙ ПУНКТ
        elif choice == "99":
            print(crit)

        # НЕПОНЯТНЫЙ ПОЛЬЗОВАТЕЛЬСКИЙ ВВОД
        else:
            print(f"Извините, в меню нет пункта {choice}")

if __name__ == "__main__":
    main()

input("\n\nНажмите Enter, чтобы выйти.")
