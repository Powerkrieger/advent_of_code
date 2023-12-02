import numpy as np


def split_move(direction, steps):
    return [direction for i in range(int(steps))]


def need_to_move(pos_h, pos_t, direction):
    ### 9 possibilities for head to be in reference to self
    ## 00 01 02
    ## 10 11 12
    ## 20 21 22

    # print("H: " + str(pos_h) + " follower: " + str(pos_t))

    xh, yh = pos_h
    xt, yt = pos_t

    # 00
    if xh < xt and yh < yt:
        if np.isin(direction, ['U', 'L']):
            return True, -1, -1

    # 01
    if xh == xt and yh < yt:
        if np.isin(direction, ['U']):
            return True, 0, -1

    # 02
    if xh > xt and yh < yt:
        if np.isin(direction, ['U', 'R']):
            return True, 1, -1

    # 10
    if xh < xt and yh == yt:
        if np.isin(direction, ['L']):
            return True, -1, 0

    # 11
    if xh == xt and yh == yt:
        print("equal")
        return False, 0, 0

    # 12
    if xh > xt and yh == yt:
        if np.isin(direction, ['R']):
            return True, 1, 0

    # 20
    if xh < xt and yh > yt:
        if np.isin(direction, ['L', 'D']):
            return True, -1, 1

    # 21
    if xh == xt and yh > yt:
        if np.isin(direction, ['D']):
            return True, 0, 1

    # 22
    if xh > xt and yh > yt:
        if np.isin(direction, ['R', 'D']):
            return True, 1, 1

    print("not moving")
    return False, 0, 0


def switch(dir):
    if dir == 'R':
        return 1, 0
    elif dir == 'L':
        return -1, 0
    elif dir == 'U':
        return 0, -1
    elif dir == 'D':
        return 0, 1
    return -1


with open("inputs/input_day_09.txt", "r+") as file1:
    count = 0

    pos_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pos_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    visited = [(0, 0)]

    for line in file1:
        direction, steps = line.split(" ")
        list_directions = split_move(direction, steps)
        print("change dir to " + direction)
        for dir in list_directions:

            new_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            new_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            print("-> move 0")
            x_new, y_new = switch(dir)
            new_x[0] = x_new
            new_y[0] = y_new

            keep_moving = True

            ### first 9 knots of the rope
            for i in range(8):
                bool, new_x_t, new_y_t = need_to_move((pos_x[i], pos_y[i]), (pos_x[i + 1], pos_y[i + 1]), dir)
                if bool and keep_moving:
                    print("True -> move " + str(i + 1))
                    new_x[i + 1] = new_x_t
                    new_y[i + 1] = new_y_t
                else:
                    # print("why not stay")
                    keep_moving = False

            ### again for last pair because need to save visited positions here

            bool, new_x_t, new_y_t = need_to_move((pos_x[i + 1], pos_y[i + 1]), (pos_x[i + 2], pos_y[i + 2]), dir)

            if bool and keep_moving:
                # count += 1
                new_x[i + 2] = new_x_t
                new_y[i + 2] = new_y_t
                visited.append((pos_x[i + 2], pos_y[i + 2]))

            for i in range(10):
                pos_x[i] += new_x[i]
                pos_y[i] += new_y[i]

    ### debugging check
    last = (0, 0)
    for i in visited:
        a, b = last
        c, d = i
        if abs(a - c) >= 2 and abs(c - d) >= 2:
            print("Debug fail")
        last = i

    vis_dic = list(dict.fromkeys(visited))

    # print("moves " + str(count))
    print("visited " + str(len(visited)))
    print("set " + str(len(vis_dic)))
    print(vis_dic)
