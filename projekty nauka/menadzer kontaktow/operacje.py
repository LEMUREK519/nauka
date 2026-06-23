from plik_json import zapisz_do_pliku
from klasa_kontakt import Kontakt

def pokaz_menu():
    print("")
    print("1. Dodaj kontakt")
    print("2. Pokaz kontakty")
    print("3. Wyszukaj kontakty")
    print("4. Edytuj kontakty")
    print("5. Usun kontakty")
    print("6. Sortuj kontakty")
    print("7. Statystyki")
    print("8. Koniec programu")

def dodaj_kontakt(kontakty):

    imie = input("Podaj imie: ")

    if imie == "":
        print("Tytual nie moze byc pusty")
        return
    
    try:
        telefon = int(input("Podaj numer telefonu: "))
    except ValueError:
        print("Numer musi byc liczbami")
        return

    email = input("Podaj email: ")
    
    if email == "":
        print("Email nie moze byc pusty")
        return

    nowy_kontakt = Kontakt(imie, telefon, email)
    kontakty.append(nowy_kontakt)

    zapisz_do_pliku(kontakty)
    print("Dodano nowy kontakt")
    
def pokaz_kontakt(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow")
        return
    
    for index, kontakt in enumerate(kontakty, start=1):
        print(index, end=". ")
        kontakt.pokaz_info()
    
def wyszukaj_kontakt(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow do wyszukania")
        return

    szukany_kontakt = input("Podaj imie lub jego fragment: ").strip().lower()

    znaleziono = False  

    for kontakt in kontakty:
        if szukany_kontakt in kontakt.imie.lower():
            kontakt.pokaz_info()
            znaleziono = True
    
    if not znaleziono:
        print("Nie znaleziono kontaktu")

def edytuj_kontakt(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow do edycji")
        return
    
    pokaz_kontakt(kontakty)

    try:
        numer = int(input("Podaj numer kontaktu do edycji: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
    
    index = numer - 1

    if index < 0 or index >= len(kontakty):
        print("Nie ma kontaktu o takim numerze")
        return
    
    kontakt = kontakty[index]

    print("Edytujesz")
    kontakt.pokaz_info()

    nowe_imie = input("Podaj nowe imie: ")
    try:
        nowy_telefon = int(input("Podaj nowy numer telofnu: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
    
    nowy_email = input("Podaj nowy adres email: ")


    if nowe_imie != "":
        kontakt.imie = nowe_imie
    
    if nowy_telefon != "":
        kontakt.telefon = nowy_telefon

    if nowy_email != "":
        kontakt.email = nowy_email

    zapisz_do_pliku(kontakty)
    print("Zmieniono zadanie")
    kontakt.pokaz_info()

def usun_kontakt(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow do usuniecia")
        return
    
    pokaz_kontakt(kontakty)

    try:
        numer = int(input("Podaj numer kontaktu do usuniecia: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
        
    index = numer - 1

    if index < 0 or index >= len(kontakty):
        print("Nie ma kontaktu o takim numerze")
        return
    
    usuniety_kontakt = kontakty.pop(index)

    print("Usunieto kontakt")
    zapisz_do_pliku(kontakty)
    usuniety_kontakt.pokaz_info()

def sortuj(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow do sortowania")
        return
    
    kontakty.sort(key=lambda kontakt: kontakt.imie)
    print("Kontakty posortowane")

def statystyki(kontakty):
    if len(kontakty) == 0:
        print("Nie ma kontaktow do statystyk")
        return
    
    ilosc_zadan = len(kontakty)
    wykonane_zadania = 0
    niewykonane_zadania = 0
        
    for kontakt in kontakty:
        if kontakt.wykonane:
            wykonane_zadania += 1
        else:
            niewykonane_zadania += 1

    print("Statystyki")
    print("Ilosc zadan: ", ilosc_zadan)
    print("Wykonane zadania: ", wykonane_zadania)
    print("Niewykonane zadania: ", niewykonane_zadania)
            