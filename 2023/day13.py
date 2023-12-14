import copy
import time
import numpy as np


def check_for_mirror(i, pat):
    row_length = len(pat)
    mirror = []
    for up, down in zip(range(i, -1, -1), range(i+1, row_length, 1)):
        mirror.append(up)
        mirror.append(down)
        if not np.array_equal(pat[up], pat[down]):
            return []
    return mirror


def is_difference_one(difference):
    flag = False
    for i in difference:
        if i != 0 and not flag:
            flag = True
        elif i != 0:
            return False
    if flag is True:
        return True
    else:
        return False


def compute(pattern):
    result_horizontal = []
    result_vertical = []
    pat = pattern
    row_length = len(pat)
    for i in range(row_length - 1):
        if np.array_equal(pat[i], pat[i + 1]):
            # possibly mirror
            if check_for_mirror(i, pat):
                result_horizontal.append((i + 1) * 100)
    pat = list(zip(*pattern))
    row_length = len(pat)
    for i in range(row_length - 1):
        if np.array_equal(pat[i], pat[i+1]):
            # possibly mirror
            if check_for_mirror(i, pat):
                result_vertical.append(i + 1)
    return result_horizontal, result_vertical


def replace_one(pattern, row, col):
    new_pattern = copy.deepcopy(pattern)
    new_pattern[row][col] = 0 if pattern[row][col] == 1 else 1
    return new_pattern


def choose_smudge(possible_smudge, pattern):
    result_old_h, result_old_v = compute(pattern)
    for row, col, result_h, result_v in possible_smudge:
        if result_h and result_v:
            # both are lists > 0
            for h in result_h:
                if h in result_old_h:
                    continue
                return h, row, col
            for v in result_v:
                if v in result_old_v:
                    continue
                return v, row, col
            print("shit")
            raise Exception
        elif result_h and np.array_equal(result_h, result_old_h):
            continue
        elif result_h:
            for h in result_h:
                if h in result_old_h:
                    continue
                return h, row, col
        elif result_v and np.array_equal(result_v, result_old_v):
            continue
        elif result_v:
            for v in result_v:
                if v in result_old_v:
                    continue
                return v, row, col
    print("this is not wanted")
    raise Exception


def compute_new(pattern):
    row_length = len(pattern)
    col_length = len(pattern[0])
    possible_smudge = []
    for row in range(row_length):
        for col in range(col_length):
            new_pattern = replace_one(pattern, row, col)
            result_h, result_v = compute(new_pattern)
            if (result_h or result_v):
                possible_smudge.append((row, col, result_h, result_v))
    print(f"possible_smudges {possible_smudge}")
    return choose_smudge(possible_smudge, pattern)


def main():
    with open("inputs/input13.txt") as file:
        puzzle = file.readlines()
        answer = 0
        count_rows = 0
        pattern = []
        for line in puzzle:
            if line == "\n":
                result, row, col = compute_new(pattern)
                print(f"result {result}, {row}, {col}")
                answer += result
                count_rows = 0
                pattern = []
            else:
                pattern.append([0 if x == "." else 1 for x in line[:-1]])
                count_rows += 1
        if count_rows > 0:
            result, row, col = compute_new(pattern)
            print(f"result {result}, {row}, {col}")
            answer += result
        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))