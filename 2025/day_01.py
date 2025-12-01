with open("inputs/input_day_01.txt", "r+") as file1:
    dial = 50
    zeros = 0
    for line in file1:
        direction, number = line[0], int(line[1:].strip())
        print(f"Start: {dial}, Direction: {direction}, Number: {number}, End {dial - number if direction == 'L' else dial + number}")
        if direction == "L":
            dial -= number
            while dial < 0:
                dial += 100

        elif direction == "R":
            dial += number
            while dial > 99:
                dial -= 100
        if dial == 0:
            zeros += 1
    print(zeros)