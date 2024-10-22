#Nyt ohjelmoidaan autokilpailu.
# Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista,
# joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1",
# "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

#Jokaisen auton nopeutta muutetaan siten,
# että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan.
# Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu,
# kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
import random
autot = []
class Auto:
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

    def kuljepa(self,aika):
        self.matka = self.matka + self.hetkinopeus * aika
        return self.matka

def randomhn():
    return random.randint(100,200)

def randomkiihd():
    return random.randint(-10,15)

def main():

    for i in range(0,10):
        luotu_auto=Auto(f"Fiat Punto 200{i}", randomhn(), 0, 0)
        autot.append(luotu_auto)

    while True:
        for i in range(0,10):
            autot[i].kiihdytys(randomkiihd())
            autot[i].kuljepa(1)
            if autot[i].matka >= 10000:
                #print(autot[i].rekisteri, autot[i].huippunopeus, autot[i].matka)
                for f in range(0,10):
                    print(f"{autot[f].rekisteri}, top speed {autot[f].huippunopeus} kmh, {autot[f].matka} meters")
                exit()
#def printx():
   # for i in range(0,10):
      #  print(autot[i].rekisteri + autot[i].huippunopeus + autot[i].matka)
main()
#printx()





