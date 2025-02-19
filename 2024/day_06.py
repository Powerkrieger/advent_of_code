import re

with open("inputs/input_day_06.txt", "r+") as file1:
#with open("inputs/test_day_06.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    matrix = []
    e = []
    f = []
    g = []

    for i, line in enumerate(file1):
        if "^" in line:
            y = i
            x = line.index("^")
        line = line.replace("\n", "")
        matrix.append(list(line.replace("^", ".")))

print(matrix)
print(x)
print(y)


starting_pos_x = x
starting_pos_y = y

bounds_x = len(matrix[0])
bounds_y = len(matrix)


nextdir = {(0, -1): [1, 0],
           (1, 0): [0, 1],
           (0, 1): [-1, 0],
           (-1, 0): [0, -1]}

current_dir = [0, -1]

def out_of_bounds(ix, iy):
    if 0 <= ix < bounds_x and 0 <= iy < bounds_y:
        return False
    else:
        return True

def next_pos(m, ix, iy, curr_dir:list):
    next_x = curr_dir[0] + ix
    next_y =  curr_dir[1] + iy
    if out_of_bounds(next_x ,next_y):
        return "done", next_x, next_y, curr_dir
    if m[next_y][next_x] == ".":
        return "move", next_x, next_y, curr_dir
    elif m[next_y][next_x] == "#":
        curr_dir = nextdir[(curr_dir[0], curr_dir[1])]
        next_x = curr_dir[0] + ix
        next_y = curr_dir[1] + iy
        return "turn", next_x, next_y, curr_dir


loop_list = []
for j in range(len(matrix)):
    for k in range(len(matrix[0])):
        print(str(j) + " " + str(k))
        if k == starting_pos_x and j == starting_pos_y:
            continue
        before = matrix[j][k]
        if before == "#":
            continue
        matrix[j][k] = "#"
        positions = set()
        loop = False
        x = starting_pos_x
        y = starting_pos_y
        current_dir = [0, -1]
        while not out_of_bounds(x, y):
            len1 = len(positions)
            positions.add((x, y, current_dir[0], current_dir[1]))
            len2 = len(positions)

            if len1 == len2:
                # old move
                print("loop!!!")
                loop = True
                break

            move, x, y, current_dir = next_pos(matrix, x, y, current_dir)
            #print(move)

        loop_list.append(loop)
        matrix[j][k] = before

c = loop_list.count(True)



print("solution")
print(c)
