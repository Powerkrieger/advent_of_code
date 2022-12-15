import numpy as np

def visible(highest, this):
    if int(this) > int(highest):
        return True
    else:
        return False

def scene(forest, x, y, row_edge, col_edge):
    height = forest[x][y]
    right = 1
    left = 1
    top = 1
    bottom = 1
    row_edge = row_edge -1
    col_edge = col_edge -1

    ix = x+1
    while ix < row_edge and forest[ix][y] < height :
        right += 1
        ix += 1

    ix = x-1
    while ix > 0 and forest[ix][y] < height :
        left += 1
        ix -= 1

    iy = y+1
    while iy < col_edge and forest[x][iy] < height:

        bottom += 1
        iy += 1

    iy = y-1
    while iy > 0 and forest[x][iy] < height:
        top += 1
        iy -= 1

    if x == 0 or x == row_edge:
        right = 0
    if y == 0 or y == col_edge:
        bottom = 0

    return right * left * bottom * top



with open("input_day_08.txt", "r+") as file1:

    forest = []
    row = 0
    for line in file1:
        if line.strip() != "":
            row += 1
            forest.append(line.strip())

    col = len(line.strip())

    print(str(row) + " by " + str(col))

    #top
    mask1 = np.full((row,col), False)
    for ix in range(col):
        highest = -1
        for iy in range(row):
            if visible(highest, forest[iy][ix]):
                mask1[iy][ix] = True
                highest = forest[iy][ix]
    print("shape " + str(mask1.shape))

    #bottom
    mask2 = np.full((row,col), False)
    for ix in range(col):
        highest = -1
        for iy in range(row-1, -1, -1):
            if visible(highest, forest[iy][ix]):
                mask2[iy][ix] = True
                highest = forest[iy][ix]

    #left
    mask3 = np.full((row,col), False)
    for iy in range(row):
        highest = -1
        for ix in range(col):
            if visible(highest, forest[iy][ix]):
                mask3[iy][ix] = True
                highest = forest[iy][ix]

    #right
    mask4 = np.full((row,col), False)
    highest = -1
    for iy in range(row):
        highest = -1
        for ix in range(col-1, -1, -1):
            if visible(highest, forest[iy][ix]):
                mask4[iy][ix] = True
                highest = forest[iy][ix]

    #add together
    count = 0
    vis_count = 0
    not_count = 0
    mask5 = np.full((row,col), False)
    for ix in range(row):
        for iy in range(col):
            count += 1
            if mask1[iy][ix] or mask2[iy][ix] or mask3[iy][ix] or mask4[iy][ix]:
                mask5[iy][ix] = True
                vis_count += 1
            else:
                not_count += 1


    print("99 * 99 = " + str(99*99))
    print("count " + str(count))
    print("visible " + str(vis_count))
    print("not visible" + str(not_count))


    max = 0
    for ix in range(row):
        for iy in range(col):
            value = scene(forest, ix, iy, row, col)
            if value > max:
                max = value

    print("best scenic value: " + str(max))
