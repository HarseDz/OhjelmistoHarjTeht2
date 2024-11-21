#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto
# ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena
# akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on
# bensatankin koko litroina.
# Kirjoita aliluokille alustajat.
# Esimerkiksi sähköauton alustaja
# saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin.
# Se kutsuu yliluokan alustajaa kahden
# ensin mainitun asettamiseksi sekä asettaa
# oman kapasiteettinsa. Kirjoita pääohjelma,
# jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton
# (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran
# ja tulosta autojen matkamittarilukemat.

class Auto:
    def __init__(self,rekisteri, huippunopeus, matka=0):
        self.rekisteri=rekisteri
        self.matka=matka
        self.huippunopeus=huippunopeus


    def kuljepa(self, kulje):
        self.matka = self.matka + self.huippunopeus * kulje

    def tulosta_tiedot(self):
        print(f"{self.rekisteri}")

class Sahko(Auto):

    def __init__(self,rekisteri, huippunopeus, matka, kWh):
        self.kWh=kWh
        super().__init__(rekisteri, huippunopeus, matka)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"sähkoauto specs: {self.kWh}, {self.huippunopeus}km/h matka on: {self.matka}km")


class DIZEL(Auto):

    def __init__(self,rekisteri, huippunopeus, matka, litr):
        self.litr=litr
        super().__init__(rekisteri, huippunopeus, matka)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"DIZELauto specs: {self.litr}, {self.huippunopeus}km/h matka on: {self.matka} km")


matkat = []
matkat.append(Sahko("ABC-15", 180, 0, "52.5 kWh" ))
matkat.append(DIZEL("ACD-123", 165, 0, "32.5L TDI 1.4L"))

for t in matkat:
    t.kuljepa(3)
    t.tulosta_tiedot()