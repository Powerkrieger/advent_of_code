if __name__ == "__main__":
    with open("input01.txt") as file:
        df = file.readlines()

        sum = 0
        for line in df:
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
