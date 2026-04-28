from asyncio import events
from turtle import pos
from typing import Self

import pygame
import pygame_menu
import sys

#Initialisation de pygame
pygame.init()

#Création de UI
width = 1300
height = 750
font_size = 11
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Like-Rogue")

# Template de font pour les boutons
font = pygame.font.SysFont('Consolas', font_size)
my_font = pygame.font.Font(None, 35)


# Création du titre
font = pygame.font.SysFont('comicsansms', 75)
text = font.render('Like-Rogue', True, ("#FFFFFFFF"))

# Création de variables de settings
settings = {
    "difficulty": "Normal"
}

# Retour de fonction de settings
def set_difficulty(value, difficulty):
    settings["difficulty"] = difficulty
    print(f"Difficulty set to: {settings['difficulty']}")

class Button:
    def __init__(self, text, width, height, pos, elevation):
        # Attributs de base
        self.press = False
        self.elevation = elevation
        self.dynamic_elev = elevation
        self.original_y_pos = pos[1]

        # Rectangle du bouton
        self.top_rect = pygame.Rect(pos, (width, height))
        self.top_color = "#000000"

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
            self.top_color = "#005501"
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elev = 0
                self.press = True
            else:
                self.dynamic_elev = self.elevation
                if self.press == True:
                    self.press = False
                    # Indication du bouton, lorsqu'il est pressé
                    print('Play Pressed!')
                    print('Settings Pressed!')
                    print('Stats Pressed!')
        else:
            self.dynamic_elev = self.elevation
            self.top_color = "#038D05"

           
#Création du bouton + loop d'affichage
buttons = [
    Button('Play!', 200, 40, (545, 400), 5),
    Button('Settings!', 300, 40, (495, 450), 5),
    Button('Stats!', 150, 40, (570, 500), 5)
]

#Création du menu de settings
settings_menu = pygame_menu.Menu('Settings!', 600, 400, theme=pygame_menu.themes.THEME_DARK)
settings_menu.add.selector("Difficulty", [("Easy", "Easy"), ("Normal", "Normal"), ("Hard", "Hard")], onchange=set_difficulty)
settings_menu.add.button("Back", pygame_menu.events.BACK)

#Création du menu de stats
stats_menu = pygame_menu.Menu('Stats!', 600, 400, theme=pygame_menu.themes.THEME_DARK)

running = True
while running:
        if settings_menu.is_enabled():
            settings_menu.update(pygame.event.get())
            settings_menu.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill("#000000")
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 4 - text.get_height() // 2))
        for btn in buttons:
            btn.draw()

        pygame.display.update()



