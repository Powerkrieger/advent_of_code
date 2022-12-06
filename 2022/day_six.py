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

def unique(list1, sign_length):
    list_set = set(list1)
    unique_list = (list(list_set))
    if len(unique_list) >= sign_length:
        return True
    else:
        return False


with open("input_day_six.txt", "r+") as file1:

    buffer = []
    for line in file1:
        buffer.extend(line.strip())

    a = 0
    b = 0
    c = 0
    d = 0
    sign_length = 14
    for i in range(len(buffer)-sign_length+1):

        sign = buffer[i:i+sign_length]

        if unique(sign, sign_length):
            print(i+sign_length)
