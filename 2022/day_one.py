with open("input.txt", "r+") as file1:
    max1 = 0
    max2 = 0
    max3 = 0
    max_elf = 0
    elf = 0
    a = 0
    for line in file1:
        if line.strip() != "":
            a += int(line)
        else:
            elf += 1
            if a > max1:
                if a > max2:
                    if a > max3:
                        max1 = max2
                        max2 = max3
                        max3 = a
                        max_elf = elf
                    else:
                        max1 = max2
                        max2 = a
                else:
                    max1 = a

            a = 0
    elf += 1
    if a > max1:
        if a > max2:
            if a > max3:
                max1 = max2
                max2 = max3
                max3 = a
                max_elf = elf
            else:
                max1 = max2
                max2 = a
        else:
            max1 = a
    a = 0

    print(max_elf)
    print(max3)
    print(max2)
    print(max1)
    print(max1+max2+max3)
