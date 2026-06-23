class Kontakt:
    def __init__(self, imie, telefon, email, wykonane=False):
        self.imie = imie
        self.telefon = telefon
        self.email = email
        self.wykonane = wykonane
        
    def pokaz_info(self):
        if self.wykonane:
            status = "wykonane" 
        else:
            status = "niewykonane"
            
            print(self.imie, "-", self.telefon, "-", self.email, "-", status)
        
    def to_dict(self):
        return {
            "imie": self.imie,
            "telefon": self.telefon,
            "email": self.email,
            "wykonane": self.wykonane
        }