import pygame
import sys

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
        self.image = pygame.transform.scale(self.image, (50, 50));

        # Set the initial position of the frog
        self.x = x - self.image.get_width()/2;
        self.y = y;
        self.leap_distance = 50; # Distance of the frog leap
        self.is_leaping = False;
        self.leap_target_y = y;
        self.leap_direction = 0;

        # Set the initial velocity of the frog
        self.speed = frog_speed;
        self.leap_speed = leap_speed;

    def draw(self, screen):
        # Draw the frog
        screen.blit(self.image, (self.x, self.y));

    def move_horizontal(self, dx):
        # Update the frog's position
        self.x += dx;

    def start_leap(self, direction):
        # if not self.is_leaping:
            self.is_leaping = True;
            self.leap_direction = direction;
            self.leap_target_y = self.y - (self.leap_distance * direction);

    def update(self):
        if self.is_leaping:
            # Move towards the leap target
            if self.leap_direction == 1: # leaping up
                if self.y > self.leap_target_y:
                    self.y -= self.leap_speed;
                else:
                    self.y = self.leap_target_y;
                    self.is_leaping = False;
            elif self.leap_direction == -1: # Leaping down
                if self.y < self.leap_target_y:
                    self.y += self.leap_speed;
                else:
                    self.y = self.leap_target_y;
                    self.is_leaping = False;

class Terrain:
    def __init__(self, x,y, width, height, color):
        # Set terrain properties
        self.rect = pygame.Rect(x,y,width,height);
        self.color = color;
    def draw(self, screen):
        # Draw the terrain as a filled rectangle
        pygame.draw.rect(screen, self.color, self.rect);


# Create the frog
frogger = Frog('./assets/frogger.png', width/2, height-50);
highest_y_position = frogger.image.get_height();

# Create a terrain object
starting_zone = Terrain(0,height-100, width, 100, (166,141,80));

# Initialize key state tracking
key_pressed = { 'up': False, 'down': False};

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
    
    #Update frog leap
    frogger.update();
      # Ensure the frog stays within vertical boundaries
    if frogger.y > lowest_y_position:
        frogger.y = lowest_y_position;
    if frogger.y < highest_y_position -50:
        frogger.y = highest_y_position -50;

    # Clear the screen
    screen.fill((33, 157, 225));

    # Draw the game objects
    starting_zone.draw(screen);
    frogger.draw(screen);



    # Update the display
    pygame.display.flip();  


    # Cap the frame rate 
    clock.tick(fps);