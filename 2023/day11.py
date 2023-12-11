import copy
import time


def main():
    with open("inputs/input11.txt") as file:
        puzzle = file.readlines()
        answer = 0
        space = []
        galaxies = []
        factor = 1000000 - 1

        # read in space and expand in y direction
        rows_to_be_expanded = []
        for y, line in enumerate(puzzle):
            no_galaxies_flag = True
            for x, possible_galaxy in enumerate(line[:-1]):
                if possible_galaxy != ".":
                    no_galaxies_flag = False
                    galaxies.append([y, x])
            space.append(line[:-1])
            if no_galaxies_flag:
                print(f"{y} y expansion")
                rows_to_be_expanded.append((y, factor))

        # calculate expansion in x direction
        cols_to_be_expanded = []
        for x in range(len(space[0])):
            no_galaxies_flag = True
            for y in range(len(space)):
                if space[y][x] != ".":
                    no_galaxies_flag = False
            if no_galaxies_flag:
                print(f"{x} x expansion")
                cols_to_be_expanded.append((x, factor))

        # add expansion and galaxies
        new_galaxies = copy.deepcopy(galaxies)
        for (row, factor) in rows_to_be_expanded:
            for index in range(len(galaxies)):
                if galaxies[index][0] > row:
                    new_galaxies[index][0] += factor

        for (col, factor) in cols_to_be_expanded:
            for index in range(len(galaxies)):
                if galaxies[index][1] > col:
                    new_galaxies[index][1] += factor

        for galaxy in galaxies:
            print(galaxy)
        print("=========")
        for galaxy in new_galaxies:
            print(galaxy)

        # calculate galaxy distances
        num_galaxies = len(new_galaxies)
        for _ in range(num_galaxies):
            galaxy = new_galaxies.pop()
            for other_galaxy in new_galaxies:
                distance = abs(galaxy[0] - other_galaxy[0]) + abs(galaxy[1] - other_galaxy[1])
                answer += distance

        print(f"answer: {answer}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %.5s seconds ---" % (time.time() - start_time))
