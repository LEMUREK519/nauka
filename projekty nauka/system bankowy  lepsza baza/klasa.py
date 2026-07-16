class KontoBankowe:
    def __init__(self, wlasciciel, saldo, id_konta=None):
        self.id = id_konta
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        self.historia = []
    
    def pokaz_saldo(self):
        print("Stan konta: ", self.saldo)

    def wplata(self, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od zera")
            return False

        self.saldo += kwota
        self.historia.append(f"Wpłata: {kwota} zł")
        print("Wpłacono: ", kwota)
        return True

    def wyplata(self, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od zera")
            return False
        
        if kwota <= self.saldo:
            self.saldo -= kwota
            self.historia.append(f"Wypłata: {kwota} zł")
            print("Wyplacono: ", kwota)
            return True
        else:
            print("Brak srodkow na koncie")
            return False

    def pokaz_historie(self):
        print("Historia operacji")
        
        if len(self.historia) == 0:
            print("Brak operacji")
            return

        for operacja in self.historia:
            print(operacja)
    
    def przelew(self, inne_konto, kwota):
        if kwota <= 0:
            print("Kwota nie moze byc mniejsza od 0")
            return False

        if kwota <= self.saldo:
            self.saldo -= kwota
            inne_konto.saldo += kwota

            self.historia.append(f"Przelew do {inne_konto.wlasciciel}: {kwota} zl")

            inne_konto.historia.append(f"Przelew od {self.wlasciciel}: {kwota} zl")

            print("Przelew wykonany")
            return True
        else:
            print("Brak srodkow na koncie")
            return False
    




