import pygame
import sys
from Frog import Frog

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Frogger in Python");

# Set up game variables
clock = pygame.time.Clock()
fps=30
frog_speed = 5;
leap_speed = 10;
lowest_y_position = height - 50;
highest_y_position = 0; 
# frogger_image = pygame.image.load("./assets/frogger.png").convert_alpha();
# frogger_rect = frogger_image.get_rect();
# frogger_rect.topleft = (100, 300);



class Terrain:
    def __init__(self, x,y, width, height, color):
        # Set terrain properties
        self.rect = pygame.Rect(x,y,width,height);
        self.color = color;
    def draw(self, screen):
        # Draw the terrain as a filled rectangle
        pygame.draw.rect(screen, self.color, self.rect);


class Log:
    def __init__(self, x, y, width, height, color, direction, speed):
        # Set log properties
        self.rect = pygame.Rect(x,y,width,height);
        self.x = x;
        self.color = color;
        self.direction = direction;
        self.speed = speed;
    def draw(self, screen):
        # Draw the log as a filled rectangle
        pygame.draw.rect(screen, self.color, self.rect);
    def move(self):
        # move the log to the left
        if(self.direction == "left"):
            # Check if the log is out the screen
            if(not self.rect.right < 0):
                self.rect.x -= self.speed;
            else:
                self.rect.x = width;



# Create the frog 
frogger = Frog('./assets/frogger.png', width/2, height-50);
highest_y_position = frogger.image.get_height();

# Add a log
log_left = Log(width, height-152, 200, 50, (0,0,0), "left", 5);

# Create a terrain object
starting_zone = Terrain(0,height-100, width, 100, (166,141,80));

# Initialize key state tracking
key_pressed = { 'up': False, 'down': False, "left": False, "right":False};

# Game loop
while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        # Game logic goes here
    keys = pygame.key.get_pressed()
    
    if(keys[pygame.K_LEFT]):
            frogger.move_horizontal(-frogger.speed);

    else:
        frogger.rotate_back();
    if(keys[pygame.K_RIGHT]):
        frogger.move_horizontal(frogger.speed);
    

    if(keys[pygame.K_UP]):
        if(not key_pressed['up']):
            key_pressed['up'] = True;
            if(frogger.y > highest_y_position-50):
                frogger.start_leap(1); # Leap up
    else: 
        key_pressed['up'] = False;

    if(keys[pygame.K_DOWN]):
        if(not key_pressed['down']):
            key_pressed['down'] = True;
            if(frogger.y < lowest_y_position):
                frogger.start_leap(-1); # Leap down
    else:
        key_pressed['down'] = False;
    
    log_left.move();

    # Ensure the frog stays within vertical boundaries
    if frogger.y > lowest_y_position:
        frogger.y = lowest_y_position;
    if frogger.y < highest_y_position -50:
        frogger.y = highest_y_position -50;

    if frogger.check_collision(log_left.rect):
        frogger.is_on_log = True;
    else:
        frogger.is_on_log = False;
        frogger.move_on_log = False;

    frogger.follow_log(log_left.rect);

    frogger.update();
    

    # Clear the screen
    screen.fill((33, 157, 225));

    # Draw the game objects
    starting_zone.draw(screen);
    log_left.draw(screen);
    
    frogger.draw(screen);



    # Update the display
    pygame.display.flip();  


    # Cap the frame rate 
    clock.tick(fps);