_map = '''..##.....T
          #.##..###.
          #H###E###E
          #.E...###.
          ###T#####G'''

map_grid = [list(i) for i in _map.split()]

def test(x, y):
    for i in range(x-1, x+2):
        if i >= 0 and i < len(map_grid[i]):
            for j in range(y-1, y+2):
                if j >= 0 and j:
                    print(map_grid[i][j])
        
def get_coordinates():
    smth = set()
    for i in range(len(map_grid)):
        for j in range(len(map_grid[i])):
            smth.add((i, j))
    return smth
#for row in range(len(map_grid)):
#    for i in range(len(map_grid[row])):
#        if map_grid[row][i] == 'H':
#            test(row, i)

test(4,8)

