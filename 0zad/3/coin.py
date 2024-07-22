import random
eagle = 0
tails = 0
tries = 1
while tries <= 100:
    coin = random.randint(1,2)
    if coin == 1:
        eagle += 1
    else:
        tails += 1
    tries += 1    
print("Орел выпало ", eagle, "раз")
print("Решка выпало ", tails, "раз")
