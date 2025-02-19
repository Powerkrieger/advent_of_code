with open("inputs/input_day_02.txt", "r+") as file1:
#with open("inputs/test_day_02.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = []
    e = []
    f = []

    for idx, line in enumerate(file1):
        levels_orig = [int(x) for x in line.split()]




        for lol in range(len(levels_orig)):
            unsafe = False
            levels = levels_orig[:]
            levels.pop(lol)
            print(levels)

            if levels[0] > levels[1]:
                print("decreasing")
                for i in range(len(levels) -1):
                    if levels[i] > levels[i+1] and levels[i] - levels[i+1] <= 3:
                        continue
                    else:
                        print("unsafe")
                        unsafe = True
                        break
                if not unsafe:
                    print("safe")
                    c += 1
                    d.append(idx)
                    break
            elif levels[1] > levels[0]:
                print("increasing")
                for i in range(len(levels) -1):
                    if levels[i] < levels[i+1] and levels[i+1] - levels[i] <= 3:
                        continue
                    else:
                        print("unsafe")
                        unsafe = True
                        break
                if not unsafe:
                    print("safe")
                    c += 1
                    d.append(idx)
                    break
            else:
                print("unsafe")
                continue

print(len(d))
print(c)
