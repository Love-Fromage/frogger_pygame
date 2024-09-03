import pygame;
import sys;

class Car:
    def __init__(self, image, x,y, direction):
        self.grid_x = x;
        self.grid_y = y;
        self.direction = direction;
        self.original_image = image;
        self.image = image;
        self.rect = self.image.get_rect();
        self.image = pygame.transform.rotate(self.original_image, 90);
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def get_pixel_position(self):
        return self.grid_x * 50, (self.grid_y *50)-50/2 # ASSUME GRID_SIZE is 50 pixels

    def move(self):
        if self.pixel_x+ self.rect.width >0 :
            if self.direction == "left":
                self.grid_x -= 0.15;
        else:
            self.grid_x = 16;
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def draw(self, screen):
        screen.blit(self.image, (self.pixel_x, self.pixel_y));
