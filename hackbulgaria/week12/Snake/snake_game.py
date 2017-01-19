# from snake_game import *
from copy import deepcopy

# TODO: http://getemoji.com/#food-drink link for emojis HTML5

class GameWorld:
    def __init__(self, size, contents=None):
        self.size = size
        self.contents = contents
        self.valid_grid = set()
        self.field = self.create_map(Cell)
    
    def create_map(self, cell_cls):
        _field = [[cell_cls() for _ in range(self.size)] for _ in range(self.size)]
        return _field     
    
    def add_content(self, content_list: list):
        for cont in content_list:
            self.__getitem__(cont._x)[cont._y] = cont
    
    def __getitem__(self, index):
        return self.field[index]
    
    def __repr__(self):
        for row in self.field:
            for cell in row:
                print(cell.is_empty(), end=' ')
            print()
        return ''                         
        
class Cell:
    def __init__(self, content=None, _x=None, _y=None):
        self.content = content
        self._x = _x
        self._y = _y
        
    def is_empty(self):
        if self.content:
            return self.content
        else:
            return '⬜'
    
class WorldObject:
    def __init__(self):
        pass
                  
class Food(WorldObject):
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy
        self.cherry = '🍒'
    
    def __repr__(self):
        return self.cherry
             
class Wall(WorldObject):
    def __init__(self):
        self.wall = '⬛'  
    
    def __repr__(self):
        return self.wall
                
class BlackHole(WorldObject):
    def __init__(self):
        self.black_hole = '☢️'
    
    def __repr__(self):
        return self.black_hole
        
class Python:

#    UP = Vec2D(?, ?)
#    DOWN = Vec2D(?, ?)
#    LEFT = Vec2D(?, ?)
#    RIGHT = Vec2D(?, ?)
    
    def __init__(self, world, coords, size, direction):
        self.world = world
        self.coords = coords
        self.size = size
        self.direction = direction

    def move(self, direction):
        pass            
    
class Vec2D:
    def __init__(self, x, y):
      self.x = x
      self.y = y

#    def possition(self):
#        for row in range(len(self.field)):
#            for col in range(len(self.field[row])):
#                new_cell = cell_cls((row, col))
#                self.valid_grid.add((row, col))
    
    def python_head(self):
        pass
    
    def _add(self):
        pass
    
    def _sub(self):
        pass

    def _mul(self):
        pass
    
    def _negative(self):
        pass      
    
    def __eq__(self, other):
        return hash(other) == hash(self)

    def __hash__(self):
      return hash((self.x, self.y))
          
    def __getitem__(self, index):
        pass

#>>> ( Vec2D(1, 1) == -Vec2D(-1, -1) ) # True

class Error(Exception):
    pass
    
class DeathError(Error):
    pass

class DirectionError(Error):
    pass  
    
    
    
    
    
game = GameWorld(15)
wall1 = Cell(Wall(), 2, 7)
wall2 = Cell(Wall(), 3, 7)
wall3 = Cell(Wall(), 4, 7)
wall4 = Cell(Food('Cherry', 2), 10, 10)
game.add_content([wall1, wall2, wall3, wall4])
print(game)  
    
    
    
    
    
    
    
    
