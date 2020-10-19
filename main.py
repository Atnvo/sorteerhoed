import pygame
import handlers.ui as ui    #Importeer functies van andere file

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
        screen = pygame.display.set_mode((1490, 800))
        screen.fill((0, 0, 0))
        clock = pygame.time.Clock()
        mouse_position = pygame.mouse.get_pos()
        
        speel_knop = ui.Button((155, 155, 155), 400, 400, 80, 30, "Speel", 20)
        speel_knop.draw(mouse_position, screen, font_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        
        screen.blit(title_image, title_image_rect)

        if speel_knop.isOver(mouse_position):
            # menu_vraag(screen)
            print('Hover', mouse_position)
        
        pygame.display.update()
        clock.tick(60)

def menu_vraag(screen):
    # screen.fill((0, 0, 0))

    text = ui.Text(pygame.font.Font("assets/fonts/lunchds.ttf", 80), False, 'Vraag 1', (221, 211, 147), 600, 400)
    text.draw(screen)    

if __name__ == '__main__':
    main()

