import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
import handlers.sorteerhoed as sorteerhoed

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()
mainClock = pygame.time.Clock()
vragenlijst = sorteerhoed.vragen_ophalen()
username = ""

def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init() 
    pygame.display.set_caption("Sorteerhoed")
    pygame.display.set_icon(pygame.image.load("assets/images/icon.png"))

    done = False

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load('assets\sounds\8bit_harrypotter_theme.mp3')
    pygame.mixer.music.play(-1)

    # Fonts / text
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)
    TextInput = ui.TextInput()

    while not done:
        pygame.event.wait()
        
        screen.fill((39, 39, 36))
        mouse_position = pygame.mouse.get_pos()
        events = pygame.event.get()
        
        start_knop = ui.Button((0, 179, 60), screen_w // 2 - 200, 400, 320, 70, "Start", 20, 0)
        start_knop.draw(mouse_position, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), screen_w // 2 - 200, 500, 320, 70, "Quit", 20, 0)
        quit_knop.draw(mouse_position, screen, font_button)

        TextInput.update(events)
        # Key listerners
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if quit_knop.isOver(mouse_position):
                done = True
            if start_knop.isOver(mouse_position):
                username = TextInput.get_text()
                done = True
                menu()
                
        screen.blit(TextInput.get_surface(), (screen_w // 2 - 100, 300))

        pygame.display.update()
        mainClock.tick(30)

def menu():
    main_menu = False
    while not main_menu:
        screen.fill((39, 39, 36))
        
        font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)
        pygame.draw.rect(screen, (39, 39, 36), (0, screen_h-150, screen_w, 150))
        mouse_position = pygame.mouse.get_pos()

        speel_knop = ui.Button((0, 179, 60), screen_w // 2 - 200, 400, 320, 70, "Speel", 20, 0)
        speel_knop.draw(mouse_position, screen, font_button)

        resultaten_knop = ui.Button((155, 155, 155), screen_w // 2 - 200, 500, 320, 70, "mijn vorige resultaten", 20)
        resultaten_knop.draw(mouse_position, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), screen_w // 2 - 200, 600, 320, 70, "Quit", 20, 0)
        quit_knop.draw(mouse_position, screen, font_button)

        # Key listerners
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True

        # Menu button click events
        if pygame.mouse.get_pressed()[0]:
            if speel_knop.isOver(mouse_position):
                main_menu = True
                menu_vraag()
            if resultaten_knop.isOver(mouse_position):
                main_menu = True
                toon_resultaten(username)
            if quit_knop.isOver(mouse_position):
                main_menu = True
                
        # screen.blit(title_image, title_image_rect)

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

        text = ui.Text(pygame.font.Font("assets/fonts/fantasy.ttf", 80), False, resultaten['naam'], (221, 211, 147), screen_w // 2 - 125, 400)
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
                menu()
                
        screen.blit(spec_image, spec_image_rect)

        pygame.display.update()
        mainClock.tick(60)

def menu_vraag():
    running = True
    while running:
        screen.fill((39, 40, 34))

        font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)
        mouse_position = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 50, 40, "X", 20, 0)
        mainmenu_knop.draw(mouse_position, screen, font_button)

        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                running = False
                menu()

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Vraag 1.', (221, 211, 147), screen_w // 3.5, 50)
        text.draw(screen)   

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 20), False, 'Geef aan welke van de volgende opties het beste bij he past', (221, 211, 147), 400, 200)
        text.draw(screen) 

        selectie_knop = ui.Button((0, 179, 60), 400, 250, 50, 50, 'A', 30, 0)
        selectie_knop.draw(mouse_position, screen, font_button)

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 20), False, "Ik houd van puzzelen", (221, 211, 147), 450, 250)
        text.draw(screen)  

        pygame.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    main()

