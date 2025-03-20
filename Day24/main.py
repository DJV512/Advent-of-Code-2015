# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from itertools import combinations
from copy import deepcopy
import math


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
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = False  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    return [int(line.strip()) for line in data]


def part1(data):

    total_sum = sum(data)
    weight = total_sum // 3
    qe = 10000000000000

    combo1 = (combo for combo in combinations(data, 6) if sum(combo)==weight)
    for group1 in combo1:
        qe1 = math.prod(group1)
        
        remaining_after_one = set(data) - set(group1)
        for j in range(6,10,2):
            combo2 = (combo for combo in combinations(remaining_after_one, j) if sum(combo)==weight)
            if combo2:
                for group2 in combo2:
                    qe2 = math.prod(group2)   
                    qe = min(qe, qe1, qe2)
            else:
                qe = min(qe, qe1)

    return qe


def part2(data):

    total_sum = sum(data)
    weight = total_sum // 4
    qe = 10000000000000

    combo1 = (combo for combo in combinations(data, 5) if sum(combo)==weight)
    for group1 in combo1:
        qe1 = math.prod(group1)
        
        remaining_after_one = set(data) - set(group1)
        for j in range(5,9,2):
            combo2 = (combo for combo in combinations(remaining_after_one, j) if sum(combo)==weight)
            if combo2:
                for group2 in combo2:
                    qe2 = math.prod(group2)   
                    qe = min(qe, qe1, qe2)
            else:
                qe = min(qe, qe1)

    return qe
  


if __name__ == "__main__":
    main()