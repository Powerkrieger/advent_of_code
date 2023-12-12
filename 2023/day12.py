import time

import numpy as np


def generate_groups(perms, springs, number_of_twos):
    groups = []
    for i in range(perms):
        new_springs = []
        perm_counter = 0
        binary = f"{i:b}".zfill(number_of_twos)
        for letter in springs:
            if letter > 1:
                new_springs.append(int(binary[perm_counter]))
                perm_counter += 1
            else:
                new_springs.append(letter)
        groups.append(new_springs)
    return groups


def count_groups(group):
    result_groups = []
    group_counter = 0
    group_flag = False
    for i in group:
        if i == 1 and group_flag:
            group_counter += 1
        elif i == 1:
            group_counter = 1
            group_flag = True
        elif i == 0 and group_flag:
            group_flag = False
            result_groups.append(group_counter)
            group_counter = 0
    if group_flag:
        result_groups.append(group_counter)
    return result_groups


def main():
    with open("inputs/input12.txt") as file:
        puzzle = file.readlines()
        answer = 0
        for line in puzzle:
            springs, numbers = line[:-1].split(" ")
            numbers = [int(x) for x in numbers.split(",")]
            springs = [0 if v == "." else 1 if v == "#" else 2 for v in springs]

            unknowns = springs.count(2)
            perms = 2**unknowns

            print("===============================")
            print(f"permutations to check: {perms}")

            groups_to_check = generate_groups(perms, springs, unknowns)

            permutations = 0
            for group in groups_to_check:
                check = count_groups(group)
                if np.array_equal(numbers, check):
                    permutations += 1

            print(f"working permutations for this run: {permutations}")
            answer += permutations

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
