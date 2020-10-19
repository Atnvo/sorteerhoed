import pygame

class Text:
    def __init__(self, font, antialias, text, color, x, y):
        self.font = font
        self.antialias = antialias
        self.text = text
        self.color = color
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.font.render(self.text, self.antialias, (self.color)), (self.x, self.y))

class Button:
    def __init__(self, color, x, y, width, height, text, fontsize):
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.fontsize = fontsize
        self.courier_button_font = pygame.font.SysFont("Courier", self.fontsize)

    def draw(self, pos, screen, font):

        button_color = 	(169,169,169) if self.rect.collidepoint(pos) else self.color
        self.rect.inflate_ip(-8,-9) if self.rect.collidepoint(pos) else self.rect
        pygame.draw.rect(screen, button_color, self.rect)

        text_width, text_height = self.courier_button_font.size(self.text)
        textpos = (self.rect.centerx - text_width // 2, self.rect.centery - text_height // 2)
        buttontext = Text(font, True, self.text, (255, 255, 255), textpos[0], textpos[1])
        buttontext.draw(screen)

    def isOver(self, pos):
        return self.rect.collidepoint(pos)
         