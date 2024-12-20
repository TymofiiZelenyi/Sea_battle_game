import pygame 

from .basement import *
from .map import *
from .battle import battle

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
FPS =  data["main"]["FPS"]

def wait_opponent():
    run_wait_opponent = True

    while run_wait_opponent:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        wait_opponent_text.button_draw(screen = screen)
        # button_back_menu.button_draw(screen = screen)
        
        placement_window = wait_opponent_text.checkPress(position = position, press = press)

        if placement_window:
            res = battle()
            if res == "BACK":
                return res
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()