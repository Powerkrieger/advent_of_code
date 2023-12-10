import time


def traverse_pipes(move, on_the_move, puzzle, x_max, y_max, starting_pos):
    main_loop = []
    starting_dirs = []
    starting_char = "S"
    for ix, (dir, pos) in enumerate(on_the_move, start=1):
        try:
            check = move[dir][puzzle[pos[0]][pos[1]]]
            main_loop.append((puzzle[pos[0]][pos[1]], pos))
            starting_dirs.append(ix)
        except KeyError:
            print(f"path {ix} ends here")
    if 1 in starting_dirs:
        if 2 in starting_dirs:
            starting_char = "-"
        elif 3 in starting_dirs:
            starting_char = "F"
        elif 4 in starting_dirs:
            starting_char = "L"
    elif 2 in starting_dirs:
        if 3 in starting_dirs:
            starting_char = "7"
        elif 4 in starting_dirs:
            starting_char = "J"
    elif 3 in starting_dirs:
        if 4 in starting_dirs:
            starting_char = "|"
    main_loop.append((starting_char, starting_pos))

    for i in range(y_max * x_max):
        new_on_the_move = []
        new_positions = []
        for ix, (dir, pos) in enumerate(on_the_move, start=1):
            try:
                new_dir = move[dir][puzzle[pos[0]][pos[1]]]
            except KeyError:
                print(f"path {ix} ends here")
                continue
            new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
            if new_pos in new_positions:
                print(f"position to meet {new_pos}")
                return i + 2, main_loop
            else:
                new_positions.append(new_pos)
                main_loop.append((puzzle[new_pos[0]][new_pos[1]], new_pos))
            new_on_the_move.append((new_dir, new_pos))
        on_the_move = new_on_the_move
    print("This is not possible")
    raise Exception


def get_inside_area(y_max, x_max, zero_map):
    counter = 0

    for pos_y in range(y_max - 1):
        open_flag = False
        for pos_x in range(x_max):
            if open_flag:
                if zero_map[pos_y][pos_x] in ["F", "|", "7"] \
                        and zero_map[pos_y + 1][pos_x] in ["|", "J", "L"]:
                    open_flag = False
                if zero_map[pos_y][pos_x] == "0":
                    counter += 1
                    zero_map[pos_y][pos_x] = "*"
            elif zero_map[pos_y][pos_x] in ["F", "|", "7"] \
                    and zero_map[pos_y + 1][pos_x] in ["|", "J", "L"]:
                open_flag = True

    return counter, zero_map


def main():
    with open("inputs/input10.txt") as file:
        puzzle = file.readlines()
        y_max = len(puzzle)
        x_max = len(puzzle[0][:-1])
        print(f"y max = {y_max}")
        print(f"x max = {x_max}")
        starting_pos = (0, 0)
        zero_map = []
        for pos_y, line in enumerate(puzzle):
            zero_line = []
            for pos_x, letter in enumerate(line[:-1]):
                zero_line.append("0")
                if letter == "S":
                    print(f"starting y,x = {pos_y}, {pos_x}")
                    starting_pos = [pos_y, pos_x]
            zero_map.append(zero_line)

        from_below = {"|": (-1, 0), "7": (0, -1), "F": (0, 1)}
        from_atop = {"|": (1, 0), "J": (0, -1), "L": (0, 1)}
        from_west = {"-": (0, 1), "J": (-1, 0), "7": (1, 0)}
        from_east = {"-": (0, -1), "L": (-1, 0), "F": (1, 0)}
        move = {(-1, 0): from_below, (1, 0): from_atop, (0, 1): from_west, (0, -1): from_east}

        on_the_move = [((0, 1), [starting_pos[0], starting_pos[1] + 1]),
                       ((0, -1), [starting_pos[0], starting_pos[1] - 1]),
                       ((1, 0), [starting_pos[0] + 1, starting_pos[1]]),
                       ((-1, 0), [starting_pos[0] - 1, starting_pos[1]])]

        steps, main_loop = traverse_pipes(move, on_the_move, puzzle, x_max, y_max, starting_pos)

        print(f"steps for half the loop: {steps}")

        for pipe, (pos_y, pos_x) in main_loop:
            zero_map[pos_y][pos_x] = pipe

        # print main loop without rest
        if x_max <= 20:
            print("Only main loop:\n")
            for line in zero_map:
                print(line)

        print("\n=============================\n")

        answer, zero_map = get_inside_area(y_max, x_max, zero_map)

        # print main loop and inside area as "*"
        if x_max <= 20:
            print("Inside area marked")
            for line in zero_map:
                print(line)

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
