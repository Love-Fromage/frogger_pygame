import pygame;
import sys;

class Car:
    def __init__(self, image, x,y, direction):
        self.grid_x = x;
        self.grid_y = y;
        self.direction = direction;
        self.original_image = image;
        self.image = image;
        self.game_over = False;
        # self.rect = self.image.get_rect();
        self.rect = pygame.Rect(x,y, self.image.get_rect().width, 50);
        self.image = pygame.transform.rotate(self.original_image, 90);
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def get_pixel_position(self):
        return self.grid_x * 50, (self.grid_y *50)-50/2 # ASSUME GRID_SIZE is 50 pixels

    def move(self):
        if not self.game_over:
            if self.direction == "left":
                if self.pixel_x+ self.rect.width >0 :
                     self.grid_x -= 0.15;
                else:
                    self.grid_x = 16;
            elif self.direction == "right":
                if self.pixel_x <= 16*50:
                    self.grid_x += 0.15;
                else:
                    self.grid_x = -1;

            self.pixel_x, self.pixel_y = self.get_pixel_position();
            self.rect.topleft = (self.pixel_x, self.pixel_y+25);
    def draw(self, screen):
        screen.blit(self.image, (self.pixel_x, self.pixel_y));
