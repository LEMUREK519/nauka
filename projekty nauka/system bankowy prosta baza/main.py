
from baza import wczytaj_z_bazy
from operacje import (
    pokaz_menu,
    utworz_konto_bankowe,
    pokaz_konta,
    wplata_na_konto,
    wyplata_na_konto,
    przelew_na_konto,
    pokaz_historie
)

konta = wczytaj_z_bazy()

while True:
    pokaz_menu()

    wybor = input("Wybierz opcje: ")

    
    if wybor == "1":
        utworz_konto_bankowe(konta)

    elif wybor == "2":
        pokaz_konta(konta)

    elif wybor == "3":
        wplata_na_konto(konta)

    elif wybor == "4":
        wyplata_na_konto(konta)

    elif wybor == "5":
        przelew_na_konto(konta)
    
    elif wybor == "6":
        pokaz_historie(konta)

    elif wybor == "7":
        print("Koniec programu")
        break

    else:
        print("Nieznana opcja")   