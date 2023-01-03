import pygame
import time
import random



rows, cols = 32, 24 
white = (255, 255, 255)
black = (0, 0, 0)



class Cell:
    def __init__(self):
        self.hollow = False 
        #self.hollow_neighbors = 0
        #self.viable = False
        self.visited = False



def main():     
    grid = make_map(rows, cols)
    make_outer_walls(grid)

    cellStack = []

    cellStack.append((1, 1))

    while (len(cellStack) > 0):
        curr = cellStack.pop()
        if (grid[curr[0]][curr[1]].visited == False):
            hollow_neighbors = False

            if (grid[curr[0] - 1][curr[1] - 1].hollow):
                if (grid[curr[0]][curr[1] - 1].hollow):
                    if (grid[curr[0] - 1][curr[1]].hollow):
                        hollow_neighbors = True 

            if (grid[curr[0] + 1][curr[1] + 1].hollow):
                if (grid[curr[0]][curr[1] + 1].hollow):
                    if (grid[curr[0] + 1][curr[1]].hollow):
                        hollow_neighbors = True

            if (grid[curr[0] - 1][curr[1] + 1].hollow):
                if (grid[curr[0]][curr[1] + 1].hollow):
                    if (grid[curr[0] - 1][curr[1]].hollow):
                        hollow_neighbors = True

            if (grid[curr[0] + 1][curr[1] - 1].hollow):
                if (grid[curr[0]][curr[1] - 1].hollow):
                    if (grid[curr[0] + 1][curr[1]].hollow):
                        hollow_neighbors = True

            num_hollow_neighbors = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (grid[curr[0] + i][curr[1] + j].hollow):
                        num_hollow_neighbors += 1
            if num_hollow_neighbors > 3:
                hollow_neighbors = True

            if (hollow_neighbors):
                grid[curr[0]][curr[1]].hollow = False 
                grid[curr[0]][curr[1]].visited = True
                continue
            else:
                grid[curr[0]][curr[1]].hollow = True 
                grid[curr[0]][curr[1]].visited = True
        unvisited_ns = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0:
                    if j == 0:
                        continue
                #grid[curr[0] + i][curr[1] + j].hollow_neighbors += 1
                # only want to traverse directly above or to the sides 
                if abs(i) == abs(j):
                    continue
                if grid[curr[0] + i][curr[1] + j].visited == False:
                    unvisited_ns.append((curr[0] + i, curr[1] + j))
                
        if len(unvisited_ns) > 0:
            cellStack.append(curr)
            rand_choice = random.choice(unvisited_ns)
            cellStack.append(rand_choice)

        time.sleep(.05)
        print_maze(grid)
    time.sleep(5)



def print_maze(grid):
    window = pygame.display.set_mode((900, 600))
    pygame.display.set_caption('Maze')
    window.fill(white)
    left_offset = 16
    top_offset = 16

    for i in range(rows):
        for j in range(cols):
            if grid[i][j].hollow:
                pygame.draw.rect(window, white, 
                        (top_offset  + (16 * i),
                         left_offset + (16 * j),
                         16, 16))
            else:
                pygame.draw.rect(window, black, 
                        (top_offset  + (16 * i),
                         left_offset + (16 * j),
                         16, 16))

    pygame.display.update()


def make_outer_walls(grid):
    for i in range(rows):
        grid[i][0].visited = True
        grid[i][0].hollow = False 
        grid[i][cols - 1].visited = True
        grid[i][cols - 1].hollow = False 
    
    for i in range(cols):
        grid[0][i].visited = True
        grid[0][i].hollow = False 
        grid[rows - 1][i].visited = True
        grid[rows - 1][i].hollow = False 
 


def make_map(r, c):
    mapArr = []

    for i in range(r):
        col = []
        for j in range(c):
            col.append(Cell())
        mapArr.append(col)

    return mapArr



if __name__ == "__main__":
    main()
