import pygame 

from .basement import *

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
FPS = data["main"]["FPS"]

def settings_real():
    run_settings = True

    sound_list = []
    space_off = 55
    space_on = 55
    ON = 5

    for item in range (10):
        sound_list.append(RectBetter(380 + space_off, 230, 50, 100, False))
        space_off += 55
    
    while run_settings:
        screen.fill(MAIN_WINDOW_COLOR)
        position =pygame.mouse.get_pos()
        press =pygame.mouse.get_pressed()

        min_rect = pygame.Rect(320, 230, 100, 100)
        plus_rect = pygame.Rect(1000, 230, 100, 100)
        pygame.draw.rect(screen,MAIN_WINDOW_COLOR , min_rect)
        pygame.draw.rect(screen,MAIN_WINDOW_COLOR ,  plus_rect)

        if ON < 0:
            ON = 0
        elif ON > 10:
            ON = 10

        for item in sound_list:
            pygame.draw.rect(screen, "black", item)

        for item in range(ON):
            pygame.draw.rect(screen, "red", (380 + space_on, 230, 50, 100))
            space_on += 55

        space_on = 55

        pygame.draw.rect(screen, "#CCCCCC", (0, 200, 300, 600), 0)

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)
        
        pygame.draw.rect(screen, HEAD_COLOR, (320, 255, 100, 50))

        pygame.draw.rect(screen, HEAD_COLOR, (1000, 255, 100, 50))
        pygame.draw.rect(screen, HEAD_COLOR, (1025, 230, 50, 100))
    
        settings_text.text_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)
        sound1.button_draw(screen = screen)

        back_to_menu = button_back_menu.checkPress(position = position, press = press)
        
        if back_to_menu:
            return "HOME"
        
        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and plus_rect.collidepoint(position) and press[0]:
                ON +=1
                pygame.mixer.music.set_volume(ON / 10)
            elif event.type == pygame.MOUSEBUTTONUP and min_rect.collidepoint(position) and press[0]:
                ON -= 1
                pygame.mixer.music.set_volume(ON / 10)
                    
            if event.type == pygame.QUIT:
                run_settings = False
                pygame.quit()