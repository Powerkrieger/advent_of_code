import re

with open("inputs/input_day_05.txt", "r+") as file1:
#with open("inputs/test_day_05.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    e = []
    f = []
    g = []

    puzzle = False
    for line in file1:
        if line == "\n":
            puzzle = True
            continue
        if not puzzle:
            e.append(line.replace("\n", ""))
        else:
            f.append(line)


for pattern in e:
    before, after = pattern.split("|")
    # make should not be patterns
    g.append(rf"{after}.*{before}")


for p in f:
    fail = False
    for pattern in g:
        if len(re.findall(pattern, p)) > 0:
            print("fail")
            fail = True
            break
    if not fail:
        x = p.split(",")
        c += int(x[len(x)//2])





print("solution")
print(c)
