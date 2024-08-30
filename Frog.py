import pygame;
import sys;
class Frog:
    def __init__(self,image, x, y):
        self.grid_x = x;
        self.grid_y = y;
        self.image = image;
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def get_pixel_position(self):
        return self.grid_x * 50, self.grid_y *50 # ASSUME GRID_SIZE is 50 pixels
    
    def move(self, direction):
        if direction == "up" and self.grid_y > 0:
            self.grid_y -= 1;
        elif direction == "down" and self.grid_y < 11:
            self.grid_y +=1;
        elif direction == "left" and self.grid_x > 0:
            self.grid_x -=1;
        elif direction == "right" and self.grid_x < 15:
            self.grid_x +=1;
        
        # Update pixel position after moving
        self.pixel_x, self.pixel_y = self.get_pixel_position();

    def draw(self, screen):
       screen.blit(self.image, (self.pixel_x, self.pixel_y));

    def check_collision(self, game_grid):
        current_tile = game_grid[self.grid_y][self.grid_x];
        # if current_tile == 0:
        #     # print("water");