import time


def can_position_group_here(starting_position, group_size, springs, max_length):
    if starting_position > 0 and springs[starting_position-1] == 1:
        return False
    if starting_position + group_size > max_length:
        return False
    if starting_position + group_size < max_length and springs[starting_position+group_size] == 1:
        return False
    for i in range(group_size):
        if springs[starting_position + i] > 0:
            continue
        return False
    return True


def no_hashtags_left(starting_position, springs, max_length):
    for i in range(starting_position, max_length):
        if springs[i] == 1:
            return False
    return True


def hashtags_missed(starting_position, end, springs):
    for i in range(starting_position, end):
        if springs[i] == 1:
            return True
    return False


def recursive_function(starting_position, numbers, springs, max_length):
    answer = 0
    if len(numbers) <= 0 and no_hashtags_left(starting_position, springs, max_length):
        return 1
    elif len(numbers) <= 0:
        pass
    elif starting_position >= max_length:
        pass
    else:
        for i in range(starting_position, max_length):
            if hashtags_missed(starting_position, i, springs):
                break
            elif len(numbers) <= 0 and no_hashtags_left(starting_position, springs, max_length):
                return answer + 1
            elif len(numbers) <= 0:
                break
            elif can_position_group_here(i, numbers[0], springs, max_length):
                copy_numbers = numbers.copy()
                g = copy_numbers.pop(0)
                new_starting_position = i + g + 1
                answer += recursive_function(new_starting_position, copy_numbers, springs, max_length)
            elif springs[i] == 1:
                break
    return answer


def main():
    with open("inputs/input12.txt") as file:
        puzzle = file.readlines()
        answer = 0
        for line in puzzle:
            springs, numbers = line[:-1].split(" ")
            numbers = [int(x) for x in numbers.split(",")]
            springs = [0 if v == "." else 1 if v == "#" else 2 for v in springs]

            max_length = len(springs)
            permutations = recursive_function(0, numbers, springs, max_length)
            print(f"working permutations for this run: {permutations}")
            answer += permutations

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
