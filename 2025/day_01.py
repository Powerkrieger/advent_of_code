with open("inputs/input_day_01.txt", "r+") as file1:
    dial = 50
    zeros = 0
    for line in file1:
        direction, number = line[0], int(line[1:].strip())
        print(f"Start: {dial}, Direction: {direction}, Number: {number}, End {dial - number if direction == 'L' else dial + number}")
        if direction == "L":
            if dial == 0:
                zeros_to_add = -1
            else:
                zeros_to_add = 0
            dial -= number
            while dial < 0:
                dial += 100
                zeros_to_add += 1

        elif direction == "R":
            dial += number
            zeros_to_add = 0
            while dial > 99:
                dial -= 100
                zeros_to_add += 1
        if dial == 0:
            zeros_to_add += 1
            if direction == "R":
                zeros_to_add -= 1
        print(f"Zeros to add {zeros_to_add}")

        zeros += zeros_to_add

    print(zeros)