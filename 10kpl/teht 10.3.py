#Jatka edellisen tehtävän ohjelmaa siten,
# että Talo-luokassa on parametriton metodi palohälytys,
# joka käskee kaikki hissit pohjakerrokseen.
# Jatka pääohjelmaa siten,
# että talossasi tulee palohälytys.

class Hissi:
    def __init__(self, korkein, alin):
        self.nykyinen = alin
        self.korkein = korkein
        self.alin = alin

    def hissiy(self):
        self.nykyinen += 1
        print(self.nykyinen)

    def hissia(self):
        self.nykyinen -= 1
        print(self.nykyinen)

    def hissiliike(self, kerros):
        if self.nykyinen > kerros and kerros >= self.alin:
            while self.nykyinen != kerros:

                self.hissia()



        elif self.nykyinen < kerros and kerros <= self.korkein:
            while self.nykyinen != kerros:
                self.hissiy()

        else:
            print("Kerros ei real")

class Talo:
    def __init__(self, ylint, alint, hissilkm, tuli):
        self.ylint = ylint
        self.alint = alint
        self.hissilkm = hissilkm
        self.hissit=[]
        self.tuli = tuli
        for i in range(0, self.hissilkm):
            self.hissit.append(Hissi(self.ylint, self.alint))


    def aja(self,hissinro, kerrosmaali):

        hissi=self.hissit[hissinro-1]
        hissi.hissiliike(kerrosmaali)


    def halytys(self, tuli):



def main():
    e = Talo(8,2,2)
    e.aja(1,7)
    e.aja(2, 4)
    tuli == 1
    e.aja(2, 8)
    e.aja(1, 3)
main()