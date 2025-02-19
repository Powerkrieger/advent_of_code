with open("inputs/input_day_01.txt", "r+") as file1:
#with open("inputs/test1.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = []
    e = []
    f = []

    for line in file1:
        a, b = line.split("   ")
        print(a + " " + b)
        d.append(int(a))
        e.append(int(b))



    for x in d:
        f.append(x * e.count(x))

    print(f)

print(sum(f))

d.sort()
e.sort()
f = []
for x, y in zip(d, e):
    f.append(abs(x - y))


print(sum(f))