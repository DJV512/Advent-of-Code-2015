FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
from itertools import combinations


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
    containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]
    
    total = 0
    for i in range(1, len(containers) + 1):
        for combo in combinations(containers, i):
            if sum(combo) == 150:
                total += 1
    
    return total


def part2():
    containers = [11, 30, 47, 31, 32, 36, 3, 1, 5, 3, 32, 36, 15, 11, 46, 26, 28, 1, 19, 3]

    total = 0
    for i in range(1, len(containers) + 1):
        done = False
        for combo in combinations(containers, i):
            if sum(combo) == 150:
                done = True
                total += 1
        if done:
            break

    return total

if __name__ == "__main__":
    main()