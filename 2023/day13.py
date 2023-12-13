import time
import numpy as np


def recheck(pattern, count_rows, starting_index):
    if starting_index * 2 < count_rows - 1:

        for i, x in zip(range(starting_index, -1, -1), range(1, starting_index*2 + 2, 2)):
            if not np.array_equal(pattern[i], pattern[i + x]):
                return False
        return True
    else:
        for i, x in zip(range(starting_index+1, count_rows), range(1, starting_index*2 + 1, 2)):
            if not np.array_equal(pattern[i], pattern[i - x]):
                return False
        return True


def compute(pattern, count_rows):
    result = 0
    count_cols = len(pattern[0])
    turned_pattern = list(zip(*pattern))
    if count_rows < count_cols:
        # find mirror horizontally first
        for i in range(count_rows - 1):
            if np.array_equal(pattern[i], pattern[i + 1]):
                if recheck(pattern, count_rows, i):
                    return 100 * (i+1)
        # else find vertical mirror
        for i in range(count_cols - 1):
            if np.array_equal(turned_pattern[i], turned_pattern[i + 1]):
                if recheck(turned_pattern, count_cols, i):
                    return (i+1)
    else:
        # find mirror vertically first
        for i in range(count_cols - 1):
            if np.array_equal(turned_pattern[i], turned_pattern[i + 1]):
                if recheck(turned_pattern, count_cols, i):
                    return (i+1)
        # find mirror horizontally
        for i in range(count_rows - 1):
            if np.array_equal(pattern[i], pattern[i + 1]):
                if recheck(pattern, count_rows, i):
                    return 100 * (i+1)

    return result


def main():
    with open("inputs/input13.txt") as file:
        puzzle = file.readlines()
        answer = 0

        count_rows = 0
        pattern = []
        for line in puzzle:
            if line == "\n":
                result = compute(pattern, count_rows)
                print(f"result {result}")
                answer += result
                count_rows = 0
                pattern = []
            else:
                pattern.append(line[:-1])
                count_rows += 1
        if count_rows > 0:
            result = compute(pattern, count_rows)
            print(f"result {result}")
            answer += result

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
