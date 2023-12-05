import sys
import time

"""
had to add some whitespace at the end of the input .... dunno 
"""

def transfer_to_dest(source, val, dest):
    return dest + val - source


def dings_range(orig_ranges, df, i):

    new_ranges = []
    while df[i] != '\n' and df[i] is not None:
        dest, source, range_of = [int(x) for x in df[i][:-1].split(" ")]
        source = (source, source + range_of -1)
        # print(f"s_range {source}, {dest - source[0]}")
        old_ranges = []
        for o_range in orig_ranges:
            # print(f"o_range {o_range}")
            # no overlap , range before
            if o_range[1] < source[0]:
                old_ranges.append(o_range)
            # no overlap, range after
            elif o_range[0] > source[1]:
                old_ranges.append(o_range)
            # only overlap
            elif o_range[0] >= source[0] and o_range[1] <= source[1]:
                new_ranges.append(
                    (transfer_to_dest(source[0], o_range[0], dest), transfer_to_dest(source[0], o_range[1], dest)))
            # overlap both sides
            elif o_range[0] < source[0] and o_range[1] > source[1]:
                old_ranges.append((o_range[0], source[0] - 1))
                new_ranges.append((transfer_to_dest(source[0], source[0], dest), transfer_to_dest(source[0], source[1], dest)))
                old_ranges.append((source[1]+1, o_range[1]))
            # overlap front
            elif source[0] <= o_range[1] <= source[1]:
                old_ranges.append((o_range[0], source[0] - 1))
                new_ranges.append((transfer_to_dest(source[0], source[0], dest), transfer_to_dest(source[0], o_range[1], dest)))
            # overlap back
            elif source[0] <= o_range[0] <= source[1]:
                new_ranges.append((transfer_to_dest(source[0], o_range[0], dest), transfer_to_dest(source[0], source[1], dest)))
                old_ranges.append((source[1]+1, o_range[1]))
            else:
                print("dumbass")
                raise Exception
        i += 1
        orig_ranges = old_ranges
    for x in orig_ranges:
        new_ranges.append(x)
    i += 2
    return new_ranges, i


def main():
    with open("inputs/input05.txt") as file:
        df = file.readlines()
        answer = sys.maxsize
        line = df[0][7:-1]
        seeds = [int(seed) for seed in line.split(" ")]
        seed_ranges = []
        i = 1
        while i < len(seeds):
            seed_ranges.append((seeds[i - 1], seeds[i - 1] + seeds[i] - 1))
            i += 2

        for seed_range in seed_ranges:
            i = 3
            seed = [seed_range]
            print(f"seed range {seed}")
            soil, i = dings_range(seed, df, i)
            print(f"soil range {soil}")
            fertilizer, i = dings_range(soil, df, i)
            print(f"fertilizer range {fertilizer}")
            water, i = dings_range(fertilizer, df, i)
            print(f"water range {water}")
            light, i = dings_range(water, df, i)
            print(f"light range {light}")
            temperature, i = dings_range(light, df, i)
            print(f"temperature range {temperature}")
            humidity, i = dings_range(temperature, df, i)
            print(f"humidity range {humidity}")
            location, i = dings_range(humidity, df, i)
            print(f"location range {location}")
            for some_range in location:
                print(some_range)
                if some_range[0] < answer:
                    answer = some_range[0]
            print("-----------\n")
        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))
