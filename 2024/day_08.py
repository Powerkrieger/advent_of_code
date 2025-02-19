import re
from collections import defaultdict

with open("inputs/input_day_08.txt", "r+") as file1:
#with open("inputs/test_day_08.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    matrix = []
    e = []
    f = []
    set_antidodes = set()
    charmap = set()

    antennas = defaultdict(list)

    for iy, line in enumerate(file1):
        matrix.append(list(line.replace("\n", "")))
        for ix, x in enumerate(list(line.replace("\n", ""))):
            antennas[x].append([iy, ix])

antennas.pop(".")

boundsy = len(matrix)
boundsx = len(matrix[0])

print(f"bounds {boundsy} {boundsx}")

for a in antennas.keys():
    if len(antennas[a]) <= 1:
        antennas.pop(a)

def out_of_bounds(y, x):
    if x >= boundsx or x < 0:
        return True
    elif y >= boundsy or y < 0:
        return True
    return False


for a in antennas.keys():
    matches = antennas[a]
    for match1 in matches:
        for match2 in matches:
            if match1 == match2:
                continue
            print(f"match {match1}, {match2}")
            disty = match1[0] - match2[0]
            distx = match1[1] - match2[1]
            #print(f"{distx}, {disty}")
            for i in range(1, boundsx):
                new_y = match1[0] - (i* disty)
                new_x = match1[1] - (i* distx)
                print(f"new pos {new_y}, {new_x}")
                if not out_of_bounds(new_y, new_x):
                    set_antidodes.add((new_y, new_x))


print(matrix)
print(antennas)
for y, x in set_antidodes:
    matrix[y][x] = "#"

for row in matrix:
    print(f"{row}")

print("solution")
print(set_antidodes)
print(len(set_antidodes))
