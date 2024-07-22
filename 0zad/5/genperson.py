# Начальные данные
points = 30
strength = 0
health = 0
wisdom = 0
agility = 0

while True:
    # Вывод текущих характеристик и оставшихся очков
    print("\nХарактеристики персонажа:")
    print(f"Сила: {strength}")
    print(f"Здоровье: {health}")
    print(f"Мудрость: {wisdom}")
    print(f"Ловкость: {agility}")
    print(f"Оставшиеся очки: {points}\n")

    # Выбор действия
    print("Выберите действие:")
    print("1. Добавить очки к характеристике")
    print("2. Убрать очки из характеристики")
    print("3. Выйти")
    choice = input("Ваш выбор: ")

    if choice == "1":
        # Выбор характеристики для добавления очков
        print("Выберите характеристику для добавления очков:")
        print("1. Сила")
        print("2. Здоровье")
        print("3. Мудрость")
        print("4. Ловкость")
        stat_choice = int(input("Ваш выбор: "))

        if stat_choice == 1:
            stat_name = "Сила"
            stat_value = strength
        elif stat_choice == 2:
            stat_name = "Здоровье"
            stat_value = health
        elif stat_choice == 3:
            stat_name = "Мудрость"
            stat_value = wisdom
        elif stat_choice == 4:
            stat_name = "Ловкость"
            stat_value = agility
        else:
            print("Неверный выбор. Попробуйте еще раз.")
            continue

        # Добавление очков к выбранной характеристике
        while True:
            print(f"Сколько очков хотите добавить к {stat_name}? (доступно {points})")
            try:
                add_points = int(input())
                if add_points <= points:
                    stat_value += add_points
                    points -= add_points
                    break
                else:
                    print("Недостаточно очков. Попробуйте еще раз.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")

        # Обновление значения выбранной характеристики
        if stat_choice == 1:
            strength = stat_value
        elif stat_choice == 2:
            health = stat_value
        elif stat_choice == 3:
            wisdom = stat_value
        elif stat_choice == 4:
            agility = stat_value

    elif choice == "2":
        # Выбор характеристики для удаления очков
        print("Выберите характеристику для удаления очков:")
        print("1. Сила")
        print("2. Здоровье")
        print("3. Мудрость")
        print("4. Ловкость")
        stat_choice = int(input("Ваш выбор: "))

        if stat_choice == 1:
            stat_name = "Сила"
            stat_value = strength
        elif stat_choice == 2:
            stat_name = "Здоровье"
            stat_value = health
        elif stat_choice == 3:
            stat_name = "Мудрость"
            stat_value = wisdom
        elif stat_choice == 4:
            stat_name = "Ловкость"
            stat_value = agility
        else:
            print("Неверный выбор. Попробуйте еще раз.")
            continue

        # Удаление очков из выбранной характеристики
        while True:
            print(f"Сколько очков хотите убрать от {stat_name}? (доступно {stat_value})")
            try:
                remove_points = int(input())
                if remove_points <= stat_value:
                    stat_value -= remove_points
                    points += remove_points
                    break
                else:
                    print("Недостаточно очков в характеристике. Попробуйте еще раз.")
            except ValueError:
                print("Пожалуйста, введите корректное число.")

        # Обновление значения выбранной характеристики
        if stat_choice == 1:
            strength = stat_value
        elif stat_choice == 2:
            health = stat_value
        elif stat_choice == 3:
            wisdom = stat_value
        elif stat_choice == 4:
            agility = stat_value

    elif choice == "3":
        break
    else:
        print("Неверный выбор. Попробуйте еще раз.")

# Вывод конечных характеристик персонажа
print("\nКонечные характеристики персонажа:")
print(f"Сила: {strength}")
print(f"Здоровье: {health}")
print(f"Мудрость: {wisdom}")
print(f"Ловкость: {agility}")
print(f"Оставшиеся очки: {points}")
print("Спасибо за игру!")



                    
