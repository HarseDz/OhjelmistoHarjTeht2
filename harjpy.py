class Nappula:
    def __init__(self, nimi, arvo, vari, liikerata):
        self.nimi = nimi
        self.arvo = arvo
        self.vari = vari

    def tulostaTiedot(self):
        print(self.nimi, self.arvo)


class Lahetti(Nappula):
    def __init__(self, nimi, arvo, vari, liikerata):
        self.liikerata = liikerata
        super().__init__(nimi, arvo, vari, liikerata)
    def tulostaTiedot(self):
        print(self.liikerata)
        super().tulostaTiedot()

class Torni(Nappula):
    def __init__(self, nimi, arvo, vari, liikerata):
        self.liikerata = liikerata
        super().__init__(nimi, arvo, vari, liikerata)

    def tulostaTiedot(self):
        print(self.liikerata)
        super().tulostaTiedot()

class Daami(Nappula, Torni):
    def __init__(self, nimi, arvo, vari, liikerata):
        self.liikerata = liikerata
        super().__init__(nimi, arvo, vari, liikerata)

class Asema:
    def __init__(self):
        self.rivi1 =[]
        self.rivi2 =[]
        self.rivi3 =[]
        self.rivi4 =[]
        self.rivi5 =[]
        self.rivi6 =[]
        self.rivi7 =[]
        self.rivi8 =[]

    def asetaNappula(self,nappula, sarake):
        if nappula.nimi == "Lahetti" and sarake == "f" and nappula.vari == "valkoinen":
            self.rivi1[2]=nappula
        elif nappula.nimi == "Lahetti" and sarake == "c" and nappula.vari == "valkoinen"::
            self.rivi[5]=nappula
        if nappula.nimi == "Lahetti" and sarake == "f" and nappula.vari == "musta":
            self.rivi1[2] = nappula
        elif nappula.nimi == "Lahetti" and sarake == "c" and nappula.vari == "musta":
            self.rivi[5] = nappula


VL1 = Lahetti("Lahetti", 3, "valkoinen", "diagonaali")
VL2 = Lahetti("Lahett i", 3, "valkoinen", "diagonaali")
ML1 = Lahetti("Lahetti", 3, "valkoinen", "diagonaali")

