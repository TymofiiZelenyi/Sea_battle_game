import pygame 
import time
import socket
import os

from .basement import *
from .map import *

def shop():
    run_shop = True

    while run_shop:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        pygame.draw.rect(screen, HEAD_COLOR, (0, 0, 1400, 150), 0)
        shop_text.text_draw(screen = screen)
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()