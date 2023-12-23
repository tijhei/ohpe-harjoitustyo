import pygame
import sys

# Alustetaan pygame
pygame.init()

# Asetetaan vakioita: näytön korkeus ja leveys sekä mustan ja valkoisen RGB-tunnisteet helpottaakseen myöhempää koodin kirjoitusta
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Luo peli-ikkuna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Soittohuone :D")

# Lataa kuvat ja äänet
bg_image1 = pygame.image.load("still1.png") # Tausta pose nro. 1
bg_image2 = pygame.image.load("still2.png") # Tausta pose nro. 2
bg_image3 = pygame.image.load("still3.png") # Tausta pose nro. 3
bg_image4 = pygame.image.load("still4.png") # Tausta pose nro. 4
demo_sound = pygame.mixer.Sound("maailman_kautta_kuljemme_laulain.wav")
la_paloma = pygame.mixer.Sound("la_paloma.wav")

# Asetetaan taustan sijaintivakiot
bg_x = WIDTH // 2
bg_y = HEIGHT

# Asetetaan fontti
font = pygame.font.Font(None, 36)

salli1 = pygame.image.load("mestari_sallinen1.png")  # Kitaristi Sällisen pose nro. 1
salli2 = pygame.image.load("mestari_sallinen2.png")  # Kitaristi Sällisen pose nro. 2

salliSpecial1 = pygame.image.load("sallinen_special1.png")  # Spessu pose nro. 1
salliSpecial2 = pygame.image.load("sallinen_special2.png")  # Spessu pose nro. 2
salliSpecial3 = pygame.image.load("sallinen_special3.png")  # Spessu pose nro. 3

image_rect = salli1.get_rect() # Kitaristin koko pelissä

x, y = WIDTH // 2 - image_rect.width // 2, HEIGHT // 2 - image_rect.height // 2 + 130 # Kitaristin sijainti pelissä
speed = 15 # Kitaristin kävelynopeus
direction = 1 # 1 kulkee oikealle, -1 vasemmalle

#Animaatiofunktio
def vaihda_sallinen(salli, direction):

    flippedSallinen1 = pygame.transform.flip(salli1, True, False) #Vasemmalle kävellessä käännä kuva
    flippedSallinen2 = pygame.transform.flip(salli2, True, False) #Vasemmalle kävellessä käännä kuva
    if direction == 1:
        if salli == 0:
            screen.blit(salli1, (x, y))
        else:
            screen.blit(salli2, (x, y))
            salli = -1
        salli += 1
    else:
        if salli == 0:
            screen.blit(flippedSallinen1, (x, y))
        else:
            screen.blit(flippedSallinen2, (x, y))
            salli = -1
        salli += 1

    return salli

#Pyörittää spessuanimaatiota
def sallinenSpecial(duration):

    if duration % 29 == 0:
        screen.blit(salliSpecial1, (x, y))
    elif duration % 4 == 0:
        screen.blit(salliSpecial2, (x, y))
    elif duration % 2 == 0:
        screen.blit(salliSpecial3, (x, y))
    elif duration % 1 == 0:
        screen.blit(salliSpecial2, (x, y))
    else:
        screen.blit(salliSpecial1, (x, y))


#Vaihda tausta, eli toisin sanoen pyöritä animaatiota
def vaihda_tausta(x):
    
    if x == 0:
        screen.blit(bg_image1, (bg_x - bg_image1.get_width() // 2, bg_y - bg_image1.get_height()))
    elif x == 1:
        screen.blit(bg_image2, (bg_x - bg_image2.get_width() // 2, bg_y - bg_image2.get_height()))
    elif x == 2:
        screen.blit(bg_image3, (bg_x - bg_image3.get_width() // 2, bg_y - bg_image3.get_height()))
    else:
        screen.blit(bg_image4, (bg_x - bg_image4.get_width() // 2, bg_y - bg_image4.get_height()))
        x = -1
    x += 1

    return x


sallinenSpecialDuration = 30 # Määrittää kuinka monta kertaa sallinenSpecial() -funktiota kutsutaan (montako framea näytetään yhteensä spessun kohalla)
sallinenSpecialAbility = False
salli = 0 # Apumuuttuja vaihda_sallinen() -funktiota varten
kuva = 0 # Apumuuttuja vaihda_tausta() -funktiota varten

# Itse pelin silmukka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                demo_sound.play()
            if event.key == pygame.K_x:
                sallinenSpecialAbility = True
                la_paloma.play()
            
            
    x += speed * direction

    if x <= 0 or x >= WIDTH - image_rect.width:
        direction *= -1 # Vaihtaa kulkusuunnan, jos kitaristi liikuu liian paljon vasemmalle tai oikealle.


    if sallinenSpecialAbility == False:

        # Näytä tausta
        kuva = vaihda_tausta(kuva)

        # Bring in the Sällinen
        salli = vaihda_sallinen(salli, direction)

    

    if sallinenSpecialAbility == True:
        
        vaihda_tausta(0) # Laita taustaksi aina sama kuva, kun erikoisanimaatio toistuu. Nyt muut eivät soita samalla kun La Paloma soi.
        speed = 0 # Liikkumisnopeus nollakso animaation ajaksi

        if sallinenSpecialDuration == 0:
            
            sallinenSpecialAbility = False
            sallinenSpecialDuration = 30
            speed = 15

        else:
            sallinenSpecialDuration -= 1

        sallinenSpecial(sallinenSpecialDuration)
        

    # Renderöi käyttöliittymän teksti
    text_color = WHITE
    gui_text = [
        "Paina 'T' kuunnellaksesi kappale 'Toivioretkellä'",
        "Paina 'X' kuunnellaksesi sairas kitarariffi"
    ] # Käytetään listaa, niin kuin tehtävänannossa käskettiin

    for i, text in enumerate(gui_text):
        text_surface = font.render(text, True, text_color)
        screen.blit(text_surface, (10, 10 + i * 40))

    pygame.display.flip()

    # Asetetaan animaatioiden nopeus
    pygame.time.Clock().tick(6)