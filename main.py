import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
import handlers.sorteerhoed as sorteerhoed

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()
print(screen_h, screen_w)
mainClock = pygame.time.Clock()
vragenlijst = sorteerhoed.vragen_ophalen()

def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init() 
    textinput = ui.TextInput('Naam: ')
    done = False
    pygame.display.set_caption("Sorteerhoed")
    pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load('assets\sounds\8bit_harrypotter_theme.mp3')
    pygame.mixer.music.play(-1)

    # Fonts / text
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)

    while not done:
        screen.fill((39, 39, 36))
        events = pygame.event.get()

        mouse = pygame.mouse.get_pos()

        start_knop = ui.Button((0, 179, 60), screen_w // 2 - 200, 400, 320, 70, "Start", 20, 0)
        start_knop.draw(mouse, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), screen_w // 2 - 200, 500, 320, 70, "Stop", 20, 0)
        quit_knop.draw(mouse, screen, font_button)

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
                
        textinput.update(events)
        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Harry potter Sorteerhoed', (221, 211, 147), screen_w // 2 - 550, 220)
        text.draw(screen)  
        screen.blit(textinput.get_surface(), (screen_w // 2 -100, 300))

        pygame.display.update()
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

        pygame.display.update()
        mainClock.tick(60)

# Pagina om de resultaten te bekijken
def toon_resultaten(username):
    resultaten = sorteerhoed.resultaten_ophalen(username)

    running = True
    while running:
        screen.fill((39, 40, 34))

        spec_image_badge = "assets/images/" + resultaten['specialisatie'] + '.png'
        spec_image = pygame.image.load(spec_image_badge)
        spec_image_rect = spec_image.get_rect()
        spec_image_rect.x, spec_image_rect.y = screen_w // 2 - spec_image_rect.width // 2, 100

        text = ui.Text(pygame.font.Font("assets/fonts/fantasy.ttf", 80), False, username, (221, 211, 147), screen_w // 2 - 125, 400)
        text.draw(screen)  

        font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)
        mouse_position = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        # Menu knoppen
        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, font_button)

        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                running = False
                menu(username)
                
        screen.blit(spec_image, spec_image_rect)

        pygame.display.update()
        mainClock.tick(60)

def menu_vraag(username):
    running = True
    for count, vraag in enumerate(vragenlijst):
        while running:
            screen.fill((39, 40, 34))
            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            # Menu knoppen
            mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 80, 35, "Terug", 20, 0)
            mainmenu_knop.draw(mouse_position, screen, (pygame.font.Font("assets/fonts/lunchds.ttf", 20)))

            index = 0
            btns = toon_vraag(index)
                
            if pygame.mouse.get_pressed()[0]:
                for btn in btns:
                    if btn.isOver(mouse_position):
                        screen.fill((39, 40, 34))
                        index = index + 1
                        toon_vraag(index)
                if mainmenu_knop.isOver(mouse_position):
                    running = False
                    menu(username)

            pygame.display.update()
            mainClock.tick(30)

def toon_vraag(count):
    btns = [ [vragenlijst['ant1'][count], vragenlijst['ant2'][count], vragenlijst['ant3'][count], vragenlijst['ant4'][count] ]
    return ui.vraag_component(vragenlijst['vraag'][count], btns)



if __name__ == '__main__':
    main()

