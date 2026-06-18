import json
from zadanie import Zadanie

def wczytaj_z_pliku():
    try:
        with open("lista_zadan.json", "r", encoding="utf-8") as plik:
            dane = json.load(plik)
    except FileNotFoundError:
        return []
    
    zadania_z_pliku = []

    for element in dane:
        zadanie = Zadanie(
            element["tytul"],
            element["opis"],
            element["wykonane"]
        )
        zadania_z_pliku.append(zadanie)
    
    return zadania_z_pliku

def zapisz_do_pliku(zadania):
    dane = []

    for zadanie in zadania:
        dane.append(zadanie.to_dict())

    with open("lista_zadan.json", "w", encoding="utf-8") as plik:
        json.dump(dane, plik, ensure_ascii=False, indent=4)