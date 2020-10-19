import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
import handlers.sorteerhoed as sorteerhoed

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()
mainClock = pygame.time.Clock()
vragenlijst = sorteerhoed.vragen_ophalen()

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

    # Logo imagew
    title_image = pygame.image.load("assets/images/logo.png")
    title_image_rect = title_image.get_rect()
    title_image_rect.x, title_image_rect.y = screen_w // 4, 20

    # Fonts / text
    font_title = pygame.font.Font("assets/fonts/harry.ttf", 140)
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)

    # title = font_title.render("Harrypotter", True, (221, 211, 147))

    while not done:
        pygame.event.wait()
        
        screen.fill((39, 39, 54))
        pygame.draw.rect(screen, (39, 39, 36), (0, screen_h-150, screen_w, 150))
        mouse_position = pygame.mouse.get_pos()

        speel_knop = ui.Button((0, 179, 60), 550, 400, 320, 70, "Speel", 20)
        speel_knop.draw(mouse_position, screen, font_button)

        resultaten_knop = ui.Button((155, 155, 155), 550, 500, 320, 70, "mijn vorige resultaten", 20)
        resultaten_knop.draw(mouse_position, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), 550, 600, 320, 70, "Quit", 20)
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
                done = True
                menu_vraag()
            if quit_knop.isOver(mouse_position):
                done = True
                
        screen.blit(title_image, title_image_rect)
        
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

        mainmenu_knop = ui.Button((249, 44, 44), 50, 50, 100, 50, "Menu", 20)
        mainmenu_knop.draw(mouse_position, screen, font_button)

        if pygame.mouse.get_pressed()[0]:
            if mainmenu_knop.isOver(mouse_position):
                running = False
                main()

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Vraag 1.', (221, 211, 147), 600, 50)
        text.draw(screen)   

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 20), False, 'Geef aan welke van de volgende opties het beste bij he past', (221, 211, 147), 400, 200)
        text.draw(screen) 

        selectie_knop = ui.Button((0, 179, 60), 400, 250, 40, 50, 'A', 30)
        selectie_knop.draw(mouse_position, screen, font_button)

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 20), False, "Ik houd van puzzelen", (221, 211, 147), 450, 250)
        text.draw(screen)  

        pygame.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    main()

