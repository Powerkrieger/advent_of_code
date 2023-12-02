def isin(string, array):
    for i in array:
        if i is string.strip():
            return True
    return False

with open("inputs/input_day_03.txt", "r+") as file1:
    sum = 0
    counter = 0
    part = [0]*3
    for line in file1:
        part[counter]=set(line.strip())
        counter += 1
        if counter < 3:
            continue
        else:
            counter = 0
            result = part[0].intersection(part[1], part[2])
            prio = ord(next(iter(result))) - 96

            if prio <=0:
                prio += 58

            sum += prio



    print(sum)
