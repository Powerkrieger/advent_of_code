import time


def new_seq_check_zero(old_seq):
    length = len(old_seq)
    new_seq = []
    all_zeros = True
    for i in range(length - 1):
        new_seq.append(old_seq[i + 1] - old_seq[i])
        if new_seq[-1] != 0:
            all_zeros = False
    if all_zeros:
        return old_seq[0]
    else:
        first_value_of_row_below = new_seq_check_zero(new_seq)
        return old_seq[0] - first_value_of_row_below


def main():
    with open("inputs/input09.txt") as file:
        puzzle = file.readlines()
        answer = 0
        for line in puzzle:
            sequence = [int(x) for x in line[:-1].split(" ")]
            print(new_seq_check_zero(sequence))
            answer += new_seq_check_zero(sequence)

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
