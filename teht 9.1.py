#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja,
# joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton
# (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class auto:
    def __init__(self,rekisteri, huippunopeus,hetkinopeus=0, matka=0):
        self.rekisteri=rekisteri
        self.huippunopeus=huippunopeus
        self.hetkinopeus=hetkinopeus
        self.matka=matka


auto1= auto( "ABC-123", "142 kmh")
print(f"{auto1.rekisteri} {auto1.huippunopeus}")