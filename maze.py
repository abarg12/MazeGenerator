import pygame


rows, cols = 16, 16


class Cell:
    def __init__(self):
        self.hollow = False


def main():     
    grid = make_map(rows, cols)
    for i in range(rows):
        for j in range(cols):
            print(grid[i][j].hollow)
    # cellStack = []


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
