import os
from copy import deepcopy
from time import sleep
from random import randint

MATRIX_SIZE = 20

class GameOfLife:

    def __init__(self,  living, matrix_size=MATRIX_SIZE):
        self.matrix_size = matrix_size
        self.grid = self.new_matrix()
        self.new_grid = self.new_matrix()
        self.grid_cords = self.get_coordinates()
        self.living_cells = living
        self.set_live_cells()
        self.next_gen_living = set()

    def set_live_cells(self):
        for i in self.living_cells:
            self.grid[i[0]][i[1]] = True
    
    def new_matrix(self):
        one_row = list(False for _ in range(self.matrix_size))
        smth = []
        for i in range(self.matrix_size):
            smth.append(deepcopy(one_row))
        return smth

    def get_coordinates(self):
        smth = set()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                smth.add((i, j))
        return smth
    
    def calculate_next_generation(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.new_grid[i][j] = self.calculate_liveness(i, j)
                # EASY DEBUG !
#                for s in self.new_grid:
#                    print(s)
#                print('--------------------')
        return self.new_grid


    def calculate_liveness(self, x, y):
        count = 0
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self.validate_coordinates(i, j):
                    if self.grid[i][j]:
                        count += 1
                else:
                    pass
        # EASY DEBUG !
        #print('Count for: ', (x, y), 'is', count, 'and bool: ', self.grid[x][y])
        if self.grid[x][y]:
            count -= 1
            if 2 <= count <= 3:
                self.next_gen_living.add((x,y))
                return True
        else:
            if count == 3:
                self.next_gen_living.add((x,y))
                return True
        return False

    def validate_coordinates(self, x, y):
        if (x, y) in self.grid_cords:
            return True
        return False
    
    def random_population(self):
        '''When called resets self.next_gen_living'''
        self.next_gen_living = set()
        random_list = [i for i in self.grid_cords]
        random_range = randint(1, len(self.grid_cords))
        for i in range(1, random_range):
            random_resurect = randint(1, random_range)
            self.next_gen_living.add(random_list[random_resurect])
        return self.next_gen_living


''' To use we need instance of GameOfLife(argv), 
    where argv should be a set of the coordinates of 
    the living cells in the next generation.
    1st generation of living cells are given by input
    in start().
    foo.next_gen_living is the atribute that returns 
    the cells for next iteration.'''

def start():
    living_cells = int(input())
    starting_cells = set()
    for i in range(living_cells):
        starting_cells.add(tuple(int(i)-1 for i in input() if i != ' '))
    return starting_cells

if __name__ == '__main__':

    foo = GameOfLife(start())

    while True:
        for row in foo.grid:
            for cell in row:
                if cell:
                    print('o', end=' ')
                else:
                    print('.', end=' ')
            print()
        print('='*40)
        foo.calculate_next_generation()
        foo = GameOfLife(foo.next_gen_living)
        sleep(1)
        os.system('clear')
        if len(foo.living_cells) == 0:
            s = input('Press R if you want random population or Q to quit: ')
            if s == 'R' or s == 'r':
                foo = GameOfLife(foo.random_population())
            else:
                break


