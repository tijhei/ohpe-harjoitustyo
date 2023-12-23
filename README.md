# ohpe-harjoitustyo

-Työn aihe ja kuvaus-

Ohjelma on yksinkertainen peli, jossa voi ohjata bändin (sähkö)kitaristia ja kuunnella musiikkia.



-Työn ratkaisuperiaate-

Peli pyörii Pygame-kirjastolla. Peli sisältää animaatioita, joiden pixel art -kuvat ovat tuotettu tietokoneella paint.net-ohjelmiston avulla.



-Työn rakenne-

Ohjelmakoodin alussa on alustusvaiheet, kuten Pygame-kirjaston alustus ja vakioarvojen asettaminen. Seuraavaksi on peli-ikkunan luominen ja kuvien sekä äänien lataaminen. Tämän jälkeen on funktiot animaatioille, kuten kitaristin liikuttaminen ja erikoisanimaation toistaminen. Pääohjelma koostuu silmukasta, jossa käsitellään tapahtumia, päivitetään pelitilannetta ja renderöidään käyttöliittymäteksti.



-Käytetyt funktiot-

vaihda_sallinen(salli, direction): Vastuussa kitaristin animaatiosta
sallinenSpecial(duration): Vastuussa erikoisanimaation toistamisesta
vaihda_tausta(x): Vastuussa taustakuvan vaihtamisesta eli toisin sanoen vastuussa taustalla pyörivän animaation pyörittämisesti 

Ohjelmassa hyödynnetään myös lukuisia muita funktiota, jotka ovat kirjastojen ennaltamäärittämiä. Esimerkiksi Pygame-kirjaston funktioita screen.blit(...) ja  pygame.image.load(...).


-Mahdollisten ulkoisten kirjastojen käyttö-

Pygame-kirjasto, jota käytetään lähinnä 2D-pelien luontiin Pythonilla.



-Ohjeet "pelin" pelaamiseen-

Paina 'T' kuunnellaksesi kappale 'Toivioretkellä'.
Paina 'X' kuunnellaksesi erikoiskitarariffiä.
Kitaristi liikkuu automaattisesti oikealle tai vasemmalle.
Erikoisanimaatio käynnistyy painamalla 'X' ja kitaristi lakkaa liikkumasta tänä aikana.
