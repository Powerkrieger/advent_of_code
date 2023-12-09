import math
import time

import numpy as np


def go_until_z(node, network, lr_sequence, seq_i=0):
    seq_length = len(lr_sequence)
    steps = 0
    while node[2] != "Z":
        seq_i = seq_i % seq_length
        node = network[node][lr_sequence[seq_i]]
        seq_i += 1
    return seq_i


def main():
    with open("../inputs/input08.txt") as file:
        puzzle = file.readlines()
        answer = []

        lr_sequence = [0 if direction == "L" else 1 for direction in puzzle[0][:-1]]

        network = {}
        x_nodes = []
        for node in puzzle[2:]:
            network[node[:3]] = (node[7:10], node[12:15])
            if node[2] == "A":
                x_nodes.append(node[:3])

        print(network)

        sequences = {}
        # !!!! wont work, not necessarily circles !!!!
        loop_offset_lengths = [[0, 0] for _ in x_nodes]
        print(loop_offset_lengths)
        seq_length = len(lr_sequence)
        for i, starting_node in enumerate(x_nodes):
            seq_i = 0
            steps = 0
            visited = [(starting_node, seq_i)]
            next_node = (network[starting_node][lr_sequence[seq_i]], seq_i+1)
            seq_i += 1
            while next_node not in visited:
                # print(visited)
                seq_i = seq_i % seq_length
                seq_i_plus = seq_i + 1 % seq_length
                visited.append(next_node)
                next_node = (network[next_node[0]][lr_sequence[seq_i]], seq_i_plus)
                seq_i += 1
                steps += 1
            loop_offset_lengths[i][0] = steps - 1
            steps = 0
            sequences[i] = []
            while next_node not in sequences[i]:
                seq_i = seq_i % seq_length
                seq_i_plus = seq_i + 1 % seq_length
                sequences[i].append(next_node)
                next_node = (network[next_node[0]][lr_sequence[seq_i]], seq_i_plus)
                seq_i += 1
                steps += 1
            print(steps)
            loop_offset_lengths[i][1] = steps

        print(loop_offset_lengths)

        for key in sequences.keys():
            print(f"sequence with {key}, length {len(sequences[key])}")
            for z_index, (node, i) in enumerate(sequences[key]):
                #print(node)
                if node[2] == "Z":
                    print(f"hooray, {z_index}")
                    continue
        for x in loop_offset_lengths:
            answer.append(x[1])

        print(f"answer: {math.lcm(*answer)}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
