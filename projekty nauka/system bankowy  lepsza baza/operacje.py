from klasa import KontoBankowe
from baza import (dodaj_konto_do_bazy , aktualizuj_konto, aktualizuj_przelew, usun_konto_z_bazy)
def pokaz_menu():
    print("\n--- BANK 2.0 ---")
    print("1. Utwórz konto")
    print("2. Pokaż konta")
    print("3. Wpłata")
    print("4. Wypłata")
    print("5. Przelew")
    print("6. Historia")
    print("7. Usun konto")
    print("8. Wyjście")

def utworz_konto_bankowe(konta):
    wlasciciel = input("Podaj wlasciciela konta: ")
    if wlasciciel == "":
        print("Nazwa nie moze byc pusta")
        return
    
    try:
        saldo = float(input("Podaj saldo poczatkowe: "))
    except ValueError:
        print("Saldo musi byc liczba")
        return
    
    if saldo < 0:
        print("Saldo poczatkowe nie moze byc ujemne")
        return

    nowe_konto = KontoBankowe(wlasciciel,saldo)

    dodaj_konto_do_bazy(nowe_konto)
    konta.append(nowe_konto)
    print("Utworzono nowe konto")

def pokaz_konta(konta):
    if len(konta) == 0:
        print("Brak kont")
    else:
        print("\nLista kont: ")

        for konto in konta:
            print(f"ID:{konto.id} - {konto.wlasciciel} - {konto.saldo}")

def znajdz_konto(konta, id_konta):
    for konto in konta:
        if konto.id == id_konta:
            return konto
        
    return None

def wybierz_konto(konta, komunikat):
    if len(konta) == 0:
        print("Brak kont")
        return None
    
    pokaz_konta(konta)

    try:
        id_konta = int(input(komunikat))
    except ValueError:
        print("ID konta musi byc liczba")
        return None
    
    konto = znajdz_konto(konta, id_konta)
    
    if konto is None:
        print("Nie ma konta o takim numerze")
        return None
    
    return konto

def wplata_na_konto(konta):
    konto = wybierz_konto(konta, "Podaj ID konta do wplaty: ")

    if konto is None:
        return
    
    try:
        kwota = float(input("Podaj kwote do wplaty: "))
    except ValueError:
        print("Numer i kwota musza byc liczbami")
        return

    if konto.wplata(kwota):
        aktualizuj_konto(konto)
        konto.pokaz_saldo()

def wyplata_na_konto(konta):
    konto = wybierz_konto(konta, "Podaj ID konta do wyplaty: ")

    if konto is None:
        return

    try:
        kwota = float(input("Podaj kwote do wyplaty: "))
    except ValueError:
        print("Numer i kwota musza byc liczbami")
        return
    
    if konto.wyplata(kwota):
        aktualizuj_konto(konto)
        konto.pokaz_saldo()

def przelew_na_konto(konta):
    if len(konta) < 2:
        print("Nie ma innych kont do przelewu")
        return
    
    pokaz_konta(konta)

    try:
        nadawca = int(input("Podaj ID konta nadawcy: "))
        odbiorca = int(input("Podaj ID konta odbiorcy: "))
        kwota = float(input("Podaj kwote do przlewu: "))
    except ValueError:
        print("Wszystkie dane musza byc liczbami")
        return

    if nadawca == odbiorca:
        print("Nie mozna zrobic przelewu do samego siebie")
        return
    
    konto_nadawcy = znajdz_konto(konta, nadawca)
    konto_odbiorca = znajdz_konto(konta, odbiorca)

    if konto_nadawcy is None:
        print("Nie ma konta o takim ID")
        return
    
    if konto_odbiorca is None:
        print("Nie ma konta o takim ID")
        return
    
    if konto_nadawcy.przelew(konto_odbiorca, kwota):
        aktualizuj_przelew(konto_nadawcy, konto_odbiorca)

    print("Saldo nadawcy")
    konto_nadawcy.pokaz_saldo()

    print("Saldo odbiorcy")
    konto_odbiorca.pokaz_saldo()

def pokaz_historie(konta):
    konto = wybierz_konto(konta, "Podaj ID konta do sprawdzenia historii: ")

    if konto is None:
        return
    
    konto.pokaz_historie()

def usun_konto(konta):
    konto = wybierz_konto(konta, "Podaj ID konta do usuniecia: ")

    if konto is None:
        return
    
    potwierdzenie = input(f"Czy napewno chcesz usunac konto {konto.wlasciciel}?\n"
                          "Wpisz TAK: ")
    if potwierdzenie.upper() != "TAK":
        print("Anulowano")
        return
    
    if usun_konto_z_bazy(konto.id):
        konta.remove(konto)
        print("Konto zostalo usuniete")
    else:
        print("Nie udalo usunac sie konta")