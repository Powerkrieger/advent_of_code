with open("inputs/input_day_04.txt", "r+") as file1:
    result = 0
    # read in the grid of rolls of papers (denoted by @) and empty spaces (denoted by .)
    grid = []
    for line in file1:
        grid.append(line.strip())

    # count initial number of @
    initial_rolls = 0
    for line in grid:
        initial_rolls += line.count('@')
    print(f"Initial rolls: {initial_rolls}")

    # check vonNeumann neighborhood for each @ if there are fewer than 4 adjacent @
    change = True
    while change == True:
        change = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '@':
                    # check all 8 directions for another @
                    directions = [(-1, -1), (-1, 0), (-1, 1),
                                  (0, -1), (0, 1),
                                  (1, -1), (1, 0), (1, 1)]
                    # count adjacent @
                    adjacent_count = 0
                    for direction in directions:
                        di, dj = direction
                        ni, nj = i + di, j + dj
                        if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                            if grid[ni][nj] == '@':
                                adjacent_count += 1
                    # if fewer than 4 adjacent @, remove this @
                    if adjacent_count < 4:
                        grid[i] = grid[i][:j] + '.' + grid[i][j+1:]
                        change = True

    # count initial number of @
    rolls_left = 0
    for line in grid:
        rolls_left += line.count('@')
    print(f"Left rolls: {rolls_left}")
    print(f"Removed rolls: {initial_rolls - rolls_left}")

    print(result)