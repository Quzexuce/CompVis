def ask_number(question, low, high, step=1):
    """Просит ввести число из диапазона с заданным шагом."""
    response = None
    while response not in range(low, high, step):
        response = input(question)
        if response.isdigit():
            response = int(response)
            if response not in range(low, high, step):
                print(f"Пожалуйста, введите число в диапазоне от {low} до {high} с шагом {step}.")
        else:
            print("Пожалуйста, введите корректное число.")
    return response

# Пример использования функции
low = 0
high = 100
step = 5
question = f"Введите число от {low} до {high} с шагом {step}: "
result = ask_number(question, low, high, step)
print(f"Вы ввели число: {result}")
