#Laajenna ohjelmaa siten,
# että mukana on kulje-metodi,
# joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran
# kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h.
# Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
class auto:
    def __init__(self,rekisteri, huippunopeus,hetkinopeus, matka, kulje):
        self.rekisteri=rekisteri
        self.huippunopeus=huippunopeus
        self.hetkinopeus=hetkinopeus
        self.matka=matka
        self.kulje=kulje

    def kuljepa(self):
        self.matka = self.matka + self.hetkinopeus * self.kulje
        return self.matka

auto1 = auto("ABC-123", 142, 60, 2000, 1.5)
auto1.kuljepa()
print(auto1.matka)