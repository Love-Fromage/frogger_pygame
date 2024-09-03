import pygame;
import sys;
class Frog:
    def __init__(self,image, x, y):
        self.grid_x = x;
        self.grid_y = y;
        self.original_image = image;
        self.image = image;
        self.rect = self.image.get_rect();
        self.pixel_x, self.pixel_y = self.get_pixel_position();
        self.rect.topleft = (self.pixel_x, self.pixel_y);
        self.life = 3;
        self.invulnerable_timer = 0;
        self.invulnerable = False;
        self.alpha = 255;
        self.alpha_change_direction = -5;

    def get_pixel_position(self):
        return self.grid_x * 50, self.grid_y *50 # ASSUME GRID_SIZE is 50 pixels

    def lose_hp(self):
        self.start_invulnerability(40);
        if self.life >= 0:
            self.life -= 1;
    
    def start_invulnerability(self, duration):
        self.invulnerable = True;
        self.invulnerable_timer = duration;
    def move(self, direction):
        if direction == "up" and self.grid_y > 0:
            self.grid_y -= 1;
            self.rotate("up");
        elif direction == "down" and self.grid_y < 11:
            self.grid_y +=1;
            self.rotate("down");
        elif direction == "left" and self.grid_x > 0:
            self.grid_x -=1;
            self.rotate("left");
        elif direction == "right" and self.grid_x < 15:
            self.grid_x +=1;
            self.rotate("right");
        
        # Update pixel position after moving
        self.pixel_x, self.pixel_y = self.get_pixel_position();
        self.rect.topleft = (self.pixel_x, self.pixel_y);
    
    def rotate(self, direction):
        if(direction == "left"):
            self.image = pygame.transform.rotate(self.original_image, 90);
            self.rect = self.image.get_rect(center=self.rect.center);
        elif(direction == "right"):
            self.image = pygame.transform.rotate(self.original_image, -90);
            self.rect = self.image.get_rect(center=self.rect.center);
        elif(direction == "up"):
            self.image = pygame.transform.rotate(self.original_image, 0);
            self.rect = self.image.get_rect(center=self.rect.center);
        elif(direction == "down"):
            self.image = pygame.transform.rotate(self.original_image, 180);
            self.rect = self.image.get_rect(center=self.rect.center);
            

    def draw(self, screen):
        temp_image = self.image.copy();
        temp_image.set_alpha(self.alpha);
        screen.blit(temp_image, (self.pixel_x, self.pixel_y));
    def check_collision(self, other_rect):
        # current_tile = game_grid[self.grid_y][self.grid_x];
        if self.rect.colliderect(other_rect) and not self.invulnerable:
            print("ouch!");
            self.lose_hp();
            return True;
        return False;