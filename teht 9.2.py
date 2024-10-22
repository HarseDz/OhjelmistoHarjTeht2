#Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
# joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa.
# Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta
# suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten,
# että auton nopeutta nostetaan ensin +30 km/h,
# sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus.
# Tee sitten hätäjarrutus määräämällä nopeuden muutos
# -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.
class auto:
    def __init__(self,rekisteri, huippunopeus,hetkinopeus, matka):
        self.rekisteri=rekisteri
        self.huippunopeus=huippunopeus
        self.hetkinopeus=hetkinopeus
        self.matka=matka
    def kiihdytys(self, muutos):
        self.hetkinopeus = self.hetkinopeus + muutos
        if self.hetkinopeus > self.huippunopeus:
            self.hetkinopeus = self.huippunopeus
        elif self.hetkinopeus < 0:
            self.hetkinopeus=0
        else :
            return self.hetkinopeus



auto1 = auto("ABC-123", 142, 30, 0)

auto1.kiihdytys(30)
print(auto1.hetkinopeus)
auto1.kiihdytys(50)
print(auto1.hetkinopeus)
auto1.kiihdytys(70)
print(auto1.hetkinopeus)
auto1.kiihdytys(-200)
print(auto1.hetkinopeus)