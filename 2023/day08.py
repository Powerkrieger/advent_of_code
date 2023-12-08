import time


def main():
    with open("inputs/input08.txt") as file:
        puzzle = file.readlines()
        answer = 0

        lr_sequence = [0 if direction == "L" else 1 for direction in puzzle[0][:-1]]

        network = {}
        for node in puzzle[2:]:
            network[node[:3]] = (node[7:10], node[12:15])

        print(network)

        x = "AAA"
        seq_i = 0
        seq_length = len(lr_sequence)

        while x != "ZZZ":
            seq_i = seq_i % seq_length
            print(network[x][lr_sequence[seq_i]])
            x = network[x][lr_sequence[seq_i]]
            answer += 1
            seq_i += 1

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
