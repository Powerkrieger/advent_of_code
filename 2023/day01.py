def starting_here(word, numbers):
    for i, number in enumerate(numbers):
        if word.startswith(number):
            return i
    return None


if __name__ == "__main__":
    with open("inputs/input01.txt") as file:
        df = file.readlines()

        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

        sum = 0
        for line in df:
            print(line)
            to_be_inserted = []
            for i in range(len(line)):
                word = line[i:]
                number = starting_here(word, numbers)
                if number is not None:
                    to_be_inserted.append((i, number))
            for count, (index, number) in enumerate(to_be_inserted, start=0):
                line = line[:index + count] + str(number) + line[index + count:]

            print(line)
            rev = line[::-1]

            for letter in line:
                if letter.isdigit():
                    a = int(letter)
                    break
            for letter in rev:
                if letter.isdigit():
                    b = int(letter)
                    break

            newdigit = a * 10 + b
            sum += newdigit

        print(sum)
