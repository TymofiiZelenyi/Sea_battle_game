import pygame
import socket

from .basement import *
from .map import *
from .battle import battle

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
FPS =  data["main"]["FPS"]

def wait_opponent():
    run_wait_opponent = True
    bg = pygame.image.load(os.path.abspath(__file__ + "/../../../image/bg/wait_for_opponent_bg.png"))
    bg = pygame.transform.scale(bg, [1400, 800])

    while run_wait_opponent:
        screen.fill(MAIN_WINDOW_COLOR)
        screen.blit(bg, (0, 0))
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        wait_opponent_text.button_draw(screen = screen)
            
        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:
                placement_window = wait_opponent_text.checkPress(position = position, press = press)

                if placement_window:
                    res = battle()
                    if res == "BACK":
                        return res
            
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()