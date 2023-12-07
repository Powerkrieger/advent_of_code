import time

import numpy as np


def split_move(direction, steps):
    return [direction for _ in range(int(steps))]


def need_to_move(pos_head, pos_tail, direction):
    # 9 possibilities for head to be in reference to self

    # 00 01 02
    # 10 11 12
    # 20 21 22

    xh, yh = pos_head
    xt, yt = pos_tail

    assert abs(xt - xh) <= 1
    assert abs(yt - yh) <= 1

    left = direction[0] < 0
    right = direction[0] > 0
    up = direction[1] > 0
    down = direction[1] < 0

    # 00
    if xh < xt and yh > yt:
        if right and up:
            return True, 0, 1
        if left and down:
            return True, -1, 0
        if left or up:
            return True, -1, 1

    # 01
    if xh == xt and yh > yt:
        if up:
            return True, direction[0], 1

    # 02
    if xh > xt and yh > yt:
        if left and up:
            return True, 0, 1
        if right and down:
            return True, 1, 0
        if right or up:
            return True, 1, 1

    # 10
    if xh < xt and yh == yt:
        if left:
            return True, -1, direction[1]

    # 11
    if xh == xt and yh == yt:
        return False, 0, 0

    # 12
    if xh > xt and yh == yt:
        if right:
            return True, 1, direction[1]

    # 20
    if xh < xt and yh < yt:
        if right and down:
            return True, 0, -1
        if left and up:
            return True, -1, 0
        if left or down:
            return True, -1, -1

    # 21
    if xh == xt and yh < yt:
        if down:
            return True, direction[0], -1

    # 22
    if xh > xt and yh < yt:
        if left and down:
            return True, 0, -1
        if right and up:
            return True, 1, 0
        if right or down:
            return True, 1, -1

    # print("why and how ...???") # move inwards for example
    return False, 0, 0


def switch(direction):
    if direction == 'R':
        return 1, 0
    elif direction == 'L':
        return -1, 0
    elif direction == 'U':
        return 0, 1
    elif direction == 'D':
        return 0, -1
    raise Exception("wrong direction input")


def debug_visited(visited):
    # check for unrealistic movement
    last = (0, 0)
    for i in visited:
        a, b = last
        c, d = i
        if abs(a - c) >= 2 and abs(c - d) >= 2:
            print("Debug fail")
        last = i
    print("=========")
    offset = 3000
    bounds = (6100, 6000)
    df = np.array([["."] * bounds[0]] * bounds[1])
    for pos in visited:
        df[pos[1] + offset][pos[0] + offset] = '#'
    df[offset][offset] = "s"
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    print(df[::-1, :])


def debug_visually(pos_x, pos_y):
    print("=========")
    offset = 15
    bounds = (40, 40)
    df = np.array([["."] * bounds[0]] * bounds[1])
    for i in range(len(pos_x)):
        df[pos_y[i] + offset][pos_x[i] + offset] = i
    df[offset][offset] = "s"
    np.set_printoptions(threshold=np.inf)
    np.set_printoptions(linewidth=np.inf)
    print(df[::-1, :])


def main():
    with open("inputs/input_day_09.txt", "r+") as file1:
        count = 0
        pos_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        pos_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        visited = [(0, 0)]

        dimension = {'R':0,
                     'L':0,
                     'U':0,
                     'D':0}

        for line in file1:
            direction, steps = line.split(" ")
            dimension[direction] += int(steps)
            list_directions = split_move(direction, steps)
            for direction in list_directions:
                new_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                new_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

                # move head first
                head_x_move, head_y_move = switch(direction)
                new_x[0] = head_x_move
                new_y[0] = head_y_move

                keep_moving = True
                # first 9 knots of the rope
                for i in range(8):
                    bool, new_x_t, new_y_t = need_to_move(pos_head=(pos_x[i], pos_y[i]),
                                                          pos_tail=(pos_x[i + 1], pos_y[i + 1]),
                                                          direction=(new_x[i], new_y[i]))
                    if bool and keep_moving:
                        new_x[i + 1] = new_x_t
                        new_y[i + 1] = new_y_t
                    else:
                        keep_moving = False

                # again for last pair because need to save visited positions here

                bool, new_x_t, new_y_t = need_to_move(pos_head=(pos_x[i + 1], pos_y[i + 1]),
                                                      pos_tail=(pos_x[i + 2], pos_y[i + 2]),
                                                      direction=(new_x[i + 1], new_y[i + 1]))
                assert i == 7
                if bool and keep_moving:
                    count += 1
                    new_x[i + 2] = new_x_t
                    new_y[i + 2] = new_y_t

                for i in range(10):
                    pos_x[i] += new_x[i]
                    pos_y[i] += new_y[i]
                visited.append((pos_x[-1], pos_y[-1]))

            # debug_visually(pos_x, pos_y)

        # debug_visited(visited)
        # print(visited)
        print("moves " + str(count))
        print("visited " + str(len(visited)))
        print("set " + str(len(set(visited))))
        print(dimension)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
