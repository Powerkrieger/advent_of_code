import re

import numpy as np


def check_if_true(matrix, mask):
    print(len(matrix))
    print(mask.shape)
    result = 0
    gear_score = 0
    star_dict = {}
    for x, line in enumerate(matrix, start=0):

        counter = 0
        numbers = re.findall("[0-9]*", line)
        only_numbers = []
        for letter in numbers:
            if letter != '':
                only_numbers.append(int(letter))
        print(only_numbers)
        number_flag = False

        for y, letter in enumerate(line, start=0):
            if letter.isdigit():
                if mask[x][y] > 0:
                    if only_numbers[counter] > 0:
                        star_dict.setdefault(mask[x][y], []).append(only_numbers[counter])
                    only_numbers[counter] = 0
                number_flag = True
            elif letter == "." and number_flag is True:
                counter += 1
                number_flag = False
                continue
            elif letter.isascii() and number_flag is True:
                counter += 1
                number_flag = False
                continue
    for key in star_dict.keys():
        if len(star_dict[key]) == 2:
            gear_score += star_dict[key][0] * star_dict[key][1]
    return gear_score


if __name__ == "__main__":
    with open("inputs/input03.txt") as file:
        df = file.readlines()
        answer = 0
        # for every line of input
        special_characters = []
        digit_mask = []
        special_characters_mask = []
        neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
        star_id = 1
        for i, line in enumerate(df):
            line = line[:-1]
            df[i] = line
            for x in line:

                if not x.isdigit() and x != '.' and x != '\n' and not x in special_characters:
                    special_characters.append(x)
            digit_mask.append([1 if x.isdigit() else 0 for x in line])
            special_characters_mask.append([idx if x == "*" else 0 for idx, x in enumerate(line, start=star_id)])
            star_id += len(special_characters_mask[i])

        special_characters_mask = np.array(special_characters_mask)
        new_special_characters_mask = np.zeros(
            shape=(special_characters_mask.shape[0], special_characters_mask.shape[1]))

        for x in range(special_characters_mask.shape[0]):
            for y in range(special_characters_mask.shape[1]):
                for n in neighbors:
                    try:
                        if special_characters_mask[x + n[0]][y + n[1]] > 0:
                            new_special_characters_mask[x][y] = special_characters_mask[x + n[0]][y + n[1]]
                            break
                    except IndexError:
                        continue
        digit_mask = np.array(digit_mask)
        answer = check_if_true(df, new_special_characters_mask)

        print(f"answer {answer}")
