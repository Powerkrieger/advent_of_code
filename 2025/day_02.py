def is_invalid(number, number_of_chars):
    for i in range(1, number_of_chars):
        if len(str(number)) % i == 0:
            parts = [str(number)[j:j+i] for j in range(0, len(str(number)), i)]
            if all(str(part) == str(parts[0]) for part in parts):
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
                if is_invalid(i, len(str(i))):
                    print(f"Invalid number found: {i}")
                    result += i

    print(result)