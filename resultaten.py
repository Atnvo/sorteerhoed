import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
import handlers.sorteerhoed as sorteerhoed

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_w, screen_h = pygame.display.get_surface().get_size()

def main(username):
    resultaten = sorteerhoed.resultaten_ophalen(username)
    mainClock = pygame.time.Clock()
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
                
        screen.blit(spec_image, spec_image_rect)

        pygame.display.update()
        mainClock.tick(60)

def vraag_component(vraag, mogelijk_antwoord):
    text = text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, vraag, (221, 211, 147), screen_w // 3.5, 50)
    button1 = ui.Button((0, 179, 60), 400, 250, 50, 50, mogelijk_antwoord[0], screen_w // 2 -200, 0)
    
    return [text, button1, button2, button3, button4]


if __name__ == '__main__':
    main()

