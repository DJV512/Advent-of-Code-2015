# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import Counter


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

    return data


def part1(data):
    nice = 0
    for line in data:
        potential = False

        if "ab" in line or "cd" in line or "pq" in line or "xy" in line:
            continue

        count = Counter(line.strip())
        if count["a"] + count["e"] + count["i"] + count["o"] + count["u"] >= 3:
            potential=True
            
        if potential:
            for i in range(len(line.strip()) - 1):
                if line[i] == line[i+1]:
                    nice += 1
                    break

    return nice


def part2(data):
    nice = 0
    for line in data:
        potential = False

        for i in range(len(line.strip()) - 2):
            if line[i] == line[i+2]:
                 potential = True
        
        if potential:
            for i in range(len(line.strip()) - 2):
                string = line[i:i+2]
                if string in line[i+2:]:
                    nice += 1
                    break

    return nice


if __name__ == "__main__":
    main()