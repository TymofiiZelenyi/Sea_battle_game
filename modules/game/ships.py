import pygame

class Ships():
    def __init__ (self, x: int, y: int, count_length: int):
        self.x = x
        self.y = y
        self.count_length = count_length
        
        # self.lenth = 60

        self.dir = "hor"

        self.rect = pygame.Rect(self.x, self.y, 60 * self.count_length, 60)

    # def rotate(self, position, press):
    #     if self.rect.collidepoint(position) and press[0] and press[2] and self.dir == "hor":
    #         self.dir = "ver"
    #         print("nnnan")
    #     if self.rect.collidepoint(position) and press[0] and press[2] and self.dir == "ver":
    #         self.dir = "hor"

    def ship_draw(self, screen):
        if self.dir == "hor":
            pygame.draw.rect(screen, '#E7C500', (self.x, self.y, 60 * self.count_length, 60))
        if self.dir == "ver":
            self.rect = pygame.Rect(self.x, self.y, 60, 60 * self.count_length)
            pygame.draw.rect(screen, '#E7C500', (self.x, self.y, 60, 60 * self.count_length))

    def move(self, position, press):
        if self.rect.collidepoint(position) and press[0] and self.dir == "hor":
            self.x = position[0] - 30
            self.y = position[1] - 30
            self.rect = pygame.Rect(self.x, self.y, 60 * self.count_length, 60)
            return True
        if self.rect.collidepoint(position) and press[0] and self.dir == "ver":
            self.x = position[0] - 30
            self.y = position[1] - 30
            self.rect = pygame.Rect(self.x, self.y, 60 * self.count_length, 60)
            return True
            
        
ship1 = Ships(x = 856, y = 162, count_length = 2)
ship2 = Ships(x = 926, y = 162, count_length = 2)

ship3 = Ships(x = 996, y = 162, count_length = 2)
ship4 = Ships(x = 1066, y = 162, count_length = 2)
ship5 = Ships(x = 1136, y = 162, count_length = 2)