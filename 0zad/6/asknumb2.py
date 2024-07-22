import random

def ask_number(question, low, high):
    """Просит ввести число из диапазона."""
    response = None
    while response not in range(low, high):
        response = input(question)
        if response.isdigit():
            response = int(response)
            if response not in range(low, high):
                print(f"Пожалуйста, введите число в диапазоне от {low} до {high}.")
        else:
            print("Пожалуйста, введите корректное число.")
    return response

def main():
    the_number = random.randint(1, 100)
    print("Я загадал число от 1 до 100.")
    
    # Использование ask_number для запроса количества попыток
    max_tries = ask_number("Введите количество попыток: ", 1, 101)
    tries = 0
    
    while tries < max_tries:
        # Использование ask_number для запроса предположений
        guess = ask_number("Ваше предположение: ", 1, 101)
        tries += 1
        
        if guess > the_number:
            print("Меньше.")
        elif guess < the_number:
            print("Больше.")
        else:
            print(f"Поздравляю! Вы отгадали число {the_number} за {tries} попыток!")
            break
    else:
        print(f"Лошпен, ты потратил все попытки. Загаданное число было {the_number}.")

main()
