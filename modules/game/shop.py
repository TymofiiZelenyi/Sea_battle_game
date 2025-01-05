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

    anchor = False
    raft = False

    def cursor(name, screen):
        path = os.path.abspath(__file__ + f"/../../../image/cursors/{name}.png")
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, [32, 32])
        x, y = pygame.mouse.get_pos()
        x -= 16
        y -= 16
        screen.blit(image, (x, y))

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
        
        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:

                back_to_menu = button_back_menu.checkPress(position = position, press = press)
                shop_coursor_1 = shop_coursor1.checkPress(position = position, press = press)
                shop_coursor_2 = shop_coursor2.checkPress(position = position, press = press)
                shop_coursor_3 = shop_coursor3.checkPress(position = position, press = press)
                shop_coursor_4 = shop_coursor4.checkPress(position = position, press = press)
                shop_coursor_5 = shop_coursor5.checkPress(position = position, press = press)

                if shop_coursor_1:
                    anchor = False
                    raft = False
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                if shop_coursor_2:
                    anchor = False
                    raft = False
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                if shop_coursor_3:
                    anchor = False
                    raft = False
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                if shop_coursor_4:
                    anchor = True
                    raft = False
                if shop_coursor_5:
                    anchor = False
                    raft = True
                
                if anchor:
                    pygame.mouse.set_visible(False)
                    cursor(name ="cursor_anchor",screen=screen)
                
                if raft:
                    pygame.mouse.set_visible(False)
                    cursor(name ="cursor_raft",screen=screen)
                
                if back_to_menu:
                    return "HOME"
                
            if event.type == pygame.QUIT:
                run_shop = False
                pygame.quit()