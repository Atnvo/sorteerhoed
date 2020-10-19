import pygame
import handlers.ui as ui    #Importeer user interacties functies van een andere file
# import handlers.sqllite_db as db

screen = pygame.display.set_mode((1490, 800))
mainClock = pygame.time.Clock()

lichtgeel = (246,185,20)

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
    title_image_rect.x, title_image_rect.y = 300, 20

    # Fonts / text
    font_title = pygame.font.Font("assets/fonts/harry.ttf", 140)
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)

    # title = font_title.render("Harrypotter", True, (221, 211, 147))

    while not done:
        pygame.event.wait()
        
        screen.fill((255, 255, 255))
        mouse_position = pygame.mouse.get_pos()
        
        speel_knop = ui.Button((0, 179, 60), 550, 400, 320, 70, "Speel", 20)
        speel_knop.draw(mouse_position, screen, font_button)

        resultaten_knop = ui.Button((155, 155, 155), 550, 500, 320, 70, "mijn vorige resultaten", 20)
        resultaten_knop.draw(mouse_position, screen, font_button)

        quit_knop = ui.Button((249, 44, 44), 550, 600, 320, 70, "Quit", 20)
        quit_knop.draw(mouse_position, screen, font_button)

        click = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(event.button)
                print('ttttt')
                if speel_knop.isOver(mouse_position):
                    done = True
                    menu_vraag()
                if quit_knop.isOver(mouse_position):
                    print('test')
                    done = True

        screen.blit(title_image, title_image_rect)
        
        pygame.display.update()
        mainClock.tick(60)

def menu_vraag():
    running = True
    while running:
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Vraag 1.', (221, 211, 147), 600, 50)
        text.draw(screen)    

        pygame.display.update()
        mainClock.tick(60)

if __name__ == '__main__':
    main()

