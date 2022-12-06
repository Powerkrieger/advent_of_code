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

    sign_length = 14
    for i in range(len(buffer)-sign_length+1):

        sign = buffer[i:i+sign_length]

        if unique(sign, sign_length):
            print(i+sign_length)
