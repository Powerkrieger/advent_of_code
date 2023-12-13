import time

import numpy as np


def check_for_mirror(i, pat):
    row_length = len(pat)
    # for 0 - number of rows - 2
    mirror = []
    for up, down in zip(range(i, -1, -1), range(i+1, row_length, 1)):
        mirror.append(up)
        mirror.append(down)
        if not np.array_equal(pat[up], pat[down]):
            return []
    return mirror


def compute(pattern):

    for multiply_by, pat in [(100, pattern), (1, list(zip(*pattern)))]:
        row_length = len(pat)
        # for 0 - number of rows - 2
        for i in range(row_length - 1):
            if np.array_equal(pat[i], pat[i+1]):
                # possibly mirror
                if check_for_mirror(i, pat):
                    return multiply_by * (i+1)


def main():
    with open("inputs/input13.txt") as file:
        puzzle = file.readlines()
        answer = 0
        count_rows = 0
        pattern = []
        for line in puzzle:
            if line == "\n":
                result = compute(pattern)
                print(f"result {result}")
                answer += result
                count_rows = 0
                pattern = []
            else:
                pattern.append([0 if x == "." else 1 for x in line[:-1]])
                count_rows += 1
        if count_rows > 0:
            result = compute(pattern)
            print(f"result {result}")
            answer += result

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))