#Kirjoita ohjelma,
#joka hakee ja
#tulostaa satunnaisen
#Chuck Norris -vitsin käyttäjälle.
#Käytä seuravalla sivulla esiteltävää rajapintaa:
#https://api.chucknorris.io/.
#Käyttäjälle on näytettävä pelkkä vitsin teksti.

import requests
#Pyynnön sijastakin voitaisiin kirjoittaa suoraan get() sisälle url
pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyyntö).json()

#en 100% tajua miksi tämän on oltava näin mutta muuten ei toiminut
print(vastaus["value"])
