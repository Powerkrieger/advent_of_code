import hashlib
import time
import array


def new_seq_check_zero(old_seq, hash_table):
    hash_of_seq = hashlib.md5(old_seq).hexdigest()
    if hash_of_seq in hash_table.keys():
       return hash_table[hash_of_seq]
    length = len(old_seq)
    new_seq = array.array('l')
    all_zeros = True
    for i in range(length - 1):
        new_seq.append(old_seq[i + 1] - old_seq[i])
        if new_seq[-1] != 0:
            all_zeros = False
    if all_zeros:
        return old_seq[-1]
    else:
        last_value_of_row_below = new_seq_check_zero(new_seq, hash_table)
        hash_table[hashlib.md5(new_seq).hexdigest()] = last_value_of_row_below
        return last_value_of_row_below + old_seq[-1]


def main():
    with open("../inputs/input09.txt") as file:
        puzzle = file.readlines()
        answer = 0
        look_up_last_value_by_hash = {}
        for line in puzzle:
            sequence = [int(x) for x in line[:-1].split(" ")]
            sequence = array.array('l', sequence)
            print(new_seq_check_zero(sequence, look_up_last_value_by_hash))
            answer += new_seq_check_zero(sequence, look_up_last_value_by_hash)

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
