import re
from asyncore import file_wrapper
from collections import defaultdict

from networkx.algorithms.operators.unary import reverse

with open("inputs/input_day_09.txt", "r+") as file1:
#with open("inputs/test_day_09.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    matrix = []
    e = []
    f = []
    space_list = []
    filelength_list = []

    for iy, line in enumerate(file1):
        l = [int(x) for x in line.replace("\n", "")]
        print(sum(l))
        for ix, x in enumerate(l):
            if ix % 2 == 0:
                e.extend([ix//2]*x)
                filelength_list.append(x)
            else:
                e.extend([-1]*x)
                space_list.append(x)

print(filelength_list)
space_list.append(0)
print(space_list)


fl = len(filelength_list)-1
add_between =0
while fl > 0:
    remove = False
    # add between = tupel added between 0 and fl
    #add_between = sum([1 for i,x in enumerate(filelength_list) if type(x) == tuple and i < fl])
    print(f"fl: {fl} and add between:{add_between} -> idx: {fl+add_between}")
    si = 0
    if type(filelength_list[fl+add_between]) == tuple:
        add_between-=1
        continue
    while si < fl+add_between:

        print(f"space idx {si}, {space_list[si]}")
        if filelength_list[fl+add_between] <= space_list[si]:
            old = space_list.pop(si)
            space_list.insert(si, 0)
            big_file = filelength_list.pop(fl+add_between)
            filelength_list.insert(si+1,(fl, big_file))


            space_list.insert(si+1, old-big_file)
            old2 = space_list.pop(fl+add_between)
            old3 = space_list.pop(fl+add_between)
            space_list.insert(fl+add_between, old2+big_file+old3)

            add_between += 1
            print(filelength_list)
            print(space_list)
            remove = True
            break
        si+=1
    if not remove:
        big_file = filelength_list.pop(fl + add_between)
        filelength_list.insert(fl + add_between, (fl, big_file))
    fl-=1

print(filelength_list)
print(space_list)

newlist = []
counter = 0
non_tuple_counter = 0
for idfile, space in zip(filelength_list, space_list):
    print(counter)
    if type(idfile) == tuple:
        for r in range(idfile[1]):
            print(counter*idfile[0])
            newlist.append(counter*idfile[0])
            counter+=1
    else:
        for r in range(idfile):
            print(counter*non_tuple_counter)
            newlist.append(counter*non_tuple_counter)
            counter += 1
        non_tuple_counter+=1
    counter += space

print(newlist)
c = sum(newlist)

# print(e)
# new_list = []
# for entry in e:
#     if entry == -1:
#         new = e.pop(-1)
#         while new == -1:
#             new = e.pop(-1)
#         new_list.append(new)
#         print(len(e))
#     else:
#         new_list.append(entry)
#
#
# for idx, holla in enumerate(new_list):
#     print(f"multiple = {idx} * {holla}")
#     c += idx * holla


print("solution")
print(c)