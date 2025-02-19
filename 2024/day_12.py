import re
from asyncore import file_wrapper
from collections import defaultdict

#with open("inputs/input_day_12.txt", "r+") as file1:
with open("inputs/test_day_12.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    matrix = []
    e = []
    f = []
    space_list = []
    filelength_list = []

    coords = {idx_x+1j*idx_y: char for idx_y, line in enumerate(file1) for idx_x, char in enumerate(line[:-1])}
    perimeters = {}
get_inside_bounds = lambda cx: coords.get(cx, "")


for char_pos in coords:
    neighbors = 0
    for direction in [1, 1j,  -1, -1j]:
        neighbors += get_inside_bounds(char_pos) == get_inside_bounds(char_pos+direction)
    perimeters[c] = (c,neighbors)




print("solution")
print(c)