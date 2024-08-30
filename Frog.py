import pygame;
import sys;
frog_speed = 5;
leap_speed = 10;
class Frog:
    def __init__(self, image_path, x, y):
        # Load the frog image
        try:
            self.image = pygame.image.load(image_path);
            print(f"Loaded the image from {image_path}");
        except pygame.error as e:
            print(f"Failed to load the image from {image_path}");
            sys.exit();
        # Scale the image down
        self.original_image = pygame.transform.scale(self.image, (50, 50));
        self.image = self.original_image.copy(); # Make a copy to rotate later

        # Set the initial position of the frog
        self.x = x - self.image.get_width()/2;
        self.y = y;
        self.leap_distance = 50; # Distance of the frog leap
        self.is_leaping = False;
        self.leap_target_y = y;
        self.leap_direction = 0;
        self.move_on_log = False;

        #store landing position
        self.landing_x = x;
        self.landing_y = y;

        # Set the initial velocity of the frog
        self.speed = frog_speed;
        self.leap_speed = leap_speed;
    
        # Create a rect for the frog for collision detection
        self.rect = self.image.get_rect();
        self.rect.topleft = (self.x, self.y);

        # Log folloeing attributes
        self.is_on_log = False;
        self.log_offset = 0; # Offset of Frogger's x position relative to the log's x position

    def draw(self, screen):
        # Draw the frog
        self.rect.topleft = (self.x, self.y);
        self.draw_hitbox(screen);
        screen.blit(self.image, self.rect.topleft);
    
    def draw_hitbox(self, screen):
        # Draw a rectangle around the frog's rect (hitbox) for debugging
        pygame.draw.rect(screen, (0,0,255), self.rect, self.rect.width);

    def move_horizontal(self, dx):
        # Update the frog's position
        if(self.is_on_log):
            self.move_on_log = True;
        self.x += dx;
        if(dx > 0):
            # If going right
            self.rotation_angle = -90;
            self.rotation_angle %= 360; # Keep angle within 0-359 degress

            # Rotate the image
            self.image = pygame.transform.rotate(self.original_image, self.rotation_angle);
    
            # Update the rect to the new image size and position
            self.rect = self.image.get_rect(center=self.rect.center);
        if(dx < 0):
            # If going left
            self.rotation_angle = 90;
            self.rotation_angle %= 360;
    
            # Rotate the image
            self.image = pygame.transform.rotate(self.original_image, self.rotation_angle);
    
            # Update the rect to the new image size and position
            self.rect = self.image.get_rect(center=self.rect.center);

    def rotate_back(self):
        self.image = pygame.transform.rotate(self.original_image, 0);
        self.rect = self.image.get_rect(center=self.rect.center);

    def start_leap(self, direction):
        # if not self.is_leaping:
            self.is_leaping = True;
            self.leap_direction = direction;
            self.leap_target_y = self.y - (self.leap_distance * direction);
            # self.is_on_log = False;

    def update(self):
        if self.is_leaping:
            # Move towards the leap target
            if self.leap_direction == 1: # leaping up
                if self.y > self.leap_target_y:
                    self.y -= self.leap_speed;
                else:
                    self.y = self.leap_target_y;
                    self.is_leaping = False;
                    self.landing_x = self.rect.centerx;
                    self.landing_y = self.rect.centery;
            elif self.leap_direction == -1: # Leaping down
                if self.y < self.leap_target_y:
                    self.y += self.leap_speed;
                else:
                    self.y = self.leap_target_y;
                    self.is_leaping = False;
                    self.landing_x = self.rect.centerx;
                    self.landing_y = self.rect.centery;
        # Update rect position after every movement
        # self.rect.topleft = (self.x, self.y);
    
    
    def check_collision(self, other_rect):
        # Check if Frogger is landing on a log after a leap
        if(self.rect.colliderect(other_rect)):
            if not self.is_leaping: # only check landing when not leaping
                # Calculate the offset
                self.landing_x = self.rect.centerx;
                self.landing_y = self.rect.centery;
                self.log_offset = self.x - other_rect.x;
            return True;
        return False;

    def follow_log(self, log_rect):
        # Make Frogger follow the log when on it.
        if(self.is_on_log and not self.move_on_log):
            if(not self.x < 0):
                self.rect.centerx = log_rect.centerx;
                self.rect.centery = log_rect.centery;
                self.x = self.rect.centerx;
            else:
                self.x = self.x;