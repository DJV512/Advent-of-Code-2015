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
        data = f.readlines()

    sues = {}
    for line in data:
        parts = line.strip().split()
        sues[parts[1][:-1]] = [(parts[2][:-1], int(parts[3][:-1])), (parts[4][:-1], int(parts[5][:-1])), (parts[6][:-1], int(parts[7]))]

    return sues


def part1(data):
    # No code needed. Good ol' Ctrl-F. However, I needed code for part 2, and since it's basically the same code,
    # I copied it up here and deleted the unnecessary conditions to spit out the right answer for part 1.
    
    goal = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    possible_sues = []
    for sue in data:
        possible = True
        for item, count in data[sue]:
            if possible:
                if goal[item] != count:
                    possible = False
            else:
                break
        if possible:
            possible_sues.append(sue)

    return possible_sues[0]


def part2(data):
    goal = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    possible_sues = []
    for sue in data:
        possible = True
        for item, count in data[sue]:
            if possible:
                if item == "trees" or item == "cats":
                    if goal[item] >= count:
                        possible = False
                        continue

                elif item == "pomeranians" or item == "goldfish":
                    if goal[item] <= count:
                        possible = False
                        continue
                
                else:
                    if goal[item] != count:
                        possible = False
                        continue

            else:
                break
        if possible:
            possible_sues.append(sue)

    return possible_sues[0]


if __name__ == "__main__":
    main()