import pygame
import sys

import pygame.locals
from Frog import Frog

# Initialize Pygame
pygame.init()

# Set up the display
# Define constants for the game
GRID_SIZE = 50 ; # Size of the cells in pixels
ROWS = 12;
COLS = 16;
SCREEN_WIDTH = COLS * GRID_SIZE;
SCREEN_HEIGHT = ROWS * GRID_SIZE;
CLOCK = pygame.time.Clock();
FPS=30;

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger in Python");


game_grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
];


frogger_image = pygame.image.load("./assets/frogger.png");
frogger_image = pygame.transform.scale(frogger_image, (GRID_SIZE, GRID_SIZE));

frogger = Frog(frogger_image, x=8, y=11);


def handle_key_events(frogger):
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.QUIT;
            sys.exit();

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                frogger.move("up");
            elif event.key == pygame.K_DOWN:
                frogger.move("down");
            elif event.key == pygame.K_LEFT:
                frogger.move("left");
            elif event.key == pygame.K_RIGHT:
                frogger.move("right");

def draw_game(frogger):
    screen.fill(( 0,0,0 )); # clear screen with black color

    for row in range(ROWS):
        for col in range(COLS):
            cell_value = game_grid[row][col];
    
            if cell_value == 0:
                # draw grass
                pygame.draw.rect(screen, (37,211,102), (col*GRID_SIZE, row*GRID_SIZE, GRID_SIZE, GRID_SIZE));
            elif cell_value == 1:
                #draw water
                pygame.draw.rect(screen, (0,0,255), (col*GRID_SIZE, row*GRID_SIZE, GRID_SIZE, GRID_SIZE));
            elif cell_value == 2:
                # draw an road
                pygame.draw.rect(screen, (0,0,0), (col*GRID_SIZE, row*GRID_SIZE, GRID_SIZE, GRID_SIZE));
                 







    # Draw frogger
    frogger.draw(screen);

    #Draw other game elements here

    pygame.display.flip(); # Update the display



# Game loop
game_is_running = True;
while game_is_running:
    handle_key_events(frogger);
    frogger.check_collision(game_grid);
    draw_game(frogger);
    # Cap the frame rate 
    CLOCK.tick(FPS);