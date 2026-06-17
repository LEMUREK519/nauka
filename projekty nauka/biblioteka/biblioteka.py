import json

class Ksiazka:
    def __init__(self, tytul, autor,rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok

    def show_info(self):
        print(self.tytul, "-", self.autor, "-", self.rok)

    def to_dict(self):
        return {
            "tytul": self.tytul,
            "autor": self.autor,
            "rok": self.rok
        }

def wczytaj_z_pliku():
    try:
        with open("ksiazki.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        return []
    
    ksiazki_z_pliku = []

    for element in dane:
        ksiazka = Ksiazka(
            element["tytul"],
            element["autor"],
            element["rok"]
        )
        ksiazki_z_pliku.append(ksiazka)

    return ksiazki_z_pliku

ksiazki = wczytaj_z_pliku()

def pokaz_menu():
    print()
    print("1. Dodaj ksiazke")
    print("2. Pokaz ksiazke")
    print("3. Wyszukaj ksiazke")
    print("4. Usun ksiazke")
    print("5. Edytuj ksiazke")
    print("6. Zakoncz")

def zapisz_do_pliku():
    dane = []

    for ksiazka in ksiazki:
        dane.append(ksiazka.to_dict())

    with open("ksiazki.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)

def dodaj_ksiazke():
    tytul = input("Podaj tytual: ")
    if tytul == "":
        print("Tytul nie moze byc pusty")
        return
    
    autor = input("Podaj autora: ")
    if autor == "":
        print("Autor nie moze byc pusty")
        return

    try:
        rok = int(input("Podaj rok: "))
    except ValueError:
        print("Rok musi byc liczba")
        return
    
    nowa_ksiazka = Ksiazka(tytul, autor, rok)
    ksiazki.append(nowa_ksiazka)
    zapisz_do_pliku()
    print("Dodano ksiazke")

def pokaz_ksiazki():
    if len(ksiazki) == 0:
        print("Nie ma zadnych ksiazek")
        return
    
    for index, ksiazka in enumerate(ksiazki, start=1):
        print(index, end=". ")
        ksiazka.show_info()

def wyszukaj_ksiazke():
    if len(ksiazki) == 0:
        print("Nie ma zadnych ksiazek")
        return
    
    szukany_tytual = input("Podaj tytaul lub jego fragment: ").lower()

    znaleziono = False

    for ksiazka in ksiazki:
        if szukany_tytual in ksiazka.tytul.lower():
            ksiazka.show_info()
            znaleziono = True
        
    if not znaleziono:
            print("Nie ma takiej ksiazki")
        
def usun_ksiazke():
    if len(ksiazki) == 0:
        print("Nie ma ksiazek do usuniecia")
        return
    
    pokaz_ksiazki()

    try:
        numer = int(input("Podaj numer ksiazki do usuniecia: "))
    except ValueError:
        print("Musisz podac liczbe")
        return
    index = numer - 1

    if index < 0 or index >= len(ksiazki):
        print("Nie ma ksiazki o takim numerze")
        return
    
    usunieta_ksiazka = ksiazki.pop(index)
    zapisz_do_pliku()

    print("Usunieto ksiazke: ")
    usunieta_ksiazka.show_info()

def edytuj_ksiazke():
    if len(ksiazki) == 0:
        print("Nie ma ksiazek do edycji")
        return
    
    try:
        numer = int(input("Podaj numer ksiazki do edycji: "))
    except ValueError:
        print("Muszisz podac liczbe")
        return
    
    index = numer - 1

    if index < 0 or index >= len(ksiazki):
        print("Nie ma ksiazki ")
        return
    
    ksiazka = ksiazki[index]
    print("Edytujesz")
    ksiazka.show_info()

    nowy_tytul = input("Nowy tytul, zostaw puste bez zmian: ")
    nowy_autor = input("Nowy autor, zostaw puste bez zmian: ")
    nowy_rok = input("Nowy rok, zostaw puste bez zmian: ")

    if nowy_tytul != "":
        ksiazka.tytul = nowy_tytul
    
    if nowy_autor != "":
        ksiazka.autor = nowy_autor

    if nowy_rok != "":
        try:
            ksiazka.rok = int(nowy_rok)
        except ValueError:
            print("Rok musi byc liczba")
            return
        
    zapisz_do_pliku()
    print("Zmieniono ksiazke")

while True:
    pokaz_menu()

    wybor = input("Wybierz opcje: ")

    if wybor == "1":
        dodaj_ksiazke()

    elif wybor == "2":
        pokaz_ksiazki()
    
    elif wybor == "3":
        wyszukaj_ksiazke()

    elif wybor == "4":
        usun_ksiazke()

    elif wybor == "5":
        edytuj_ksiazke()

    elif wybor == "6":
        print("Koniec")
        break
    
    else:
        print("Nieznana opjca")