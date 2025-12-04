with open("inputs/input_day_04.txt", "r+") as file1:
    result = 0
    # read in the grid of rolls of papers (denoted by @) and empty spaces (denoted by .)
    grid = []
    for line in file1:
        grid.append(line.strip())

    # check vonNeumann neighborhood for each @ if there are fewer than 4 adjacent @
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                # check all 8 directions for another @
                directions = [(-1, -1), (-1, 0), (-1, 1),
                              (0, -1),          (0, 1),
                              (1, -1), (1, 0), (1, 1)]
                # count adjacent @
                adjacent_count = 0
                for direction in directions:
                    di, dj = direction
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[i]):
                        if grid[ni][nj] == '@':
                            adjacent_count += 1
                if adjacent_count < 4:
                    result += 1

    print(result)