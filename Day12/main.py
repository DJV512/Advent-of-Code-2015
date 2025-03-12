# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import re
import json


def main():
    start_time = time.time()

    data = parse_data()
    parse_time = time.time()

    answer1 = part1(data)
    part1_time = time.time()
    answer2 = part2(data, answer1)
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

def sum_nums(input):
    return sum([int(x) for x in re.findall(r"-?\d+", str(input))])


def sum_red(input):
    if type(input) in (str, int):
        return 0
    if type(input) == list:
        return sum(sum_red(x) for x in input)
    if type(input) == dict:
        if "red" in input.values():
            return sum_nums(input)
        return sum_red(list(input.values()))


def part1(data):
    return sum_nums(data)


# I had a tough time with part 2. Part of the problem was that I didn't understand what was being asked.
# I didn't realize that "red" had to be a VALUE in the dictionary, not just in it at all.
# Ended up having to get some help from the reddit. Found this code from sqrtxander at 
# https://github.com/sqrtxander/adventofcode/blob/main/2015/day12/python/part2.py
# Thanks to him/her!
def part2(data, total):
    data = json.loads(data)
    red_sum = sum_red(data)
    return total - red_sum


if __name__ == "__main__":
    main()