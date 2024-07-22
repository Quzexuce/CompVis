import random
the_number = random.randint(1, 100)
max_tries = int(input("Введите количество попыток: "))
tries = 1
guess = int(input("Ваше предположение: "))
while guess != the_number and tries < max_tries:
    if guess > the_number:
        print("Меньше")
    else:
        print("Больше")
    guess = int(input("Ваше предположение: "))
    tries += 1
if guess == the_number:
    print("Вам удалось отгадать число", the_number)
    print("Это заняло", tries, "попыток!")
else:
    print("Лошпен ты потратил все попытки. Загаданное число было:", the_number)

