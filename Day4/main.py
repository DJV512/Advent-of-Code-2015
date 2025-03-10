FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from hashlib import md5


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
    real = "iwrupvqb"

    i=0
    while True:
        i += 1
        start = real + str(i)
        hash = md5(start.encode()).hexdigest()
        if hash[0:5] == "00000":
            return i



def part2():
    real = "iwrupvqb"

    i=0
    while True:
        i += 1
        start = real + str(i)
        hash = md5(start.encode()).hexdigest()
        if hash[0:6] == "000000":
            return i


if __name__ == "__main__":
    main()