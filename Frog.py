import pygame;
import sys;
class Frog:
    def __init__(self,image, x, y):
        self.grid_x = x;
        self.grid_y = y;
        self.initial_x = x;
        self.initial_y = y;
        self.original_image = image;
        self.image = image;
        self.rect = self.image.get_rect();
        self.pixel_x, self.pixel_y = self.get_pixel_position();
        self.rect.topleft = (self.pixel_x, self.pixel_y);
        self.life = 3;
        self.game_over = False;
        self.invulnerable_timer = 0;
        self.invulnerable = False;
        self.alpha = 255;
        self.alpha_change_direction = -5;

    def get_pixel_position(self):
        return self.grid_x * 50, self.grid_y *50 # ASSUME GRID_SIZE is 50 pixels

    def lose_hp(self):
        self.start_invulnerability(40);
        if self.life > 0:
            self.life -= 1;
    
    def start_invulnerability(self, duration):
        self.invulnerable = True;
        self.invulnerable_timer = duration;
    def move(self, direction):
        if not self.game_over:
            if direction == "up" and self.grid_y > 0:
                self.grid_y -= 1;
                self.rotate("up");
            elif direction == "down" and self.grid_y < 10:
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
    def check_collision_car(self, other_rect):
        # current_tile = game_grid[self.grid_y][self.grid_x];
        if self.rect.colliderect(other_rect) and not self.invulnerable:
            print("ouch!");
            self.lose_hp();
            self.grid_x = self.initial_x;
            self.grid_y = self.initial_y;
            self.pixel_x, self.pixel_y = self.get_pixel_position();
            self.rect.topleft = (self.pixel_x, self.pixel_y);
            return True;
        return False;

    def check_collision_log(self, other_rect, log):
        if self.rect.colliderect(other_rect):
            collision_x = self.rect.centerx;
            relative_x = collision_x - other_rect.left;

             # Optional: Normalize to a value between 0 and 1 (percentage of width)
            relative_position_percentage = relative_x / other_rect.width
            relative_position_percentage = relative_position_percentage * 100 ;
            if relative_position_percentage <=33:
                print("1/3");
                self.pixel_x = (other_rect.left+(other_rect.width/3));
            elif relative_position_percentage >33 and relative_position_percentage <= 66:
                print("2/3");
            elif relative_position_percentage >66:
                print("3/3");
            
            if log.direction == "right":
                self.grid_x += log.speed;
            elif log.direction == "left":
                self.grid_x -= log.speed;
            self.pixel_x = self.get_pixel_position()[0];
            self.rect.topleft = (self.pixel_x, self.pixel_y);


            # Print or use the relative position
            # print(f"{relative_position_percentage}");
            # print(f"Collision relative X: {relative_x} pixels from target's left edge")
            # print(f"Collision at {relative_position_percentage * 100:.2f}% of target_rect's width");