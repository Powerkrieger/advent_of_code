if __name__ == "__main__":
    with open("inputs/input04.txt") as file:
        df = file.readlines()
        answer = 0
        for line in df:
            card, winning_numbers = line.split("|")
            card_id, numbers = card.split(":")
            card, id = [x for x in card_id.split(" ") if x != '']
            numbers = [x for x in numbers.split(" ") if x != '']
            winning_numbers = [x for x in winning_numbers.split(" ") if x != '']
            winning_numbers[-1] = winning_numbers[-1].replace("\n", "")
            print(f"card with id {id}, {numbers} and winning ns {winning_numbers}")

            power = len([x for x in numbers if x in winning_numbers])
            print(power)
            if power > 0:
                answer += 2**(power-1)

        print(f"answer: {answer}")
