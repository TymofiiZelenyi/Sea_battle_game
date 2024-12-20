import pygame 
import os

from .basement import *
from .map import *

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
FPS = data["main"]["FPS"]

def shop():
    run_shop = True

    # def coursor(name):
    #     x, y = pygame.mouse.get_pos()
    #     x -= 16
    #     y -= 16
    #     screen.blit(cursor, (x, y))

    while run_shop:
        screen.fill(MAIN_WINDOW_COLOR)
        
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        
        pygame.draw.rect(screen, HEAD_COLOR, (0, 0, 1400, 150), 0)
        shop_text.text_draw(screen = screen)

        button_back_menu.button_draw(screen = screen)
        
        shop_coursor1.button_draw(screen = screen)
        shop_coursor2.button_draw(screen = screen)
        shop_coursor3.button_draw(screen = screen)
        shop_coursor4.button_draw(screen = screen)
        shop_coursor5.button_draw(screen = screen)

        back_to_menu = button_back_menu.checkPress(position = position, press = press)
        
        shop_coursor_1 = shop_coursor1.checkPress(position = position, press = press)
        shop_coursor_2 = shop_coursor2.checkPress(position = position, press = press)
        shop_coursor_3 = shop_coursor3.checkPress(position = position, press = press)
        shop_coursor_4 = shop_coursor4.checkPress(position = position, press = press)
        shop_coursor_5 = shop_coursor5.checkPress(position = position, press = press)

        if shop_coursor_1:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
        if shop_coursor_2:
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        if shop_coursor_3:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
        if shop_coursor_4:
            anchor = os.path.abspath(__file__ + f"/../../../../image/cursonr/cursonr_anchor.png")
            pygame.mouse.set_cursor(*pygame.cursors.anchor) 
        if shop_coursor_5:
            raft = os.path.abspath(__file__ + f"/../../../../image/cursonr/cursonr_raft.png")
            pygame.mouse.set_cursor(*pygame.cursors.raft)   
        
        if back_to_menu:
            return "HOME"
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_wait_opponent = False
                pygame.quit()