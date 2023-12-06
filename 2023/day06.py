import time


def main():
    with open("inputs/input06.txt") as file:
        df = file.readlines()
        answer = 1
        time = [int(df[0][5:-1].replace(" ", ""))]
        dist = [int(df[1][9:-1].replace(" ", ""))]
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
