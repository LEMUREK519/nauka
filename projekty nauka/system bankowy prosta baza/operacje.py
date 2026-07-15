from klasa import KontoBankowe
from baza import zapisz_do_bazy

def pokaz_menu():
    print("\n--- BANK 2.0 ---")
    print("1. Utwórz konto")
    print("2. Pokaż konta")
    print("3. Wpłata")
    print("4. Wypłata")
    print("5. Przelew")
    print("6. Historia")
    print("7. Wyjście")

def utworz_konto_bankowe(konta):
    wlasciciel = input("Podaj wlasciciela konta: ")
    if wlasciciel == "":
        print("Nazwa nie moze byc pusta")
        return
    saldo = float(input("Podaj saldo poczatkowe: "))

    nowe_konto = KontoBankowe(wlasciciel,saldo)

    konta.append(nowe_konto)
    zapisz_do_bazy(konta)
    print("Utworzono nowe konto")

def pokaz_konta(konta):
    if len(konta) == 0:
        print("Brak kont")
        return
    else:
        print("\nLista kont: ")

        for index, konto in enumerate(konta, start=1):
            print(f"{index}. {konto.wlasciciel} - {konto.saldo}")

def wplata_na_konto(konta):
    if len(konta) == 0:
        print("Brak kont")
        return
     
    pokaz_konta(konta)
    
    try:
        numer = int(input("Podaj numer konta do wplaty: "))
        kwota = float(input("Podaj kwote do wplaty: "))
    except ValueError:
        print("Numer i kwota musza byc liczbami")
        return
    
    index = numer - 1

    if index < 0 or index >= len(konta):
        print("Nie ma konta o takim numerze")
        return

    konto = konta[index]
    konto.wplata(kwota)
    konto.pokaz_saldo()
    zapisz_do_bazy(konta)

def wyplata_na_konto(konta):
    if len(konta) == 0:
        print("Brak kont")
        return
    
    pokaz_konta(konta)

    try:
        numer = int(input("Podaj numer konta do wyplaty: "))
        kwota = float(input("Podaj kwote do wyplaty: "))
    except ValueError:
        print("Numer i kwota musza byc liczbami")
        return
    
    index = numer - 1

    if index < 0 or index >= len(konta):
        print("Nie ma konta o takim numerze")
        return

    konto = konta[index]
    konto.wyplata(kwota)
    konto.pokaz_saldo()
    zapisz_do_bazy(konta)

def przelew_na_konto(konta):
    if len(konta) < 2:
        print("Nie ma innych kont do przelewu")
        return
    pokaz_konta(konta)

    try:
        nadawca = int(input("Podaj numer konta nadawcy: "))
        odbiorca = int(input("Podaj numer konta odbiorcy: "))
        kwota = float(input("Podaj kwote do przlewu: "))
    except ValueError:
        print("Wszystkie dane musza byc liczbami")
        return

    if nadawca == odbiorca:
        print("Nie mozna zrobic przelewu do samego siebie")
        return
    
    index1 = nadawca - 1
    index2 = odbiorca - 1
    
    if index1 < 0 or index1 >= len(konta):
        print("Nie ma konta o takim numerze")
        return
    
    if index2 < 0 or index2 >= len(konta):
        print("Nie ma konta o takim numerze")
        return
    
    konto_nadawcy = konta[index1]
    konto_odbiorcy = konta[index2]

    konto_nadawcy.przelew(konto_odbiorcy, kwota)
    zapisz_do_bazy(konta)

def pokaz_historie(konta):
    pokaz_konta(konta)

    try:
        numer = int(input("Podaj numer konta do sprawdzenia histori: "))
    except ValueError:
        print("Numer musi byc liczba")
        return
    
    index = numer - 1

    if index < 0 or index >= len(konta):
        print("Nie ma konta o takim numerze")
        return
        
    konto = konta[index]
    konto.pokaz_historie()
    
    