with open("inputs/input_day_03.txt", "r+") as file1:
    result = 0
    for line in file1:
        bank = line.strip()
        print(f"bank: {bank}, length: {len(bank)}")
        # find the highest number from the left until one less than the end and then the highest number from that to the end.
        max_num = -1
        max_pos = -1
        for i in range(len(bank)-1):
            if int(bank[i]) > max_num:
                max_num = int(bank[i])
                max_pos=i
                if max_num >= 9:
                    break
        print(f"Max num: {max_num} at pos {max_pos}, max_pos+1: {max_pos+1}")
        # keep i as starting point and find the highest number from there to the end
        max_second = -1
        for j in range(max_pos+1, len(bank)):
            print(f"Checking bank[{j}] = {bank[j]} against max_second {max_second}")
            if int(bank[j]) > max_second:
                max_second = int(bank[j])
                if max_second >= 9:
                    break
        print(f"Max num: {max_num}, Max second: {max_second}")
        bank_res = int(max_num) * 10 + int(max_second)
        print(bank_res)
        result += bank_res

    print(result)