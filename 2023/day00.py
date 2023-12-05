import time


def main():
    with open("inputs/input_test.txt") as file:
        df = file.readlines()
        answer = 0
        for line in df:
            pass

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
