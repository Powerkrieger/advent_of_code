import time

import numpy as np


def ordering_function(in1, in2):
    pass


def hand_type(num_hot_hand):
    # 0en 1en 2en 3en 4en 5e
    bins = np.bincount(np.array(num_hot_hand), minlength=6)
    # 5 of a kind
    if bins[5] > 0:
        return 6
    # 4 of a kind
    if bins[4] > 0:
        return 5
    # full house
    if bins[3] > 0 and bins[2] > 0:
        return 4
    # 3 of a kind
    if bins[3] > 0:
        return 3
    # two pair
    if bins[2] > 1:
        return 2
    # pair
    if bins[2] > 0:
        return 1
    return 0

def main():
    with open("inputs/input07.txt") as file:
        puzzle = file.readlines()
        answer = 0

        order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
        deck = []

        for line in puzzle:
            hand, bid = line[:-1].split(" ")
            hand = [order.index(x) + 2 for x in hand]
            num_hot_hand = [0] * 13
            for i in hand:
                num_hot_hand[i - 2] += 1
            hand_type(num_hot_hand)
            deck.append((hand_type(num_hot_hand), hand, int(bid)))

        deck.sort(key=lambda row: (row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4]), reverse=True)
        total_rank = len(deck)
        for _, _, bid in deck:
            print(f"{bid}*{total_rank}")
            answer += bid * total_rank
            total_rank -= 1

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
