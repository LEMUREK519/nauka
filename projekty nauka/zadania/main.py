
from plik_json import wczytaj_z_pliku
from operacje import (
        pokaz_menu,
        dodaj_zadanie,
        pokaz_zadania,
        oznacz_jako_wykonane,
        oznacz_jako_niewykonane,
        usun_zadanie,
        wyszukaj_zadanie,
        edytuj_zadanie,
        statystyki
)

zadania = wczytaj_z_pliku()

while True:
    pokaz_menu()

    wybor = input("Wybierz opjce: ")
    
    if wybor == "1":
        dodaj_zadanie(zadania)

    elif wybor == "2":
        pokaz_zadania(zadania)

    elif wybor == "3":
        oznacz_jako_wykonane(zadania)

    elif wybor == "4":
        oznacz_jako_niewykonane(zadania)

    elif wybor == "5":
        usun_zadanie(zadania)
    
    elif wybor == "6":
        wyszukaj_zadanie(zadania)

    elif wybor == "7":
        edytuj_zadanie(zadania)

    elif wybor == "8":
        statystyki(zadania)

    elif wybor == "9":
        print("Koniec programu")
        break

    else:
        print("Nieznana opcja")   
