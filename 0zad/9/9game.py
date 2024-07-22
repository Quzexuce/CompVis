class Location:
    def __init__(self, name, description, adjacent_locations=None):
        self.name = name
        self.description = description
        self.adjacent_locations = adjacent_locations or []

    def add_adjacent_location(self, location):
        if location not in self.adjacent_locations:
            self.adjacent_locations.append(location)
            location.add_adjacent_location(self)

    def __str__(self):
        return self.name

class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location

    def move_to(self, location):
        if location in self.current_location.adjacent_locations:
            self.current_location = location
            print(f"{self.name} переместился в {location.name}")
            print(location.description)
        else:
            print("Вы не можете туда переместиться.")

    def get_current_location(self):
        return self.current_location

class Game:
    def __init__(self, player):
        self.player = player

    def start(self):
        print("Добро пожаловать в игру!")
        print(f"Вы находитесь в {self.player.get_current_location().name}.")
        print(self.player.get_current_location().description)
        self.play()

    def play(self):
        while True:
            print("\nКуда вы хотите пойти?")
            for i, loc in enumerate(self.player.get_current_location().adjacent_locations):
                print(f"{i + 1}. {loc.name}")

            try:
                choice = int(input("Введите номер вашего выбора: "))
                if 1 <= choice <= len(self.player.get_current_location().adjacent_locations):
                    selected_location = self.player.get_current_location().adjacent_locations[choice - 1]
                    self.player.move_to(selected_location)
                else:
                    print("Неправильный выбор.")
            except ValueError:
                print("Введите корректный номер.")

# Создание локаций
forest = Location("Лес", "Вы находитесь в густом лесу. Вокруг вас высокие деревья.")
cave = Location("Пещера", "Вы вошли в тёмную пещеру. Слышен звук капающей воды.")
lake = Location("Озеро", "Вы у озера с чистой водой. Видны плавающие рыбы.")
village = Location("Деревня", "Вы в деревне с несколькими домиками и жителями.")

# Связывание локаций
forest.add_adjacent_location(cave)
forest.add_adjacent_location(lake)
lake.add_adjacent_location(village)
village.add_adjacent_location(cave)

# Создание игрока
player_name = input("Введите ваше имя: ")
player = Player(player_name, forest)

# Запуск игры
game = Game(player)
game.start()
