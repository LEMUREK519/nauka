import random

liczba = random.randint(0,10)

while True:
    strzal = int(input("Zgadnij liczbe: "))

    if strzal == liczba:
        print("brawo")
        break
    elif strzal < liczba:
        print("Za malo")
    else:
        print("Za duzo")






