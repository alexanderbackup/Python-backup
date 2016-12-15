# strawberries.py
from copy import deepcopy

def strawberries(rows, columns, days, dead_strawberries: list):
    if not(0 < columns <= rows <= 1000):
        raise ValueError()
    if not(0 <= days <= 1000):
        raise ValueError()
    field = [[True for i in range(columns)] for i in range(rows)]
    valid_cords = set()
    for row in range(len(field)):
        for col in range(len(field[row])):
            valid_cords.add((row, col))
            if (row, col) in dead_strawberries:
                field[row][col] = False
    iter_field = [deepcopy(i) for i in field]
    while days+1:
        alive = 0
        for row in range(len(iter_field)):
            for col in range(len(iter_field[row])):
                if not iter_field[row][col]:
                    #decay(row, col)
                    if (row, col-1) in valid_cords:
                        field[row][col-1] = False
                    if (row, col+1) in valid_cords:
                        field[row][col+1] = False
                    if (row-1, col) in valid_cords:
                        field[row-1][col] = False
                    if (row+1, col) in valid_cords:
                        field[row+1][col] = False
                else:
                    alive += 1
        iter_field = [deepcopy(i) for i in field]
        days -= 1
    return alive







strawberries(8, 10, 2, [(4, 8), (2, 7)])

#def matrix_bombing_plan(m):
#	cord_damage = {}
#	result = {}
#	matrix_hp = sum(sum(i) for i in m)
#	for row in range(len(m)):
#		for col in range(len(m[row])):
#			cord_damage[(row, col)] = m[row][col] # {(row, col): damage}

#	for k, damage in cord_damage.items():
#		damage_done = 0
#		for i in range(k[0]-1, k[0]+2):
#			for j in range(k[1]-1, k[1]+2):
#				if (i, j) in cord_damage and (i, j) != k:
#					if m[i][j] > damage:
#						damage_done += damage
#					else:
#						damage_done +=(m[i][j])
#		result[k] = matrix_hp - damage_done
#	return result
