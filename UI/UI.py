import pygame 
import sys

#Initialisation de pygame
pygame.init()

#Création de UI
width = 1350
height = 800
font_size = 11
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Like-Rogue")

# Template de font pour les boutons
font = pygame.font.SysFont('Consolas', font_size)

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Attributs de base
        self.press = False
        self.elevation = elevation
        self.dynamic_elev = elevation
        self.original_y_pos = pos[1]

        # Rectangle du bouton
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = '#475F77'

        # Texte du bouton
        self.text_surf = my_font.render(text, True, "#000202FF")
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self):
        # logique de l'élévation
        self.top_rect.y = self.original_y_pos - self.dynamic_elev
        self.text_rect.center = self.top_rect.center

        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)

        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = '#D74B4B'
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elev = 0
                self.press = True
            else:
                self.dynamic_elev = self.elevation
                if self.press == True:
                    self.press = False
                    # Indication du bouton, lorsqu'il est pressé
                    print('Play Pressed!')
        else:
            self.dynamic_elev = self.elevation
            self.top_color = "#038D05"

# Création du bouton + loop d'affichage
my_font = pygame.font.Font(None, 35)
button = Button('Play!', 200, 40, (600, 300), 5)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#00C3FE")
    button.draw()

    pygame.display.update()



