import json

class Auto:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def show_info(self):
        print(self.marka, "-", self.model, "-", self.rok)

    def get_age(self):
        return 2026 - self.rok
    
    def age_car(self):
        print("Age of car:", self.get_age())

    def old_car(self):
        if self.get_age() >= 25:
            print("The car is vintage")
        else:
            print("The car isn't vintage")
        
    def to_dict(self):
        return {
            "marka": self.marka,
            "model": self.model,
            "rok": self.rok
        }
    
def wczytaj_z_pliku():
    try:
        with open("auta.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        return []
    
    auta_z_pliku = []

    for element in dane:
        auto = Auto(
            element["marka"],
            element["model"],
            element["rok"]
        )
        auta_z_pliku.append(auto)

    return auta_z_pliku

auta = wczytaj_z_pliku()


def panel_startowy():
    print()
    print("1. Dodaj auto")
    print("2. Pokaż auto")
    print("3. Usuń auto")
    print("4. Zakończ")

def zapis_do_pliku():
    dane = []

    for auto in auta:
        dane.append(auto.to_dict())
    
    with open("auta.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)

def dodaj_auto():
    marka = input("Podaj marke: ")
    model = input("Podaj model: ")
        
    try:
        rok = int(input("Podaj rok: "))
    except ValueError:
        print("Rok musi byc liczba")
        return

    nowe_auta = Auto(marka, model, rok)
    auta.append(nowe_auta)

    zapis_do_pliku()

    print("Dodano auto")

def pokaz_auto():
    if len(auta) == 0:
        print("Nie ma żadnych aut")
        return
    
    for index, auto in enumerate(auta, start=1):
        print(index, end=". ")
        auto.show_info()
        auto.age_car()
        auto.old_car()
        print()

def usun_auto():
    if len(auta) == 0:
        print("Nie ma zadnych aut do usuniecia")
        return
    
    pokaz_auto()

    try:
        numer = int(input("Podaj numer auto do usuniecia: "))
    except ValueError:
        print("Musisz podac liczbe")
        return
    index = numer -1

    if index < 0 or index >= len(auta):
        print("Nie ma auta o takim numerze")
        return
    
    usuniete_auto = auta.pop(index)
    zapis_do_pliku()

    print("Usunieto auto")
    usuniete_auto.show_info()

while True:
    
    panel_startowy()

    wybor = (input("Wybierz opcje: "))

    if wybor == "1":
        dodaj_auto()

    elif wybor == "2":
        pokaz_auto()
            
    elif wybor == "3":
        usun_auto()

    elif wybor == "4":
        print("Koniec programu")
        break

    else:
        print("Nieznana opcja")