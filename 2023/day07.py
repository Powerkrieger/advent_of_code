import time
import numpy as np


def hand_type(num_hot_hand):
    # 0en 1en 2en 3en 4en 5e
    print(f"num_hot_hand {num_hot_hand}")
    j = num_hot_hand[0]
    j_inc = np.ones_like(num_hot_hand) * j
    j_inc[0] = 0
    # num_hot_hand += j_inc
    bins = np.bincount(np.array(num_hot_hand), minlength=6)

    if len(bins) > 6:
        print(bins)
        raise Exception
    print(f"increased {num_hot_hand}, bins {bins}")
    # 5 of a kind
    if bins[5] > 0 or (bins[4] and j == 1) or (bins[3] and j == 2) or (bins[2] and j == 3) or (bins[1] and j == 4):
        return 6
    # 4 of a kind
    if bins[4] > 0 or (bins[3] and j == 1) or (bins[2] == 2 and j == 2) or (bins[1] and j == 3):
        return 5
    # full house
    if (bins[3] > 0 and bins[2] > 0) or (bins[2] == 2 and j >= 1):
        return 4
    # 3 of a kind
    if bins[3] > 0 or (bins[2] == 1 and j == 1) or (j == 2 and bins[1] == 3):
        return 3
    # two pair
    if bins[2] > 1 or j > 1:
        return 2
    # pair
    if bins[2] > 0 or j >= 1:
        return 1
    return 0


def main():
    with open("inputs/input07.txt") as file:
        puzzle = file.readlines()
        answer = 0

        order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
        deck = []

        x = [0] * 13
        x[0] = 5
        assert hand_type(x) == 6
        x[0] = 4
        x[1] = 1
        assert hand_type(x) == 6
        x[0] = 3
        x[2] = 1
        assert hand_type(x) == 5
        x[0] = 2
        x[3] = 1
        print(hand_type(x))
        assert hand_type(x) == 3
        x[0] = 1
        x[4] = 1
        assert hand_type(x) == 1
        x[0] = 0
        x[5] = 1
        assert hand_type(x) == 0
        print(hand_type(x))

        for line in puzzle:
            hand, bid = line[:-1].split(" ")
            hand = [order.index(x) for x in hand]
            num_hot_hand = [0] * 13
            for i in hand:
                num_hot_hand[i] += 1
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
