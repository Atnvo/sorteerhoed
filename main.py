import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
import handlers.sorteerhoed as sorteerhoed
import handlers.grafiek as grafiek

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()
print(screen_h, screen_w)
mainClock = pygame.time.Clock()
vragenlijst = sorteerhoed.vragen_ophalen()

# Begin scherm waar de gebruiker zijn naam kan invullen en het spel starten
def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048) 
    pygame.init() 
    textinput = ui.TextInput('Naam: ')
    done = False
    pygame.display.set_caption("Sorteerhoed")
    pygame.display.set_icon(pygame.image.load("assets/images/Sorting_hat.png"))

    # Music
##    pygame.mixer.init()
##    pygame.mixer.music.load('assets\sounds\8bit_harrypotter_theme.mp3')
##    pygame.mixer.music.play(-1)

    # Fonts / text
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)

    # Pygame moet altijd in een loop zitten
    while not done:
        screen.fill((39, 39, 36))
        events = pygame.event.get()

        mouse = pygame.mouse.get_pos()

        start_knop = ui.Button((0, 179, 60), screen_w // 2 - 200, 400, 320, 70, "Start", 20, 0)
        start_knop.draw(mouse, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), screen_w // 2 - 200, 500, 320, 70, "Stop", 20, 0)
        quit_knop.draw(mouse, screen, font_button)

        help_knop = ui.Button((0, 0, 0), screen_w // 2 - 200, 600, 320, 70, "Instructies", 20, 0)
        help_knop.draw(mouse, screen, font_button)

        hoe_werkt_het_knop = ui.Button((0, 0, 0), screen_w // 2 - 200, 700, 320, 70, "Applicatie Informatie", 20, 0)
        hoe_werkt_het_knop.draw(mouse, screen, font_button)


        # Key listerners
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
                menu(textinput.get_text())

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if quit_knop.isOver(mouse):
                exit()
            if start_knop.isOver(mouse):
                menu(ui.TextInput.get_text(textinput).replace('Naam:', ''))
                done = True
            if help_knop.isOver(mouse):
                main_menu = True
                Instructies()
            if hoe_werkt_het_knop.isOver(mouse):
                main_menu = True
                HoeWerktHet()
                
        textinput.update(events)
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Harry potter Sorteerhoed', (221, 211, 147), screen_w // 2 - 550, 220)
        text.draw(screen)  
        screen.blit(textinput.get_surface(), (screen_w // 2 -100, 300))

        pygame.display.flip()
        mainClock.tick(30)

def menu(username):
    main_menu = False
    while not main_menu:
        screen.fill((39, 39, 36))
        
        font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)
        pygame.draw.rect(screen, (39, 39, 36), (0, screen_h-150, screen_w, 150))
        mouse_position = pygame.mouse.get_pos()

        start_knop = ui.Button((200, 179, 60), screen_w // 2 - 200, 400, 320, 70, "Speel", 20, 0)
        start_knop.draw(mouse_position, screen, font_button)

        resultaten_knop = ui.Button((155, 155, 155), screen_w // 2 - 200, 500, 320, 70, "mijn vorige resultaten", 20)
        resultaten_knop.draw(mouse_position, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), screen_w // 2 - 200, 600, 320, 70, "Quit", 20, 0)
        quit_knop.draw(mouse_position, screen, font_button)

        mainmenu_knop = ui.Button((255, 255, 255), 700, 150, 80, 35, "Hoe werkt het", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, pygame.font.Font("assets/fonts/pixel2.ttf", 20))


        # Key listerners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                main_menu = True

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if start_knop.isOver(mouse_position):
                main_menu = True
                menu_vraag(username)
            if resultaten_knop.isOver(mouse_position):
                main_menu = True
                toon_resultaten(username)
            if quit_knop.isOver(mouse_position):
                main_menu = True
        

        pygame.display.flip()
        mainClock.tick(60)


def HoeWerktHet():
    done = False
    while not done:
        screen.fill((39, 39, 36))
        events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()
 
        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, (pygame.font.Font("assets/fonts/lunchds.ttf", 20)))

        # Key listerners
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
                menu(textinput.get_text())

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                done = True
                main()

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Applicatie Informatie.', (221, 211, 147), screen_w // 2 - 800, 220)
        text.draw(screen)  

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '1) Je selecteerd een antwoord.', (255, 255, 255), screen_w // 2 - 800, 500)
        text.draw(screen) 
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '2) Je antwoord wordt opgelslagen.', (255, 255, 255), screen_w // 2 - 800, 550)
        text.draw(screen) 
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '3) De antwoorden zijn gerelateerd aan een specialisatie. ', (255, 255, 255), screen_w // 2 - 800, 600)
        text.draw(screen) 
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '4) Er wordt met een percentage berekent welke specialisatie bij jou past.', (255, 255, 255), screen_w // 2 - 800, 650)
        text.draw(screen) 

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False,'Gemaakt door: INFV1', (255, 255, 255), screen_w // 2 - 800, 1000)
        text.draw(screen) 

        pygame.display.flip()
        mainClock.tick(30)

def Instructies():
    done = False
    while not done:
        screen.fill((39, 39, 36))
        events = pygame.event.get()
        mouse_position = pygame.mouse.get_pos()
 
        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, (pygame.font.Font("assets/fonts/lunchds.ttf", 20)))

        # Key listerners
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                done = True
                main()
                

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Instructies', (221, 211, 147), screen_w // 2 - 800, 220)
        text.draw(screen)  

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '1) Je selecteert een antwoord door erop te klikken.  ', (255, 255, 255), screen_w // 2 - 800, 500)
        text.draw(screen)  
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '2) Om opnieuw te beginnen moet je op "terug" drukken en daarna op "speel".', (255, 255, 255), screen_w // 2 - 800, 550)
        text.draw(screen)  
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 30), False, '3) Om het resultaat van de laatste speler te zien druk op "terug" en daarna op "mijn vorige resultaten".', (255, 255, 255), screen_w // 2 - 800, 600)
        text.draw(screen) 
        

        pygame.display.flip()
        mainClock.tick(30)

# Pagina om de resultaten te bekijken
def toon_resultaten(username):
    resultaten = sorteerhoed.resultaten_ophalen(username)

    toon_resultaten = True
    while toon_resultaten:
        screen.fill((39, 40, 34))

        spec_image_badge = "assets/images/" + resultaten['specialisatie'] + '.png'
        spec_image = pygame.image.load(spec_image_badge)
        spec_image_rect = spec_image.get_rect()
        spec_image_rect.x, spec_image_rect.y = screen_w // 2 - spec_image_rect.width // 2, 100

        text = ui.Text(pygame.font.Font("assets/fonts/fantasy.ttf", 80), False, username, (221, 211, 147), screen_w // 2 - 125, 400)
        text.draw(screen)  

        mouse_position = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                toon_resultaten = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                toon_resultaten = False

        # Menu knoppen
        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, pygame.font.Font("assets/fonts/pixel2.ttf", 20))

        grafiek_knop = ui.Button((249, 44, 44), 200, 200, 150, 35, "Zie grafiek", 20, 0)
        grafiek_knop.draw(mouse_position, screen, pygame.font.Font("assets/fonts/pixel2.ttf", 20))

        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                toon_resultaten = False
                menu(username)
            if grafiek_knop.isOver(mouse_position):
                toon_resultaten = False
                grafiek.pi(sorteerhoed.resultaten_ophalen(username))
                
        screen.blit(spec_image, spec_image_rect)

        pygame.display.flip()
        mainClock.tick(60)

# Vragen loop
def menu_vraag(username):
    count = 0
    running = True
    teller = [0, 0, 0, 0]
    totaal = [0, 0, 0, 0]
    for count, vraag in enumerate(vragenlijst):
        while running:
            screen.fill((39, 40, 34))
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            # btns = ui.vraag_component( vragenlijst['vraag'][count], [vragenlijst['ant1'][count], vragenlijst['ant2'][count], vragenlijst['ant3'][count], vragenlijst['ant4'][count]] )
            btns = ui.vraag_component( vragenlijst['vraag'][count], [vragenlijst['ant1'][count], vragenlijst['ant2'][count], vragenlijst['ant3'][count], vragenlijst['ant4'][count]],
            [ vragenlijst['spec_ant1'][count], vragenlijst['spec_ant2'][count], vragenlijst['spec_ant3'][count], vragenlijst['spec_ant4'][count] ])
                
            if pygame.mouse.get_pressed()[0]:
                for i, btn in enumerate(btns):
                    punten = list(btn.get_spec()[i].replace(',', ''))
                    for i in range(0,4):
                        totaal[i] += int(punten[i])
                        if btn.isOver(pygame.mouse.get_pos()):
                            count += 1
                            pygame.event.wait()
                            punten = list(btn.get_spec()[i].replace(',', ''))
                            for i in range(0,4):
                                teller[i] += int(punten[i])
                            
                        # Punt volgorde = IAT, FICT, SE, BDaM
        

            if count == 12:
                    #Manier van uitrekenen: om iedere specialisatie evenveel kans te geven berekenen we het percentage door
                    #het 'gekozen' puntenaantal per specialisatie te delen door het totale puntenaantal van die
                    #specialisatie. Dit om te voorkomen dat er in totaal meer punten aan één specialisatie toegekend
                    #worden en de kans dus groter is dat die specialisatie de uitslag is.

                percentage = []
                for i in range(0,4):
                    print(teller[i], totaal[i])
                    percentage.append(teller[i] / totaal[i])
                print("IAT: " + str(percentage[0]) + "FICT: " + str(percentage[1]) + "SE: " + str(percentage[2]) + "BDam: " + str(percentage[3]))
                # sorteerhoed.resultaten_opslaan([username, percentage[0], percentage[1], percentage[2], percentage[3]])
                running = False
                eind_vraag(username)


            # Menu knoppen
            mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
            mainmenu_knop.draw(mouse_position, screen, (pygame.font.Font("assets/fonts/lunchds.ttf", 20)))
            counter = str(count+1) + " / 12" 
            vraag_nr = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 20), False, counter , (225, 225, 225), screen_w // 2 - 650, 250)
            vraag_nr.draw(screen)

            if pygame.mouse.get_pressed()[0]:
                if mainmenu_knop.isOver(mouse_position):
                    running = False
                    menu(username)
                
                if mainmenu_knop.isOver(mouse_position):
                    running = False
                    menu(username)

            pygame.display.flip()
            mainClock.tick(60)

# de pagina na het einde van de quiz.
def eind_vraag(username):
    eind_vraag = True
    while eind_vraag:
        screen.fill((39, 40, 34))

        text = ui.Text(pygame.font.Font("assets/fonts/fantasy.ttf", 80), False, 'Einde Quiz', (221, 211, 147), screen_w // 2 - 200, 400)
        text.draw(screen)  

        mouse_position = pygame.mouse.get_pos()

        sorting_hat = pygame.image.load("assets/images/Sorting_hat.gif")
        sorting_hat_rect = sorting_hat.get_rect()
        sorting_hat_rect.x, sorting_hat_rect.y = screen_w // 2 - sorting_hat_rect.width // 2, 100
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                eind_vraag = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                eind_vraag = False

        # Menu knoppen
        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, pygame.font.Font("assets/fonts/pixel2.ttf", 20))

        resultaten_knop = ui.Button((0, 204, 0), screen_w // 2 - 200, 575, 320, 70, "Bekijk mijn resultaten", 20)
        resultaten_knop.draw(mouse_position, screen, pygame.font.Font("assets/fonts/pixel2.ttf", 20))

        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                eind_vraag = False
                menu(username)
            if resultaten_knop.isOver(mouse_position):
                eind_vraag = False
                toon_resultaten(username)

        screen.blit(sorting_hat, sorting_hat_rect)

        pygame.display.flip()
        mainClock.tick(60)
            


if __name__ == '__main__':
    main()
