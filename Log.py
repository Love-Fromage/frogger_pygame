import pygame

class Log:
    def __init__(self,width:int, height:int, x, y, direction:str, speed:float):
        self.grid_x = x;
        self.grid_y = y;
        self.direction = direction;
        self.width = width;
        self.height = height;
        self.game_over = False;
        self.speed = speed;
        self.rect = pygame.Rect(x, y, self.width, self.height);
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def get_pixel_position(self):
        return self.grid_x * 50, (self.grid_y*50)-50/2;

    def move(self):
        if not self.game_over:
            if self.direction == "left":
                if self.pixel_x + self.rect.width > 0:
                    self.grid_x -= self.speed;
                else:
                    self.grid_x = 16;
            elif self.direction == "right":
                # print(f"self.pixel_x - self.width = {self.pixel_x - self.width}")
                if self.pixel_x - self.width <= (14*50):
                    self.grid_x += self.speed;
                else:
                    self.grid_x = -4;

            self.pixel_x, self.pixel_y = self.get_pixel_position();
            self.rect.topleft = (self.pixel_x, self.pixel_y+25);

    def draw(self, screen):
       pygame.draw.rect(screen,(128, 104, 58), self.rect) 