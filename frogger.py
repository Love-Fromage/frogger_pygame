import pygame
import sys

import pygame.locals
from Frog import Frog
from Car import Car
from Log import Log

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
FPS=14;


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Frogger in Python");

# Sounds goes here!
pygame.mixer.init();
looping_sound = pygame.mixer.Sound("./assets/sounds/Grind.mp3");
looping_sound.play(loops=-1);
looping_sound.set_volume(0.1);
ouch_sound = pygame.mixer.Sound("./assets/sounds/Low Thud.mp3");
ouch_sound.set_volume(0.5);
game_over_music = pygame.mixer.Sound("./assets/sounds/Music_Loop_4_Full.wav");
game_over_music.set_volume(0.1);

game_grid = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
];


frogger_image = pygame.image.load("./assets/frogger.png").convert_alpha();
frogger_image = pygame.transform.scale(frogger_image, (GRID_SIZE, GRID_SIZE));
frog_life_image = frogger_image;
frog_life_image = pygame.transform.scale(frog_life_image, (GRID_SIZE/2, GRID_SIZE/2));
car_image = pygame.image.load("./assets/police_car.png");
road_image = pygame.image.load("./assets/road.png");
game_over_text = pygame.image.load("./assets/game_over_text.png").convert_alpha();
game_over_bg = pygame.image.load("./assets/game_over_bg.png");

game_over_alpha = 255;
game_over_direction = 1;
game_over_speed = 7;
game_over_text.set_alpha(game_over_alpha);

car = Car(car_image, 15, 8, "left");
car2 = Car(car_image, -1, 7, "right");

frogger = Frog(frogger_image, x=8, y=10, game_grid=game_grid);
life1 = Frog(frog_life_image, x=0, y=11, game_grid=game_grid);
life2 = Frog(frog_life_image, x=1, y=11, game_grid=game_grid);
life3 = Frog(frog_life_image, x=2, y=11, game_grid=game_grid);
log1 = Log(200, 50, 15, 2, "left", 0.12);
log2 = Log(200, 50, 16, 3, "right", 0.20);
log3 = Log(200, 50, 0, 4, "right", 0.15);
log4 = Log(200, 50, 2, 5, "left", 0.12);



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

def draw_game(frogger, car):
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
                # pygame.draw.rect(screen, (0,0,0), (col*GRID_SIZE, row*GRID_SIZE, GRID_SIZE, GRID_SIZE));
                screen.blit(road_image,(col*GRID_SIZE, row*GRID_SIZE) )
            elif cell_value == -1:
                # thats the void
                pygame.draw.rect(screen, (0,0,0), (col*GRID_SIZE, row*GRID_SIZE, GRID_SIZE, GRID_SIZE));
            
            # pygame.draw.rect(screen, (230, 0,0), (15*GRID_SIZE, 8*GRID_SIZE+ GRID_SIZE/4, GRID_SIZE/2, GRID_SIZE/2))
            


    # Draw frogger
    log1.draw(screen);
    log2.draw(screen);
    log3.draw(screen);
    log4.draw(screen);
    # pygame.draw.rect(screen, (255,0,0), (((log4.rect.right-(log4.rect.width/3))), (log4.rect.top+log4.rect.height/2), 2,2));

    #testing 

    frogger.draw(screen);
    car.draw(screen);
    car2.draw(screen);
    
    if frogger.life == 3:
        life1.draw(screen) 
        life2.draw(screen) 
        life3.draw(screen)
    elif frogger.life == 2:
        life1.draw(screen)
        life2.draw(screen)
    elif frogger.life == 1:
        life1.draw(screen);


    #Draw other game elements here
    # Draw hitboxes for debugging
    # pygame.draw.rect(screen, (0,0,255), frogger.rect, 2);
    # pygame.draw.rect(screen, (255,0,255), car.rect, 2);

    if is_game_over:
        global game_over_alpha, game_over_direction
        screen.blit(game_over_bg, (0,0))
        game_over_alpha += game_over_direction * game_over_speed;
        if game_over_alpha >= 255:
            game_over_alpha = 255;
            game_over_direction = -1;
        elif game_over_alpha <= 0:
            game_over_alpha = 0;
            game_over_direction = 1;
        game_over_text.set_alpha(game_over_alpha);
        screen.blit(game_over_text, (0,0));
    

    pygame.display.flip(); # Update the display


is_game_over = False;
def game_over():
        global is_game_over 
        is_game_over = True;
        car.game_over = True;
        frogger.game_over = True;
        looping_sound.stop();
        game_over_music.play(loops=-1);
        print("cest fini")
        return

logs = [
    log1,
    log2,
    log3,
    log4
];
def check_if_touch_water():
        # for row in range(ROWS):
        #     for col in range(COLS):
        #         cell_value = game_grid[row][col];
        #         if cell_value == 1:
        #             if frogger.grid_x == row and frogger.grid_y == col:
        #                 print("water");
    if not frogger.on_log: 
        cell_value = game_grid[int(frogger.grid_y)][int(frogger.grid_x)];
        if cell_value == 1:
            print("water");
    # frogger.lose_hp();
    # frogger.grid_x = frogger.initial_x;
    # frogger.grid_y = frogger.initial_y;
    # frogger.pixel_x, frogger.pixel_y = frogger.get_pixel_position();
    # frogger.rect.topleft = (frogger.pixel_x, frogger.pixel_y);

# Game loop
game_is_running = True;
while game_is_running:
    if frogger.life == 0 and not is_game_over:
        game_over();
        



    handle_key_events(frogger);

    if not is_game_over:
        if (frogger.rect.colliderect(car.rect) or frogger.rect.colliderect(car2.rect)) and not frogger.invulnerable:
            ouch_sound.play();

        frogger.check_collision_car(car.rect);
        frogger.check_collision_car(car2.rect);
        frogger.check_collision_log(logs);
        if frogger.ouch:
            ouch_sound.play();

        # check_if_touch_water();


    if frogger.invulnerable:
        frogger.invulnerable_timer -=1;
        if frogger.invulnerable_timer <=0:
            frogger.invulnerable = False;
            frogger.alpha = 255;
        else:
            frogger.alpha += frogger.alpha_change_direction;
            if frogger.alpha <= 50 or frogger.alpha >=255:
                frogger.alpha_change_direction *= -1;
    car.move();
    car2.move();
    log1.move();
    log2.move();
    log3.move();
    log4.move();
    draw_game(frogger, car);
    # Cap the frame rate 
    CLOCK.tick(FPS);