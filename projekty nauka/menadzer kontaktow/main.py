from plik_json import wczytaj_do_pliku
from operacje import *

kontakty = wczytaj_do_pliku()

while True:
    pokaz_menu()

    wybor = input("Wybierz opcje: ")

    if wybor == "1":
        dodaj_kontakt(kontakty)
    
    elif wybor == "2":
        pokaz_kontakt(kontakty)
    
    elif wybor == "3":
        wyszukaj_kontakt(kontakty)
    
    elif wybor == "4":
        edytuj_kontakt(kontakty)

    elif wybor == "5":
        usun_kontakt(kontakty)

    elif wybor == "6":
        sortuj(kontakty)

    elif wybor == "7":
        statystyki(kontakty)

    elif wybor == "8":
        print("Koniec programu")
        break

    else:
        print("Nieznana opjca")