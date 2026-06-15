import json

def wczytaj_z_pliku():
    try:
        with open("koszyk.json", "r", encoding="utf-8") as plik:
            return json.load(plik)
    except FileNotFoundError:
        return {}
    
def zapisz_do_pliku():
    with open("koszyk.json", "w", encoding = "utf-8") as plik:
        json.dump(koszyk, plik, ensure_ascii = False, indent = 4)

koszyk = wczytaj_z_pliku()

def panel_startowy():
    print()
    print("1. Dodaj produkt")
    print("2. Pokaż listę")
    print("3. Usuń produkt")
    print("4. Zakończ")
    print("5. Wyczysc koszyk")

def dodaj_produkt():
    produkt = input("Podaj produkt: ").strip()
    
    
    if produkt in koszyk:
        koszyk[produkt] += 1
    else:
        koszyk[produkt] = 1
    
    zapisz_do_pliku()
    print("Dodano: ", produkt)

def lista_zakupow():
    print()
    print("Lista zakupów ")
    
    if len(koszyk) ==0:
        print("nic tu nie ma")
        return
    
    for produkt, ilosci in koszyk.items():
        print("-", produkt, "x", ilosci)

def usuwanie():
    if len(koszyk) == 0:
        print()
        print("Koszyk jest pusty")
        return

    lista_zakupow()

    produkt = input("Co usunac? ")

    if produkt in koszyk:
        if koszyk[produkt] > 1:
            koszyk[produkt] -= 1
            print("Zmniejszono ilość:", produkt)
        else:
            del koszyk[produkt]
            print("Usunieto:", produkt)

        zapisz_do_pliku()

    else:
        print("Nie ma tego w koszyku")

def wyczysc_koszyk():
    if len(koszyk) == 0:
        print("Koszyk już jest pusty")
        return

    decyzja = input("Czy na pewno wyczyścić koszyk? tak/nie: ")

    if decyzja == "tak":
        koszyk.clear()
        zapisz_do_pliku()
        print("Wyczyszczono koszyk")
    else:
        print("Anulowano")

while True:
    panel_startowy()
    
    wybor = input("Wybierz opcję ")

    if wybor == "1":
        dodaj_produkt()
    
    elif wybor == "2":
        lista_zakupow()
    
    elif wybor =="3":
        usuwanie()

    elif wybor == "4":
        print("Koniec zakupow")
        break

    elif wybor == "5":
        wyczysc_koszyk()

    else:
        print()
        print("Nieznana opcja")




