import pygame

def main():
    pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
    pygame.init() 

    done = False

    # Music
    pygame.mixer.init()
    pygame.mixer.music.load('assets\sounds\8bit_harrypotter_theme.mp3')
    pygame.mixer.music.play(-1)

    # Fonts / text
    font_title = pygame.font.Font("assets/fonts/harry.ttf", 80)
    font_button = pygame.font.Font("assets/fonts/pixel2.ttf", 20)

    
    # font_subtitle = pygame.font.Font("assets/fonts/lunchds.ttf", 114)
    bit_harry = pygame.image.load("assets/images/harry_bit.png")
    bit_harry = bit_harry.get_rect()

    title = font_title.render("Harrypotter", True, (255, 255, 255))

    while not done:

        mouse = pygame.mouse.get_pos()

        pygame.event.wait()
        screen = pygame.display.set_mode((980, 640))
        clock = pygame.time.Clock()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                done = True
        
        screen.fill((0, 0, 0))
        
        screen.blit(
            title, (440 - title.get_width() // 2, 140 - title.get_height() // 2)
        )

        speel = Button((255, 255, 255), 210, 400, 80, 30, "Speel", 20)
        speel.draw(mouse, screen, font_button)

        if speel.isOver:
            menu_vraag()
        
        pygame.display.update()
        clock.tick(60)

def menu_vraag():
    print('tesstt')

class Fonts:
    def __init__(self, font, antialias, text, color, x, y):
        self.font = font
        self.antialias = antialias
        self.text = text
        self.color = color
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.font.render(self.text, self.antialias, (self.color)), (self.x, self.y))

class image:
    def __init__(self, bestand, x, y):
        self.bestand = pygame.image.load(bestand)
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.bestand, (self.x, self.y))

class Button:
    def __init__(self, color, x, y, width, height, text, fontsize):
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.fontsize = fontsize
        self.courier_button_font = pygame.font.SysFont("Courier", self.fontsize)

    def draw(self, pos, screen, font):

        button_color = (211, 211, 211) if self.rect.collidepoint(pos) else self.color
        pygame.draw.rect(screen, button_color, self.rect)

        text_width, text_height = self.courier_button_font.size(self.text)
        textpos = (self.rect.centerx - text_width // 2, self.rect.centery - text_height // 2)
        buttontext = Fonts(font, True, self.text, (255, 255, 255), textpos[0], textpos[1])
        buttontext.draw(screen)

    def isOver(self, pos):
        return self.rect.collidepoint(pos) 

if __name__ == '__main__':
    main()