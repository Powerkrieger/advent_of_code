with open("inputs/input_day_03.txt", "r+") as file1:
    result = 0
    for line in file1:
        bank = line.strip()
        print(f"bank: {bank}, length: {len(bank)}")
        # find the highest number from the left until one less than the end and then the highest number from that to the end.
        batteries = []
        max_pos = -1
        for each in range(11, -1, -1):

            max_pos += 1
            max_num = -1
            # find highest number until len(bank)-each so that each-1 numbers are left for the second highest
            for i in range(max_pos, len(bank)-each):
                if int(bank[i]) > max_num:
                    max_num = int(bank[i])
                    max_pos=i
                    if max_num >= 9:
                        break
            print(f"Max num: {max_num} at pos {max_pos}, max_pos+1: {max_pos+1}")
            batteries.append(max_num)

        # convert list of ints to one sequence of numbers and that sequence to one integer
        bank_res = int(''.join(map(str, batteries)))
        print(f"bank result: {bank_res}, batteries: {batteries}")
        result += bank_res

    print(result)