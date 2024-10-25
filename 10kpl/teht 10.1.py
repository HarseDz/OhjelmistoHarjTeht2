#Kirjoita Hissi-luokka,
# joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen,
# kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen.
# Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja
# käsket sen siirtymään haluamaasi kerrokseen ja
# sen jälkeen takaisin alimpaan kerrokseen.
class hissi:
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

hissi1=hissi(5,-2)
hissi1.hissiliike(5)
hissi1.hissiliike(8)
hissi1.hissiliike(-2)
print()
#hissi1=hissi(1,5)
#print(f"{hissi1.nykyinen} kerroksella")

#kerros = int(input("Anna kerros (MAX 5), kirjoita 0 lopettaaksesi"))
#hissi1.hissiliike(kerros)
#print(f"{hissi1.nykyinen} kerroksella")

#while kerros != 9:
   # if kerros > 0 and kerros <= 5:
   #     kerros = int(input("Anna kerros (MAX 5), kirjoita 0 lopettaaksesi"))
   #     hissi1.hissiliike(kerros)
   #     print(f"{hissi1.nykyinen} kerroksella")
  #  elif kerros != 9:
    #    print(f"{kerros} ei ole olemassa!")
   #     kerros = int(input("Anna kerros (MAX 5), kirjoita 0 lopettaaksesi"))
   #     hissi1.hissiliike(kerros)
    #    print(f"{hissi1.nykyinen} kerroksella")