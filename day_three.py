def isin(string, array):
    for i in array:
        if i is string.strip():
            return True
    return False

with open("input_day_three.txt", "r+") as file1:
    sum = 0
    for line in file1:
        size = len(line.strip())//2
        part1 = set(line[0:size])
        part2 = set(line.strip()[size:])

        result = part1.intersection(part2)

        prio = ord(next(iter(result))) - 96

        if prio <=0:
            prio += 58

        sum += prio

    print(sum)
