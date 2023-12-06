import time


def main():
    with open("inputs/input06.txt") as file:
        df = file.readlines()
        answer = 1
        time = [int(x) for x in df[0][5:-1].split(" ") if x != '']
        dist = [int(x) for x in df[1][9:-1].split(" ") if x != '']
        print(time)
        print(dist)

        for t, d in zip(time, dist):
            count = 0
            for i in range(t):
                if i * (t - i) > d:
                    count += 1
            answer *= count

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
