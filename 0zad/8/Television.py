class Television:
    """Класс, имитирующий телевизор."""

    def __init__(self, channel=1, volume=10, max_channel=10, max_volume=100):
        self.channel = channel
        self.volume = volume
        self.max_channel = max_channel
        self.max_volume = max_volume

    def change_channel(self, new_channel):
        if 1 <= new_channel <= self.max_channel:
            self.channel = new_channel
            print(f"Канал изменен на {self.channel}.")
        else:
            print(f"Ошибка: канал должен быть в диапазоне от 1 до {self.max_channel}.")

    def increase_volume(self):
        if self.volume < self.max_volume:
            self.volume += 10
            print(f"Громкость увеличена до {self.volume}.")
        else:
            print(f"Громкость уже на максимуме ({self.max_volume}).")

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 10
            print(f"Громкость уменьшена до {self.volume}.")
        else:
            print("Громкость уже на минимуме (0).")

    def __str__(self):
        return f"Текущий канал: {self.channel}, текущая громкость: {self.volume}"

def main():
    tv = Television()

    choice = None
    while choice != "0":
        print(
            """
Телевизор
0 - Выйти
1 - Изменить канал
2 - Увеличить громкость
3 - Уменьшить громкость
4 - Узнать текущие настройки
"""
        )
        choice = input("Ваш выбор: ")
        print()

        # ВЫХОД
        if choice == "0":
            print("До свидания.")

        # ИЗМЕНЕНИЕ КАНАЛА
        elif choice == "1":
            new_channel = int(input("Введите номер канала: "))
            tv.change_channel(new_channel)

        # УВЕЛИЧЕНИЕ ГРОМКОСТИ
        elif choice == "2":
            tv.increase_volume()

        # УМЕНЬШЕНИЕ ГРОМКОСТИ
        elif choice == "3":
            tv.decrease_volume()

        # ТЕКУЩИЕ НАСТРОЙКИ
        elif choice == "4":
            print(tv)

        # НЕПОНЯТНЫЙ ПОЛЬЗОВАТЕЛЬСКИЙ ВВОД
        else:
            print(f"Извините, в меню нет пункта {choice}")

main()

input("\n\nНажмите Enter, чтобы выйти.")
