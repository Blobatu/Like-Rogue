

import pygame
import pygame_menu
import sys

#Initialisation de pygame
pygame.init()

#Création de UI
font_size = 11
screen = pygame.display.set_mode((1300, 750))
pygame.display.set_caption("Like-Rogue")


# Template de font pour les boutons
font = pygame.font.SysFont('Consolas', font_size)
my_font = pygame.font.Font(None, 35)


# Création du titre
font = pygame.font.SysFont('comicsansms', 75)
text = font.render('Like-Rogue', True, ("#FFFFFFFF"))

# Création de variables de settings
settings = {
    "Difficulty": "Normal"
}

# Retour de fonction de settings
def set_difficulty( value, difficulty):
    settings["Difficulty"] = difficulty
    print(f"Difficulty set to: {settings['Difficulty']})")

# Création de variables de stats
stats = {
    "character_name": "Nard",
    "level_progression": 0,
    "Xp level progression": 0
}

# Retour de fonctions de stats
def get_character_name():
        return stats["character_name"]

def get_level_progression():
    return stats["level_progression"]

def get_xp_level_progression():
    return stats["Xp level progression"]


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
                    print('Quit Pressed!')
        else:
            self.dynamic_elev = self.elevation
            self.top_color = "#038D05"



# Loop d'affichage
def start_game():
    running = True
    clock = pygame.time.Clock()
    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(60)

#Création du menu de settings
settings_menu = pygame_menu.Menu('Settings!', 600, 400, theme=pygame_menu.themes.THEME_DARK)
settings_menu.add.selector("Difficulty", [("Easy", "Easy"), ("Normal", "Normal"), ("Hard", "Hard")], onchange=set_difficulty)
settings_menu.add.button("Back", pygame_menu.events.BACK)

#Création du menu de stats
stats_menu = pygame_menu.Menu('Stats!', 600, 400, theme=pygame_menu.themes.THEME_DARK)
stats_menu.add.label(f"Character name: {get_character_name()}")
stats_menu.add.progress_bar("Level progression:", default=get_level_progression())
stats_menu.add.progress_bar("XP progression:", default=get_xp_level_progression())
stats_menu.add.button("Back", pygame_menu.events.BACK)

#Création du menu de principal
main_menu = pygame_menu.Menu('Rogue-Like', 1300, 750, theme=pygame_menu.themes.THEME_DARK)
buttons = [
main_menu.add.button("Play!", start_game, 200, 40, (545, 400), 5,),
main_menu.add.button("Settings!", settings_menu, 300, 40, (495, 450), 5,),
main_menu.add.button("Stats!", stats_menu, 150, 40, (570, 500), 5),
main_menu.add.button("Quit!", pygame_menu.events.EXIT, 150, 40, (570, 550), 5)
]

running = True
while running:
                  
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                
            screen.fill("#000000")

            if main_menu.is_enabled():
                main_menu.update(events)
                main_menu.draw(screen)


            screen.blit(text, (1300 // 2 - text.get_width() // 2, 750 // 4 - text.get_height() // 2))
        
            pygame.display.update()
            pygame.display.flip()
            
 



