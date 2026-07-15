class KontoBankowe:
    def __init__(self, wlasciciel, saldo):
        self.wlasciciel = wlasciciel
        self.saldo = saldo
        self.historia = []
    
    def pokaz_saldo(self):
        print("Stan konta: ", self.saldo)

    def wplata(self, kwota):
        self.saldo += kwota
        self.historia.append(f"Wpłata: {kwota} zł")
        print("Wpłacono: ", kwota)

    def wyplata(self, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            self.historia.append(f"Wypłata: {kwota} zł")
            print("Wyplacono: ", kwota)
        else:
            print("Brak srodkow na koncie")

    def pokaz_historie(self):
        print("Historia operacji")
        
        for operacja in self.historia:
            print(operacja)
    
    def przelew(self, inne_konto, kwota):
        if kwota <= self.saldo:
            self.saldo -= kwota
            inne_konto.saldo += kwota

            self.historia.append(f"Przelew do {inne_konto.wlasciciel}: {kwota} zl")

            inne_konto.historia.append(f"Przelew od {self.wlasciciel}: {kwota} zl")

            print("Przelew wykonany")
        else:
            print("Brak srodkow na koncie")
            
    def to_dict(self):
        return {
            "wlasciciel": self.wlasciciel,
            "saldo": self.saldo,
            "historia": self.historia
        }

class KontoOszczednosciowe(KontoBankowe):
    def __init__(self, wlasciciel, saldo, oprocentowanie):
        super().__init__(wlasciciel, saldo)
        self.oprocentowanie = oprocentowanie

    def nalicz_odsetki(self):
        odsetki = self.saldo * self.oprocentowanie / 100
        self.saldo += odsetki




