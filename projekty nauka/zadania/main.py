from zadanie import Zadanie
from plik_json import wczytaj_z_pliku, zapisz_do_pliku

zadania = wczytaj_z_pliku()

def pokaz_menu():
    print()
    print("1. Dodaj zadanie")
    print("2. Pokaż zadania")
    print("3. Oznacz jako wykonane")
    print("4. Oznacz jako niewykonane")
    print("5. Usuń zadanie")
    print("6. Wyszukaj zadanie")
    print("7. Edytuj zadanie")
    print("8. Statystyki")
    print("9. Zakończ")

def dodaj_zadanie():
    
    tytul = input("Podaj tytul: ")

    if tytul == "":
        print("Tytul nie moze byc pusty")
        return
    
    opis = input("Podaj opis: ")
    
    if opis == "":
        print("Opis nie moze byc pusty")
        return

    nowe_zadanie = Zadanie(tytul, opis)
    zadania.append(nowe_zadanie)

    zapisz_do_pliku(zadania)
    print("Dodamo zadanie")


def pokaz_zadania():
    if len(zadania) == 0:
        print("Nie ma zadanych zdan")
        return
    for index, zadanie in enumerate(zadania, start=1):
        print(index, end=". ")
        zadanie.pokaz_info()

def oznacz_jako_wykonane():
    if len(zadania) == 0:
        print("Nie ma zadan")
        return
    
    pokaz_zadania()
    
    try:
        numer = int(input("Podaj numer zadania jako wykonane: "))
    except ValueError:
        print("Numer musi byc liczba")
        return

    index = numer - 1

    if index < 0 or index >= len(zadania):
        print("Nie ma takiego zadania")
        return
    
    zadanie = zadania[index]
    zadanie.wykonane = True

    print("Oznaczona jako wykonane")
    zapisz_do_pliku(zadania)
    zadanie.pokaz_info()

def oznacz_jako_niewykonane():
    if len(zadania) == 0:
        print("Nie ma zadan")
        return
    
    pokaz_zadania()
    
    try:
        numer = int(input("Podaj numer zadania jako niewykonane: "))
    except ValueError:
        print("Numer musi byc liczba")
        return

    index = numer - 1

    if index < 0 or index >= len(zadania):
        print("Nie ma takiego zadania")
        return
    
    zadanie = zadania[index]
    zadanie.wykonane = False

    print("Oznaczone jako niewykonane")
    zapisz_do_pliku(zadania)
    zadanie.pokaz_info()

def usun_zadanie():
    if len(zadania) == 0:
        print("Nie ma zadan do usunia")
        return
    
    pokaz_zadania()
    
    try:
        numer = int(input("Podaj numer zadania do usuniecia: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
    
    index = numer - 1

    if index < 0 or index >= len(zadania):
        print("Nie ma zadania o takim numerze")
        return
    
    usuniete_zadanie = zadania.pop(index)

    print("Usunieto zadanie")
    zapisz_do_pliku(zadania)
    usuniete_zadanie.pokaz_info()

def wyszukaj_zadanie():
    if len(zadania) == 0:
        print("Nie ma zadan do wyszukania")
        return
    
    szukane_zadanie = input("Podaj tytual zadania lub jego fragment: ").strip().lower()

    if szukane_zadanie == "":
        print("Nie wpisano tekstu")
        return
    
    znaleziono = False

    for zadanie in zadania:
        if szukane_zadanie in zadanie.tytul.lower():
            zadanie.pokaz_info()
            znaleziono = True

    if not znaleziono:
        print("Nie znaleziono zadania")

def edytuj_zadanie():
    if len(zadania) == 0:
        print("Nie ma zadan do edycji")
        return
    
    pokaz_zadania()

    try:
        numer = int(input("Podaj numer zadania do edyzji: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
    
    index = numer - 1

    if index < 0 or index >= len(zadania):
        print("Nie ma zadania o takim numerze")
        return
    
    zadanie = zadania[index]

    print("Edytujesz")
    zadanie.pokaz_info()

    nowy_tytul = input("Podaj nowy tytul: ")
    nowy_opis = input("Podaj nowy opis: ")

    if nowy_tytul != "":
        zadanie.tytul = nowy_tytul
    
    if nowy_opis != "":
        zadanie.opis = nowy_opis

    zapisz_do_pliku(zadania)
    print("Zmieniono zadnie")
    zadanie.pokaz_info()

def statystyki():
    if len(zadania) == 0:
        print("Nie ma zadan")
        return
    
    liczba_zadan = len(zadania)
    wykonane = 0
    niewykonane = 0

    for zadanie in zadania:
        if zadanie.wykonane:
            wykonane += 1
        else:
            niewykonane += 1

    procent = wykonane / liczba_zadan * 100

    print("Statystyki")
    print("Liczba wszystkich zadan: ", liczba_zadan)
    print("Wykonane zadania: ", wykonane)
    print("Niewykonane zadania: ", niewykonane)
    print("Procent wykonania: ", procent)

while True:
    pokaz_menu()

    wybor = input("Wybierz opjce: ")
    
    if wybor == "1":
        dodaj_zadanie()

    elif wybor == "2":
        pokaz_zadania()

    elif wybor == "3":
        oznacz_jako_wykonane()

    elif wybor == "4":
        oznacz_jako_niewykonane()

    elif wybor == "5":
        usun_zadanie()
    
    elif wybor == "6":
        wyszukaj_zadanie()

    elif wybor == "7":
        edytuj_zadanie()

    elif wybor == "8":
        statystyki()

    elif wybor == "9":
        print("Koniec programu")
        break

    else:
        print("Nieznana opcja")   
