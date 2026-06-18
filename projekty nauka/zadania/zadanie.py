
class Zadanie:
    def __init__(self, tytul, opis, wykonane=False):
        self.tytul = tytul
        self.opis = opis
        self.wykonane = wykonane

    def pokaz_info(self):
        if self.wykonane:
            status = "wykonane"
        else:
            status = "niewykonane"

        print(self.tytul, "- ", self.opis, "-", status)

    def to_dict(self):
        return {
            "tytul": self.tytul,
            "opis": self.opis,
            "wykonane": self.wykonane
        }