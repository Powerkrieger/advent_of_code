import math
import time


def solve(node, network, lr_sequence):
    x = node
    seq_i = 0
    seq_length = len(lr_sequence)
    count = 0
    while x[2] != "Z":
        seq_i = seq_i % seq_length
        # print(network[x][lr_sequence[seq_i]])
        try:
            x = network[x][lr_sequence[seq_i]]
        except Exception:
            print(seq_i)
            raise Exception
        count += 1
        seq_i += 1
    return count


def main():
    with open("inputs/input08.txt") as file:
        puzzle = file.readlines()
        lr_sequence = [0 if direction == "L" else 1 for direction in puzzle[0][:-1]]
        answer = []
        network = {}
        starting_nodes = []
        for node in puzzle[2:]:
            network[node[:3]] = (node[7:10], node[12:15])
            if node[2] == "A":
                starting_nodes.append(node[:3])

        for node in starting_nodes:
            answer.append(solve(node, network, lr_sequence))

        print(answer)
        print(*answer)  # *mind blown*

        print(f"answer: {math.lcm(*answer)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
