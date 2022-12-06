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


with open("input_day_four.txt", "r+") as file1:


    counter = 0
    line_counter = 0
    for line in file1:
        line_counter += 1
        first, second = line.strip().split(",")
        a,b = first.split("-")
        x,y = second.split("-")

        print(a + " - " + b)
        print(x + " - " + y)
        #print(looong(a,b,x,y))

        if looong(a,b,x,y):
            counter += 1

    print(counter)
    print(line_counter)
