import sys
import math
import random

def sum_score(mapXY_list, t_value, h_value):
    """sum_score sum of all map of tree and house value

    Args:
        mapXY_list (list): map list (2 deg)
        t_value (int): tree value
        h_value (int): house value

    Returns:
        int: sum score
    """
    score = 0
    for yline in mapXY_list:
        for _x in yline:
            if _x == ".": # tree
                score += t_value
            elif _x == "X": # house
                score += h_value
            elif _x == "#":
                score += 0
            else:
                print("some error !", file=sys.stderr)
    return score


def Area_Check(maplist, x, y):
    wdth = len(maplist[0])
    hght = len(maplist)
    if (0 <= x < wdth) and (0 <= y < hght):
        return True
    else:
        return False


def Cuttable(gridmap_list, firemap_list, x, y):
    if Area_Check(gridmap_list, x, y):
        if (gridmap_list[y][x] != "#") and (firemap_list[y][x] == -1):
                return True
        else:
            return False
    else:
        return False


def Neighbor_Coord(gridmap_list, firemap_list, x, y):
    """Neighbor_Coord fire next neighbor coordinates

    Args:
        gridmap_list (list): grid map
        firemap_list (list): fire map
        x (int): fire x
        y (int): fire y

    Returns:
        list: list of tuple of fire neighbor like [(2, 2), (2, 3), ...]
    """
    neighbors = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direc in directions:
        if Cuttable(gridmap_list, firemap_list, x+direc[0], y+direc[1]):
            neighbors.append((x+direc[0], y+direc[1]))

    return neighbors


# Read the constant data of the map before the main loop, then read the state of the fire and give an action at each turn

# tree_treatment_duration: cooldown for cutting a "tree" cell
# tree_fire_duration: number of turns for the fire to propagate on adjacent cells from a "tree" cell
# tree_value: value lost if a "tree" cell is burnt or cut
tree_treatment_duration, tree_fire_duration, tree_value = [int(i) for i in input().split()]
# house_treatment_duration: cooldown for cutting a "house" cell
# house_fire_duration: number of turns for the fire to propagate on adjacent cells from a "house" cell
# house_value: value lost if a "house" cell is burnt or cut
house_treatment_duration, house_fire_duration, house_value = [int(i) for i in input().split()]
# width: number of columns in the grid
# height: number of rows in the grid
width, height = [int(i) for i in input().split()]
# fire_start_x: column where the fire starts
# fire_start_y: row where the fire starts
fire_start_x, fire_start_y = [int(i) for i in input().split()]

grid_map = []
# map data

for i in range(height):
    grid_line = input()
    # Each character represents the type of a cell.
    # '#' is a safe cell. '.' is a tree cell. 'X' is a house cell.
    grid_map.append(grid_line)
    print(grid_line, file=sys.stderr)
Ini_score = sum_score(grid_map, tree_value, house_value)
print(f"Initial score = {Ini_score}", file=sys.stderr)

# print Initial data
print("Tree Treat, Fire Duration, Value ",file=sys.stderr)
print(tree_treatment_duration, tree_fire_duration, tree_value, file=sys.stderr)
print("",file=sys.stderr)

print("House Treat, Fire Duration, Value ",file=sys.stderr)
print(house_treatment_duration, house_fire_duration, house_value, file=sys.stderr)
print("",file=sys.stderr)

print(f"width, height = ({width}, {height})", file=sys.stderr)
print(f"fire starts ({fire_start_x}, {fire_start_y})", file=sys.stderr)


# game loop
while True:
    cooldown = int(input())  # number of turns remaining before you can cut a new cell
    # the number of turns before you can give the instruction of cutting a cell
    # (≥ 1 means you have to WAIT / == 0 means you can give a cell to cut).
    print(f"cooldown = {cooldown}", file=sys.stderr)
    print(f"score = {sum_score(grid_map, tree_value, house_value)}", file=sys.stderr)
    print("", file=sys.stderr)

    fire_map = [[] for _ in range(height)]
    # fire progress map Initialize
    # print(fire_map, file=sys.stderr)

    for i in range(height):
        for j in input().split():
            # fire_progress: state of the fire in this cell
            # (-2: safe, -1: no fire, 0<=.<fireDuration: fire, fireDuration: burnt)
            fire_progress = int(j)
            fire_map[i].append(fire_progress)
            print(f"{fire_progress:2}", end="", file=sys.stderr)
        print("", file=sys.stderr)

    print(fire_map, file=sys.stderr)
    # Write an action using print
    # To debug: print("Debusg messages...", file=sys.stderr, flush=True)


    # WAIT if your intervention cooldown is not zero, else position [x] [y] of your intervention.
    if cooldown != 0:
        print("WAIT")
    else:
        targets = []
        for _y, yline in enumerate(fire_map):
            for _x, xline in enumerate(yline):
                if xline >= 0:
                    temp_targets = Neighbor_Coord(grid_map, fire_map, _x, _y)
                    for temp in temp_targets:
                        if temp not in targets:
                            targets.append(temp)
        print(f"targets = {targets}", file=sys.stderr)

        # print(f"Neighbor {Neighbor_Coord(grid_map, fire_map, fire_start_x, fire_start_y)}", file=sys.stderr)
        if not targets:
            print("WAIT")
        else:
            target_x, target_y = random.choice(targets)
            print(f"Neighbor {Neighbor_Coord(grid_map, fire_map, target_x, target_y)}", file=sys.stderr)
            #Todo: scan map and add fire neighbors (duplicate eliminate)
            print(f"({target_x}, {target_y}) = {grid_map[target_y][target_x]}", file=sys.stderr)
            if Cuttable(grid_map, fire_map, target_x, target_y):
                print(f"{target_x} {target_y}")
            else:
                print("WAIT")