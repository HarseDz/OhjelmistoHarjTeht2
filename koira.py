class Koira:
    def __init__(self, nimi, syntymavuosi):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi

koira = Koira("Rekku", 2022)
tuntikoira = Koira("Laikku", 2011)

print(f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}.")
print(f"{tuntikoira.nimi:s} on syntynyt vuonna {tuntikoira.syntymavuosi:d}.")