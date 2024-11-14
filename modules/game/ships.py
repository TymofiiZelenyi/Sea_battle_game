import pygame
#image_ship: None | None

class Ships():
    def __init__ (self, x: int, y: int):
        # self.current_x, 
        # self.current_y, 
        self.x = x
        self.y = y
        #self.image_ship = image_ship
        self.width = 60, 
        self.height = 60,

        self.rect = pygame.Rect(self.x, self.y, 60, 60)

        # self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def ship_draw(self, screen):
        ship = pygame.surface.Surface((60, 60))
        ship.fill('#100000')
        screen.blit(ship, (self.x, self.y))

    def move(self, position, press):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and press == (True, False, False): 
            self.x = position[0] -30
            self.y = position[1] -30
        # else:
        #     self.x = self.x
        #     self.y = self.y
            
        
ship1 = Ships(x= 856, y= 162)