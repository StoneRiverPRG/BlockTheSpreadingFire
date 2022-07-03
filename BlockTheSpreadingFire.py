import sys
import math

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
for i in range(height):
    grid_line = input()
    # Each character represents the type of a cell.
    # '#' is a safe cell. '.' is a tree cell. 'X' is a house cell.
    print(grid_line, file=sys.stderr)

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
    print("", file=sys.stderr)

    for i in range(height):
        for j in input().split():
            # fire_progress: state of the fire in this cell (-2: safe, -1: no fire, 0<=.<fireDuration: fire, fireDuration: burnt)
            fire_progress = int(j)
            print(f"{fire_progress:02}", end="", file=sys.stderr)
        print("", file=sys.stderr)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # WAIT if your intervention cooldown is not zero, else position [x] [y] of your intervention.
    print("WAIT")
