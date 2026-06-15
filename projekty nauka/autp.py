class Auto:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def show_info(self):
        print(self.marka, "-", self.model, "-", self.rok)
    
    def age_car(self):
        age = 2026 - self.rok
        print("Age of car:", age)

auto1 = Auto("Audi", "Rs5", 2022)
auto2 = Auto("Bmw", "X7", 2023 )
auto3 = Auto("Honda", "Civic", 2024)

auto1.show_info()
auto1.age_car()

auto2.show_info()
auto2.age_car()

auto3.show_info()
auto3.age_car()