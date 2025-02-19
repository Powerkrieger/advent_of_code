import re

with open("inputs/input_day_04.txt", "r+") as file1:
#with open("inputs/test_day_04.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    e = []
    f = []

    pattern1 = "XMAS"
    pattern2 = "SAMX"

    for line in file1:
        e.append(line.replace("\n", ""))


def diagonalOrderUP(array: list[str], n, m):
    ans = [[] for i in range(n+m -1)]
    for i in range(m):
        for j in range(n):
            ans[i+j].append(array[j][i])
    return ans


# from left
for l in e:
    c += len(re.findall(pattern1, l))
    c += len(re.findall(pattern2, l))

# from diagonal left -> up
diags = diagonalOrderUP(e, len(e), len(e[0]))
for l in diags:
    x = "".join(l)
    c += len(re.findall(pattern1, x))
    c += len(re.findall(pattern2, x))


# from up
ee = [[] for i in range(len(e[0]))]
for j in range(len(e)):
    for x, i in enumerate(reversed(range(len(e[0])))):
        ee[i].append(e[j][x])
for l in ee:
    x = "".join(l)
    c += len(re.findall(pattern1, x))
    c += len(re.findall(pattern2, x))


# from diagonal up -> right
diags = diagonalOrderUP(ee, len(ee), len(ee[0]))
for l in diags:
    x = "".join(l)
    c += len(re.findall(pattern1, x))
    c += len(re.findall(pattern2, x))




print("solution")
print(c)
