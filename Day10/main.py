FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from itertools import groupby


def main():
    start_time = time.time()

    # data = parse_data()
    parse_time = time.time()

    answer1 = part1()
    part1_time = time.time()
    answer2 = part2()
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
    return


def part1():
    number = "1113222113"
    for _ in range(40):
        chunks = ["".join(group) for _, group in groupby(number)]
        number = ""
        for item in chunks:
            length = len(item)
            number += str(length) + item[0]

    return len(number)


def part2():
    number = "1113222113"
    for _ in range(50):
        chunks = ["".join(group) for _, group in groupby(number)]
        number = ""
        for item in chunks:
            length = len(item)
            number += str(length) + item[0]

    return len(number)

if __name__ == "__main__":
    main()