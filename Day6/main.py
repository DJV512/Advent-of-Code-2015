# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data)
    part2_time = time.time()

    print("---------------------------------------------------")
    print(f"Part 1 Answer: {answer1}")
    print()
    print(f"Part 2 Answer: {answer2}")
    print()
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time)} ms")
    print("---------------------------------------------------")


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    directions = []
    pattern = r"\d{1,3},\d{1,3}"
    for line in data:
        matches = re.findall(pattern, line.strip())
        one_one, one_two = matches[0].split(",")
        two_one, two_two = matches[1].split(",")
        if "on" in line:
            directions.append(("on", int(one_one), int(one_two), int(two_one), int(two_two)))
        elif "off" in line:
            directions.append(("off", int(one_one), int(one_two), int(two_one), int(two_two)))
        elif "toggle" in line:
            directions.append(("toggle", int(one_one), int(one_two), int(two_one), int(two_two)))
        else:
            raise TypeError("bad direction")

    return directions

def part1(data):

    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in data:
        direction, one_one, one_two, two_one, two_two = line

        for y in range(one_one, two_one + 1):
            for x in range(one_two, two_two + 1):
                if direction == "on":
                    lights[y][x] = 1
                elif direction == "off":
                    lights[y][x] = 0
                else:
                    if lights[y][x] == 1:
                        lights[y][x] = 0
                    else:
                         lights[y][x] = 1

    total_on = 0
    for y in range(1000):
        for x in range(1000):
            if lights[y][x] == 1:
                total_on += 1

    return total_on


def part2(data):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in data:
        direction, one_one, one_two, two_one, two_two = line

        for y in range(one_one, two_one + 1):
            for x in range(one_two, two_two + 1):
                if direction == "on":
                    lights[y][x] += 1
                elif direction == "off":
                    lights[y][x] -= 1
                    if lights[y][x] < 0:
                        lights[y][x] = 0
                else:
                    lights[y][x] += 2

    total_brightness = 0
    for y in range(1000):
        for x in range(1000):
            total_brightness += lights[y][x]

    return total_brightness


if __name__ == "__main__":
    main()