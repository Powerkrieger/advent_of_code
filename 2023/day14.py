import time


def count_weight_on_pole(platform):
    answer = 0
    for line in platform:
        weight = []
        start = 0
        max_space = len(line)
        for i, space in enumerate(line, start=1):
            if space == "O":
                weight.append(max_space - start)
                start += 1
            elif space == "#":
                start = i
        answer += sum(weight)
    return answer


def main():
    with open("inputs/input14.txt") as file:
        puzzle = file.readlines()

        platform = []
        for line in puzzle:
            platform.append(line[:-1])

        platform = list(zip(*platform))
        answer = count_weight_on_pole(platform)
        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
