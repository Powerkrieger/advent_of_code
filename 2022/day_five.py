def isin(string, array):
    for i in array:
        if i is string.strip():
            return True
    return False

def contains(a,b,x,y):
    if (a < x and b < x) or (x < a and y < a):
        return False
    if (a > y and b > y) or (x > b and y > b):
        return False
    if (a >= x and y >= b) or (x >= a and b >= y):
        return True
    return False

def not_contains(a,b,x,y):
    if (a < x and b < x) or (x < a and y < a):
        return True
    if (a > y and b > y) or (x > b and y > b):
        return True
    if a < x and b < y:
        return True
    if a > x and b > y:
        return True
    return False


def looong(a,b,x,y):
    ab = set([lol for lol in range(int(a),int(b)+1)])
    xy = set([lol for lol in range(int(x),int(y)+1)])
    lol = ab.intersection(xy)
    if len(lol) > 0:
        return True
    else:
        return False


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
