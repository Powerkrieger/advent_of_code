def is_invalid(number):
    if len(str(number)) % 2 == 0:
        start = int(str(number)[len(str(number))//2:])
        end = int(str(number)[:len(str(number))//2])
        if start == end:
            return True
    return False

with open("inputs/input_day_02.txt", "r+") as file1:
    result = 0
    for line in file1:
        ranges = line.strip().split(",")
        for r in ranges:
            print(r)
            start, end = r.split("-")
            print(f"Start: {start}, End: {end}")
            for i in range(int(start), int(end)+1):
                if is_invalid(i):
                    print(f"Invalid number found: {i}")
                    result += i

    print(result)