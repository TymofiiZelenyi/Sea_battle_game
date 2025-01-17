import pygame 

from .basement import *

data = read_json(fd="settings.json")

MAIN_WINDOW_COLOR = data["main"]["MAIN_WINDOW_COLOR"]
HEAD_COLOR = data["color"]["HEAD_COLOR"]
FPS = data["main"]["FPS"]

def settings_real():
    run_settings = True

    SOUND = data["main"]["MUSICK"]

    sound_list = []
    space_off = 55
    space_on = 55
    ON = SOUND

    shop_coursor_1 = False
    shop_coursor_2 = False
    shop_coursor_3 = False

    music1 = False
    music2  = False
    music3 = False
    music4  = False

    # def cursor(name, screen):
    #     path = os.path.abspath(__file__ + f"/../../../image/cursors/{name}.png")
    #     image = pygame.image.load(path)
    #     image = pygame.transform.scale(image, [32, 32])
    #     x, y = pygame.mouse.get_pos()
    #     x -= 16
    #     y -= 16
    #     screen.blit(image, (x, y))

    WIN_SOUND = True
    WIN_CURSOR = False
    WIN_MUSIC = False

    for item in range (10):
        sound_list.append(RectBetter(380 + space_off, 230, 50, 100, False))
        space_off += 55
    

##########################
    while run_settings:
        screen.fill(MAIN_WINDOW_COLOR)
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        #поле взаємодії з гучністю звука
        if WIN_SOUND:
            min_rect = pygame.Rect(320, 230, 100, 100)
            plus_rect = pygame.Rect(1000, 230, 100, 100)
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, min_rect)
            pygame.draw.rect(screen, MAIN_WINDOW_COLOR, plus_rect)

            #контроль налаштування гучності в рамках 10-ти кнопок 
            if ON < 0:
                ON = 0
            elif ON > 10:
                ON = 10

            #цикл відмальовування ДИЗактивованих ступней гучності
            for item in sound_list:
                pygame.draw.rect(screen, "black", item)

            #цикл відмальовування Активованих ступней гучності
            for item in range(ON):
                pygame.draw.rect(screen, "red", (380 + space_on, 230, 50, 100))
                space_on += 55

            space_on = 55

            
            pygame.draw.rect(screen, HEAD_COLOR, (320, 255, 100, 50))

            pygame.draw.rect(screen, HEAD_COLOR, (1000, 255, 100, 50))
            pygame.draw.rect(screen, HEAD_COLOR, (1025, 230, 50, 100))
        
 
        if WIN_CURSOR:
            shop_coursor1.button_draw(screen = screen)
            shop_coursor2.button_draw(screen = screen)
            shop_coursor3.button_draw(screen = screen)


        if WIN_MUSIC:
            c418.button_draw(screen = screen)
            new_year.button_draw(screen = screen)
            trolo.button_draw(screen = screen)
            rammstein.button_draw(screen = screen)
            
        
        #відмальовування статичних частин вікна SETTINGS
        pygame.draw.rect(screen, "#CCCCCC", (0, 200, 300, 600), 0)

        pygame.draw.rect(screen, HEAD_COLOR, (0, 50, 1400, 150), 0)

        settings_text.text_draw(screen = screen)
        button_back_menu.button_draw(screen = screen)

        sound_activated.button_draw(screen = screen)
        cursors_activated.button_draw(screen = screen)
        music_activated.button_draw(screen = screen)
        
        # print(clock.get_fps())
        
        pygame.display.flip()
        clock.tick(FPS)


        ##############################

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and press[0]:
                back_to_menu = button_back_menu.checkPress(position = position, press = press)
                win_sound = sound_activated.checkPress(position = position, press = press)
                win_cursor = cursors_activated.checkPress(position = position, press = press)
                win_music = music_activated.checkPress(position = position, press = press)

                if WIN_CURSOR:
                    shop_coursor_1 = shop_coursor1.checkPress(position = position, press = press)
                    shop_coursor_2 = shop_coursor2.checkPress(position = position, press = press)
                    shop_coursor_3 = shop_coursor3.checkPress(position = position, press = press)

                    
                if WIN_MUSIC:
                    music1 = c418.checkPress(position = position, press = press)
                    music2 = new_year.checkPress(position = position, press = press)
                    music3 = trolo.checkPress(position = position, press = press)
                    music4 = rammstein.checkPress(position = position, press = press)
                    
                if back_to_menu:
                    return "HOME"
                
                if music1:
                    print("c418")
                    play_music("c418", volume = ON)
                if music2:
                    print("new_year")
                    play_music("new_year", volume = ON)
                if music3:
                    print("trolo")
                    data["main"]["MUSICK_NAME"] = "trolo"
                    play_music("trolo", volume = ON)
                if music4:
                    print("rammstein")
                    data["main"]["MUSICK_NAME"] = "rammstein"
                    play_music("rammstein", volume = ON)
                
                
                if shop_coursor_1:
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.arrow)
                if shop_coursor_2:
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                if shop_coursor_3:
                    pygame.mouse.set_visible(True)
                    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                
                if not win_sound and not win_cursor and not win_music:
                    pass
                elif win_sound:
                    WIN_SOUND = True
                    WIN_CURSOR = False
                    WIN_MUSIC = False
                elif win_cursor:
                    WIN_SOUND = False
                    WIN_CURSOR = True
                    WIN_MUSIC = False
                elif win_music:
                    WIN_SOUND = False
                    WIN_CURSOR = False
                    WIN_MUSIC = True          
                
            if WIN_SOUND:
                if event.type == pygame.MOUSEBUTTONUP and plus_rect.collidepoint(position) and press[0]:
                    ON +=1
                    pygame.mixer.music.set_volume(ON / 10)
                    data["main"]["MUSICK"] = ON
                    SOUND = data["main"]["MUSICK"]
                elif event.type == pygame.MOUSEBUTTONUP and min_rect.collidepoint(position) and press[0]:
                    ON -= 1
                    pygame.mixer.music.set_volume(ON / 10)
                    data["main"]["MUSICK"] = ON
                    SOUND = data["main"]["MUSICK"]
                            
            if event.type == pygame.QUIT:
                run_settings = False
                pygame.quit()

                
