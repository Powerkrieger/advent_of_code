import time


def main():
    with open("inputs/input04.txt") as file:
        df = file.readlines()
        answer = 0
        copy_of = []
        for line in df:
            card, winning_numbers = line.split("|")
            card_id, numbers = card.split(":")
            card, id = [x for x in card_id.split(" ") if x != '']
            numbers = [x for x in numbers.split(" ") if x != '']
            winning_numbers = [x for x in winning_numbers.split(" ") if x != '']
            winning_numbers[-1] = winning_numbers[-1].replace("\n", "")

            copy_of.append(int(id))

            power = len([x for x in numbers if x in winning_numbers])
            if power <= 0:
                continue
            count_of_copies = len([x for x in copy_of if x == int(id)])
            for _ in range(count_of_copies):
                for i in range(1, power + 1):
                    copy_of.append(int(id) + i)

        answer = len(copy_of)
        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
