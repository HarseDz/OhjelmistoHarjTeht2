#Toteuta seuraava luokkahierarkia Python-kielellä:
# Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi.
# Kirjalla on lisäksi kirjoittaja ja sivumäärä,
# kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat.
# Tee aliluokkiin metodi tulosta_tiedot,
# joka tudostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka
# (päätoimittaja Aki Hyyppä) ja Hytti n:o 6
# (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:

    julkaisujen_lukumäärä = 0

    def __init__(self, nimi):
        Julkaisu.julkaisujen_lukumäärä = Julkaisu.julkaisujen_lukumäärä + 1
        self.julkaisunumero = Julkaisu.julkaisujen_lukumäärä
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f"{self.julkaisunumero}: {self.nimi}")

class Kirja(Julkaisu):

    def __init__(self,nimi, kirjoittaja, sivumäärä):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):

    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Päätoimittaja: {self.päätoimittaja}")


julkaisut = []
julkaisut.append(Lehti("Aku Ankka", "Aki Hyyppä"))
julkaisut.append(Kirja("Hytti no. 6", "Rosa Liksom", 250))

for t in julkaisut:
    t.tulosta_tiedot()