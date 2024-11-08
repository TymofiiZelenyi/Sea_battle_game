import pygame
from .button import button_play, button_quit, button_settings
from .__settings__ import BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, FPS, WINDOW_HEIGHT, WINDOW_WIDTH, MAIN_WINDOW_COLOR

pygame.init()
pygame.display.set_caption("Sea_battle_game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))



def menu():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)

        button_play.button_draw(screen = screen)
        button_settings.button_draw(screen = screen)
        button_quit.button_draw(screen = screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()


        #press= press
        button_play.checkPress(position = position, press = press)
        button_settings.checkPress(position = position, press = press)
        button_quit.checkPress(position = position, press = press)
        
        
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    
    pygame.quit()

def settings():
    pass