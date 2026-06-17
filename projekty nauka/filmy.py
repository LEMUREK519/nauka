import json

class Filmy:
    def __init__(self, tytul, autor, rok ,ocena):
      self.tytul = tytul
      self.autor = autor
      self.rok = rok
      self.ocena = ocena  

    def ksiazka_info(self):
       print(self.tytul, "-", self.autor, "-", self.rok, "-", self.ocena)



def wczytaj_pliku():
    pass

filmy = []

def zapisz_do_pliku():
   pass

def panel_startowy():
   pass

def dodaj_film():
   pass

def pokaz_filmy():
   pass

def wyszkaj_film():
   pass

def usun_film():
   pass

def edytuj_film():
   pass

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
        print("Koniec")
        break
    
    else:
        print("Nieznana opjca")