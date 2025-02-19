from collections import defaultdict

with open("inputs/input_day_07.txt", "r+") as file1:
#with open("inputs/test_day_07.txt", "r+") as file1:

    a = 0
    b = 0
    c = 0

    d = ""
    matrix = []
    e = []
    f = []
    g = []

    def flatten(l):
        return [x for xs in l for x in xs]

    for line in file1:
        possible_answers = defaultdict(list)
        answer, rest = line.split(":")
        numbers = rest.split()
        possible_answers[0] = [0]
        for i, n in enumerate(numbers, start=1):
            possible_answers[i] = flatten([[int(n)+x, int(n)*x, int(str(x) + n)] for x in possible_answers[i-1]])
        if int(answer) in possible_answers[i]:
            c += int(answer)



print("solution")
print(c)
