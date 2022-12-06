with open("input_day_five.txt", "r+") as file1:

    count_line = 0
    mat = [[] for _ in range(0, 9)]
    for line in file1:

        if count_line >=8:
            break

        n = 4
        four_chars = [(line[i:i+n]) for i in range(0, len(line), n)]
        for i, four_char in enumerate(four_chars):
            if len(four_char) > 2:
                mat[i].append(four_char[1])

        count_line += 1

    for stack in mat:
        stack.reverse()
        while stack[-1] == ' ':
            stack.pop()

    #for stack in mat:
    #    print(stack)

    for line in file1:
        if line.strip() == "":
            continue
        _, elements, _, from1, _, to1 = line.split(" ")
        changing = []
        for i in range(int(elements)):
            changing.append(mat[int(from1)-1].pop())
        changing.reverse()
        mat[int(to1)-1] = mat[int(to1)-1] + changing


    for stack in mat:
        print(stack)
