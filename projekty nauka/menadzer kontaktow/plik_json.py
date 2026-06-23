import json
from klasa_kontakt import Kontakt

def wczytaj_do_pliku():
    try:
        with open("lista_kontaktow.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        return []
    
    kontakty_z_pliku = []

    for element in dane:
        kontakt = Kontakt(
            element["imie"],
            element["telefon"],
            element["email"],
            element["wykonane"]
        )
        kontakty_z_pliku.append(kontakt)

    return kontakty_z_pliku

def zapisz_do_pliku(kontakty):
    dane = []
    for kontakt in kontakty:
        dane.append(kontakt.to_dict())

    with open("lista_kontaktow.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)       