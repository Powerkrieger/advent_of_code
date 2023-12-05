import sys


def dings(start, df, i):
    goal = start
    while df[i] != '\n' and df[i] is not None:
        dest, source, range_of = [int(x) for x in df[i][:-1].split(" ")]
        if source < start < (source + range_of):
            goal = dest + start - source
        i += 1
    i += 2
    return goal, i


if __name__ == "__main__":
    with open("inputs/input05.txt") as file:
        df = file.readlines()
        answer = sys.maxsize
        line = df[0][7:-1]
        seeds = [int(seed) for seed in line.split(" ")]

        for seed in seeds:
            i = 3
            print(seed)
            soil, i = dings(seed, df, i)
            print(soil)
            fertilizer, i = dings(soil, df, i)
            print(fertilizer)
            water, i = dings(fertilizer, df, i)
            print(water)
            light, i = dings(water, df, i)
            print(light)
            temperature, i = dings(light, df, i)
            print(temperature)
            humidity, i = dings(temperature, df, i)
            print(humidity)
            location, i = dings(humidity, df, i)
            print(location)
            if location < answer:
                answer = location
            print("-----------\n")
        print(f"answer: {answer}")
