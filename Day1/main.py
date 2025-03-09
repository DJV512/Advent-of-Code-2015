# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils


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
        data = f.read()

    return data


def part1(data):
    floor = 0
    for char in data.strip():
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor


def part2(data):
    floor = 0
    position = 0
    for char in data.strip():
        position += 1
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor < 0:
            return position


if __name__ == "__main__":
    main()