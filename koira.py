class Koira:
    def __init__(self, nimi, syntymavuosi, haukahdus):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        print(f"{self.nimi} haukkuu seuraavasti: ")
        for i in range(kerrat):
            print(f"{self.haukahdus} {i+1} kerran.")
        return
    def annaNimi(self):
        return self.nimi
koira1 = Koira("Muro", 2018, "Vuh Vuh")
koira2 = Koira("Rekku", 2022, "Viu viu viu")
#koira = Koira("Rekku", 2022)
#tuntikoira = Koira("Laikku", 2011)
#print(f"{koira1.nimi} on syntynyt vuonna {koira1.syntymavuosi}.")
#print(hauku(1))
# koira1.hauku(2)
# koira2.hauku(5)
# print(f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}.")
# print(f"{tuntikoira.nimi:s} on syntynyt vuonna {tuntikoira.syntymavuosi:d}.")
print(koira1.annaNimi())