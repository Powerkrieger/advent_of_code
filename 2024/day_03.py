import re

with open("inputs/input_day_03.txt", "r+") as file1:
#with open("inputs/test_day_03.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    e = []
    f = []

    for line in file1:
        d += line



    do = True
    dont_matches = re.split("don't\(\)", d, 1)

    # dos
    do_list = dont_matches[0]
    matches = re.findall("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", do_list)
    print(matches)

    for m in matches:
        a,b = [int(x) for x in tuple(m)]
        print(a*b)
        c += a*b

    #find next do
    do_matches = re.split("do\(\)", dont_matches[1], 1)
    while len(do_matches) >= 2:
        rest = do_matches[1]
        dont_matches = re.split("don't\(\)", rest, 1)

        # dos
        do_list = dont_matches[0]
        matches = re.findall("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", do_list)
        print(matches)

        for m in matches:
            a, b = [int(x) for x in tuple(m)]
            print(a * b)
            c += a * b

        if len(dont_matches) >= 2:
            do_matches = re.split("do\(\)", dont_matches[1], 1)
        else:
            break
    # part 1
    # for line in file1:
    #     matches = re.findall("mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([1-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", line)
    #     for m in matches:
    #         a, b = [int(x) for x in tuple(m)]
    #         print(a * b)
    #         c += a * b


print("solution")
print(c)
