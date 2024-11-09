import pygame 
from .button import button_back_menu, button_play, button_quit, button_ready, button_settings
from .__settings__ import FPS, WINDOW_HEIGHT, WINDOW_WIDTH, MAIN_WINDOW_COLOR, PLACE_LENGTH, BUTTON_COLOR

pygame.init()
pygame.display.set_caption("Sea_battle_game")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
ACTIVE_SCREEN = "menu"
#menu_active = True

def menu():
    while True:
    #while menu_active == True:
    
        screen.fill(MAIN_WINDOW_COLOR)

        #Створення кнопок "play" "settings" "quit", задавання їх величини та кординат на головному екрані. Містять у собі рядковий контент.
        
        

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
    #pygame.quit()




def wait_opponent():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)

        button_back_menu.button_draw(screen = screen)
        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        button_back_menu.checkPress(position = position, press = press)




        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        



def placement():
    while True:
        screen.fill(MAIN_WINDOW_COLOR)

        position = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        button_ready.button_draw(screen = screen)
    
        button_ready.checkPress(position = position, press = press)
    
    
    
        pygame.display.flip()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

def battle():
    
    screen.fill((MAIN_WINDOW_COLOR))
    
   

#Помилка із класом RECT
    your_screen = pygame.Rect(x = 75, y = 60, width = PLACE_LENGTH, height = PLACE_LENGTH)
    your_screen.fill(BUTTON_COLOR)
    screen.blit(your_screen)

#Помилка із класом RECT
    enemy_screen = pygame.Rect(x = 635, y = 60, width = PLACE_LENGTH, height = PLACE_LENGTH)
    enemy_screen.fill(BUTTON_COLOR)
    screen.blit(enemy_screen)

    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



    

    
    




