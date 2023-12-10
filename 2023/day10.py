import time


def main():
    with open("inputs/input10.txt") as file:
        puzzle = file.readlines()
        answer = 0
        y_max = len(puzzle)
        x_max = len(puzzle[0])
        print(f"y max = {y_max}")
        print(f"x max = {x_max}")
        starting_pos = (0, 0)
        for pos_y, line in enumerate(puzzle):
            for pos_x, letter in enumerate(line[:-1]):
                if letter == "S":
                    print(f"starting y,x = {pos_y}, {pos_x}")
                    starting_pos = [pos_y, pos_x]

        from_below = {"|": (-1, 0), "7": (0, -1), "F": (0, 1)}
        from_atop = {"|": (1, 0), "J": (0, -1), "L": (0, 1)}
        from_west = {"-": (0, 1), "J": (-1, 0), "7": (1, 0)}
        from_east = {"-": (0, -1), "L": (-1, 0), "F": (1, 0)}
        # move = [from_below, from_atop, from_west, from_east]
        move = {(-1, 0): from_below, (1, 0): from_atop, (0, 1): from_west, (0, -1): from_east}

        print(move)

        on_the_move = [((0, 1), [starting_pos[0], starting_pos[1] + 1]),
                       ((0, -1), [starting_pos[0], starting_pos[1] - 1]),
                       ((1, 0), [starting_pos[0] + 1, starting_pos[1]]),
                       ((-1, 0), [starting_pos[0] - 1, starting_pos[1]])]

        print(on_the_move)

        answer = traverse_pipes(move, on_the_move, puzzle, x_max, y_max)

        print(f"answer: {answer}")


def traverse_pipes(move, on_the_move, puzzle, x_max, y_max):
    for i in range(y_max * x_max):
        new_on_the_move = []
        new_positions = []
        for ix, (dir, pos) in enumerate(on_the_move):
            print(f"{ix}: {pos}")
            try:
                new_dir = move[dir][puzzle[pos[0]][pos[1]]]
            except KeyError:
                print("path ends here")
                continue
            new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
            if new_pos in new_positions:
                print(f"position to meet {new_pos}")
                return i+2
            else:
                new_positions.append(new_pos)
            new_on_the_move.append((new_dir, new_pos))
        on_the_move = new_on_the_move
    return 0


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
