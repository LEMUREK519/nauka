class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        self.historia = []
    
    def pokaz_saldo(self):
        print("Stan konta: ", self.saldo)

    def wplata(self, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od zera")
            return

        self.saldo += kwota
        self.historia.append(f"Wpłata: {kwota} zł")
        print("Wpłacono: ", kwota)

    def wyplata(self, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od zera")
            return
        
        if kwota <= self.saldo:
            self.saldo -= kwota
            self.historia.append(f"Wypłata: {kwota} zł")
            print("Wyplacono: ", kwota)
        else:
            print("Brak srodkow na koncie")

    def pokaz_historie(self):
        print("Historia operacji")
        
        if len(operacja) == 0:
            print("Brak operacji")
            return
        
        for operacja in self.historia:
            print(operacja)
    
    def przelew(self, inne_konto, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od 0")
            return
        
        if kwota <= self.saldo:
            self.saldo -= kwota
            inne_konto.saldo += kwota

            self.historia.append(f"Przelew do {inne_konto.wlasciciel}: {kwota} zl")

            inne_konto.historia.append(f"Przelew od {self.wlasciciel}: {kwota} zl")

            print("Przelew wykonany")
        else:
            print("Brak srodkow na koncie")
    




