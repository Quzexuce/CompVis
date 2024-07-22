start = int(input("Введите начало счёта: "))
end = int(input("Введите конец счёта: "))
step = int(input("Введите интервал между числами: "))
if step == 0:
    print("Интервал не может быть равен нулю.")
else:
    if start > end and step > 0:
        print("При положительном интервале начало должно быть меньше конца.")
    elif start < end and step < 0:
        print("При отрицательном интервале начало должно быть больше конца.")
    else:
        for number in range(start, end + 1, step):
            print(number)
