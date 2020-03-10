# MODULES
import pygame
import pandas as pd





def runner(n_x, n_y, agent_pos, target_pos, timestep, fast = True):
    
    agent_pos_x = agent_pos[0]
    agent_pos_y = agent_pos[1]
    target_pos_x = target_pos[0]
    target_pos_y = target_pos[1]
    

    # PARAMETERS

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # WIDTH and HEIGHT of each grid location
    WIDTH = 13
    HEIGHT = 13
    # margin between each cell
    MARGIN = 5

    WINDOW_SIZE = [1500, 1000]


    # FUNCTIONS 

    def create_grid():
        grid = []
        for row in range(n_y+1):
            grid.append([])
            for column in range(n_x+1):
                grid[row].append(0)  # Append a cell
        return grid

    
    def plot_grid(grid):
        grid[agent_pos_y][agent_pos_x] += 2
        grid[target_pos_y][target_pos_x] += 1
        for row in range(n_y+1):
            for column in range(n_x+1):
                color = WHITE
                if grid[row][column] == 1:
                    color = BLACK
                elif grid[row][column] == 2:
                    color = RED
                elif grid[row][column] == 3:
                    color = GREEN
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])   


    def write(text, x, y):
        font = pygame.font.Font('freesansbold.ttf', 12) 
        text = font.render(text, True, WHITE, BLACK) 
        textRect = text.get_rect()  
        textRect.center = (x, y) 
        screen.blit(text, textRect)    


    # dataset creator
    # RUN ONLY IF YOU WANT TO CREATE A NEW ROUTE
    # CODE 

    pygame.init()
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("ENVIRONMENT")
    clock = pygame.time.Clock()
    grid = create_grid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
    screen.fill(BLACK) 
    plot_grid(grid)
    write('Time: '+str(timestep), 530, 10)
    if fast == False:
        clock.tick(3)
    else: 
        clock.tick(1000)
    pygame.display.flip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    