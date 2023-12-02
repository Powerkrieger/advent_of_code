if __name__ == "__main__":
    with open("input02.txt") as file:
        df = file.readlines()
        sum_ids = 0
        max_green, max_red, max_blue = 13, 12, 14
        for line in df:
            games = line.split(";")
            id, game1 = games[0].split(":")
            id = id.split(" ")[1]
            games[0] = game1

            skip = False
            green, red, blue = 0, 0, 0
            for game in games:
                cubes = game.split(",")
                for cube in cubes:
                    if "green" in cube:
                        _, new_green, _ = cube.split(" ")
                        if int(new_green) > green:
                            green = int(new_green)
                    if "red" in cube:
                        _, new_red, _ = cube.split(" ")
                        if int(new_red) > red:
                            red = int(new_red)
                    if "blue" in cube:
                        _, new_blue, _ = cube.split(" ")
                        if int(new_blue) > blue:
                            blue = int(new_blue)
                if green > max_green or red > max_red or blue > max_blue:
                    skip = True
                    break

            if not skip:
                sum_ids += int(id)

            # print(f"id: {id}, game1 {game1} should be included in games{games}")

        print(sum_ids)
