import json

class Filmy:
    def __init__(self, tytul, autor, rok ,ocena, obejrzany=False):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok
        self.ocena = ocena
        self.obejrzany = obejrzany

    def film_info(self):
        if self.obejrzany:
            status = "obejrzany"
        else:
            status = "nieobejrzany"
        print(self.tytul, "-", self.autor, "-", self.rok, "-", self.ocena, "-", status)

    def to_dict(self):
        return{
            "tytul": self.tytul,
            "autor" : self.autor,
            "rok": self.rok,
            "ocena": self.ocena,
            "obejrzany": self.obejrzany
        }

def wczytaj_pliku():
    try:
        with open("kino.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        return[]
    
    filmy_z_pliku = []

    for element in dane:
        film = Filmy(
            element["tytul"],
            element["autor"],
            element["rok"],
            element["ocena"],
            element["obejrzany"]
        )
        filmy_z_pliku.append(film)

    return filmy_z_pliku

filmy = wczytaj_pliku()

def zapisz_do_pliku():
    dane = []

    for film in filmy:
        dane.append(film.to_dict())

    with open("kino.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)

def panel_startowy():
    print()
    print("1. Dodaj film")
    print("2. Pokaż filmy")
    print("3. Wyszkaj filmy")
    print("4. Usuń filmy")
    print("5. Edytuj film")
    print("6. Dodaj do obejrzane")
    print("7. Oznacz jako nieobejrzane")
    print("8. Zakoncz")

def dodaj_film():
    tytul = input("Podaj tytul: ")
    if tytul == "":
        print("Tytul nie moze byc pusty")
        return

    autor = input("Podaj autora: ")
    if autor == "":
        print("Autor nie moze byc pusty")
        return
    
    try:
        rok = int(input("Podaj rok: "))
        ocena = int(input("Podaj ocene od 0 do 10: "))
    except ValueError:
        print("Rok musi byc liczba")
        return
    if ocena < 1 or ocena > 10:
        print("Ocena musi byc od 1 do 10")
        return
    
    nowy_film = Filmy(tytul, autor, rok, ocena)
    filmy.append(nowy_film)
    zapisz_do_pliku()
    print("Dodano film")
    

def pokaz_filmy():
    if len(filmy) == 0:
        print("Nie ma zadnych filmow")
        return
    
    for index, film in enumerate(filmy, start=1):
        print(index,end=". ")
        film.film_info()


def wyszkaj_film():
    if len(filmy) == 0:
        print("Nie ma filmow do wyszukania")
        return
    
    szukany_film = input("Podaj tytual filmu lub jego fragment: ").lower()

    znaleziono = False

    for film in filmy:
        if szukany_film in film.tytul.lower():
            film.film_info()
            znaleziono = True

    if not znaleziono:
        print("Nie ma takiej ksiazki")

def usun_film():
    if len(filmy) == 0:
        print("Nie ma ksiazek do usniecia")
        return
    
    pokaz_filmy()
    
    try:
        numer = int(input("Podaj numer filmu do usuniecia: "))
    except ValueError:
        print("Muszisz podac liczbe")
        return
    
    index = numer - 1

    if index < 0 or index >= len(filmy):
        print("Nie ma filmu o takim numerze")
        return
    
    usuniety_film = filmy.pop(index)
    zapisz_do_pliku()

    print("Usunieto film")
    usuniety_film.film_info()

def edytuj_film():
    if len(filmy) == 0:
        print("Nie ma filmow do edycji")
        return

    try:
        numer = int(input("Podaj numer filmu do edycji: "))
    except ValueError:
        print("Numer filmu musi byc liczba")
        return
    
    index = numer - 1
    
    if index < 0 or index >= len(filmy):
        print("Nie ma ksiazki o takim numerze")
        return
    
    film = filmy[index]
    print("Edytujesz")
    film.film_info()

    nowy_tytaul = input("Podaj nowy tytul: ")
    nowy_autor = input("Podaj nowego autora: ")
    nowy_rok = input("Podaj nowy rok: ")
    nowa_ocena = input("Podaj nowa ocene: ")

    if nowy_tytaul != "":
        film.tytul = nowy_tytaul
    
    if nowy_autor != "":
        film.autor = nowy_autor

    if nowy_rok != "":
        try:
            film.rok = int(nowy_rok)
        except ValueError:
            print("Rok musi byc liczba")
            return

    if nowa_ocena != "":
        try:
            film.ocena = int(nowa_ocena)
        except ValueError:
            print("Ocena musi byc liczba")
            return
    
    zapisz_do_pliku()
    print("Zmieniono film")

def dodaj_do_obejrzane():
    if len(filmy) == 0:
        print("Nie ma filmow")
        return
    
    pokaz_filmy()

    try:
        numer = int(input("Podaj numer filmu, ktory obejrzalej: "))
    except ValueError:
        print("Nie ma filmu o takim numerze")
        return
    
    index = numer - 1

    if index < 0 or index > len(filmy):
        print("Nie ma filmu o takim numerze")
        return
    
    film = filmy[index]
    film.obejrzany = True

    zapisz_do_pliku()

    print("Oznaczono film jako obejrzany")
    film.film_info()

def oznacz_jako_nieobejrzany():
    if len(filmy) == 0:
        print("Nie ma filmow")
        return

    pokaz_filmy()

    try:
        numer = int(input("Podaj numer filmu: "))
    except ValueError:
        print("Musisz podac liczbe")
        return

    index = numer - 1

    if index < 0 or index >= len(filmy):
        print("Nie ma filmu o takim numerze")
        return

    film = filmy[index]
    film.obejrzany = False

    zapisz_do_pliku()

    print("Oznaczono film jako nieobejrzany:")
    film.film_info()


while True:
   
    panel_startowy()

    wybor = input("Wybierz opcje: ")

    if wybor == "1":
        dodaj_film()

    elif wybor == "2":
        pokaz_filmy()
    
    elif wybor == "3":
        wyszkaj_film()

    elif wybor == "4":
        usun_film()

    elif wybor == "5":
        edytuj_film()

    elif wybor == "6":
        dodaj_do_obejrzane()

    elif wybor == "7":
        oznacz_jako_nieobejrzany()

    elif wybor == "8":
        print("Koniec")
        break
    
    else:
        print("Nieznana opjca")