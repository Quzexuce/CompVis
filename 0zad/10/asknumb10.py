import tkinter as tk
from tkinter import messagebox
import random

def check_guess():
    """Проверка предположения пользователя."""
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            raise ValueError("Вне диапазона")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число от 1 до 100.")
        return

    global tries, the_number

    tries += 1
    if guess > the_number:
        result_label.config(text="Меньше.")
    elif guess < the_number:
        result_label.config(text="Больше.")
    else:
        result_label.config(text=f"Поздравляем! Вы отгадали число {the_number} за {tries} попыток!")
        guess_button.config(state=tk.DISABLED)
        return

    if tries >= max_tries:
        result_label.config(text=f"Вы исчерпали все попытки. Загаданное число было {the_number}.")
        guess_button.config(state=tk.DISABLED)

def start_game():
    """Начало новой игры."""
    global tries, the_number, max_tries
    try:
        max_tries = int(tries_entry.get())
        if max_tries < 1 or max_tries > 100:
            raise ValueError("Вне диапазона")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите целое число от 1 до 100 для количества попыток.")
        return

    tries = 0
    the_number = random.randint(1, 100)
    result_label.config(text="Игра началась! Введите ваше предположение.")
    guess_button.config(state=tk.NORMAL)

# Создание главного окна
root = tk.Tk()
root.title("Угадай число")

# Метка и поле для ввода количества попыток
tries_label = tk.Label(root, text="Введите количество попыток (1-100):")
tries_label.pack()

tries_entry = tk.Entry(root)
tries_entry.pack()

start_button = tk.Button(root, text="Начать игру", command=start_game)
start_button.pack()

# Метка и поле для ввода предположения
guess_label = tk.Label(root, text="Введите ваше предположение (1-100):")
guess_label.pack()

guess_entry = tk.Entry(root)
guess_entry.pack()

guess_button = tk.Button(root, text="Угадать", state=tk.DISABLED, command=check_guess)
guess_button.pack()

# Метка для вывода результата
result_label = tk.Label(root, text="Начните игру, введя количество попыток и нажав 'Начать игру'.")
result_label.pack()

# Глобальные переменные
tries = 0
the_number = 0
max_tries = 0

# Запуск главного цикла обработки событий
root.mainloop()
