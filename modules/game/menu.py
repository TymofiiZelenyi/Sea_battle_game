import pygame 

from .basement import *
from .placement import placement
from .settings_real import settings_real
from .shop import shop

play_music("All I Want for Christmas Is You", volume = 0)

# pygame.mouse.set_cursor(*pygame.cursors.tri_left)
# pygame.mouse.set_cursor()

data = read_json(fd="settings.json")

GOLD = data["main"]["GOLD"]
FPS = data["main"]["FPS"]
def menu():

    run_menu = True

    count_gold = Text(x = 1100, y = 20, text = f"{GOLD} GOLD", text_size=50, color="Red")
    
    while run_menu:
        
        screen.fill(MAIN_WINDOW_COLOR)

        #Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
        
        button_play.button_draw(screen = screen)
        button_settings.button_draw(screen = screen)
        button_shop.button_draw(screen = screen)
        button_quit.button_draw(screen = screen)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        count_gold.text_draw(screen = screen)

        wait_opponent_window = button_play.checkPress(position = position, press = press)
        settigs_window = button_settings.checkPress(position = position, press = press)
        shop_win = button_shop.checkPress(position = position, press = press)
        quit = button_quit.checkPress(position = position, press = press)

        if wait_opponent_window:
            placement()
        if settigs_window:
            settings_real()
        if shop_win:
            shop()
        if quit:
            run_menu = False

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_menu = False
                pygame.quit()
