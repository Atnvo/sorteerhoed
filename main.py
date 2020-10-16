import pygame
import os

def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init()          
    done = False

    pygame.mixer.init()
    pygame.mixer.music.load('assets\sounds\8bit_harrypotter_theme.mp3')
    pygame.mixer.music.play(-1)

    font_title = pygame.font.Font("assets/fonts/harry.ttf", 124)
    font_subtitle = pygame.font.Font("assets/fonts/lunchds.ttf", 114)
    bit_harry = pygame.image.load("assets/images/harry_bit.png")
    bit_harry = bit_harry.get_rect()

    title = font_title.render("Harrypotter", True, (255, 255, 255))
    sub_title = font_subtitle.render("Sorteerhoed", True, (255, 255, 255))

    while not done:

        pygame.event.wait()
        screen = pygame.display.set_mode((880, 640))
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        
        screen.fill((0, 0, 0))
        screen.blit(
            title, (440 - title.get_width() // 2, 240 - title.get_height() // 2)
            # sub_title, (640 - sub_title.get_width() // 2, 440 - sub_title.get_height() // 2)
        )
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()