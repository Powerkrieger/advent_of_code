stone = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]

def both(first, second):
    if isin(first, stone) and isin(second, stone):
        return True
    if isin(first, paper) and isin(second, paper):
        return True
    if isin(first, scissors) and isin(second, scissors):
        return True
    return False

def won(first, second):
    if isin(first, stone) and isin(second, scissors):
        return True
    if isin(first, paper) and isin(second, stone):
        return True
    if isin(first, scissors) and isin(second, paper):
        return True
    return False

def isin(string, array):
    for i in array:
        if i is string.strip():
            return True
    return False

with open("inputs/input_day_02.txt", "r+") as file1:

    score=0
    for line in file1:
        #print(line)
        opponent, me = line.split(" ")
        #print(a)
        #print(b)
        if isin(opponent, stone):
            if isin(me, stone):
                score+=3
            if isin(me, paper):
                score+=4
            if isin(me, scissors):
                score+=8
        elif isin(opponent, paper):
            if isin(me, stone):
                score+=1
            if isin(me, paper):
                score+=5
            if isin(me, scissors):
                score+=9
        elif isin(opponent, scissors):
            if isin(me, stone):
                score+=2
            if isin(me, paper):
                score+=6
            if isin(me, scissors):
                score+=7

    print(score)
