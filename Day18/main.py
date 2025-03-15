# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from copy import deepcopy


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

    return utils.grid_parse(data)


def part1(data):

    length = len(data)
    width = len(data[0])

    for _ in range(100):
        new_data = deepcopy(data)
        for y in range(length):
            for x in range(width):
                if data[y][x] == "#":
                    on = True
                else:
                    on = False
                neighbors_on = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if (a, b) != (0,0) and 0 <= y+a < length and 0 <= x+b < width:
                            if data[y+a][x+b] == "#":
                                neighbors_on +=1
                if on and neighbors_on in [2,3]:
                    new_data[y][x] = "#"
                elif on:
                    new_data[y][x] = "."
                elif not on and neighbors_on == 3:
                    new_data[y][x] = "#"
                elif not on:
                    new_data[y][x] = "."
        data = deepcopy(new_data)
    
    return sum(1 for y in range(length) for x in range(width) if data[y][x] == "#") 


def part2(data):
    length = len(data)
    width = len(data[0])

    data[0][0] = "#"
    data[0][width-1] = "#"
    data[length-1][0] = "#"
    data[length-1][width-1] = "#"

    for _ in range(100):
        new_data = deepcopy(data)
        for y in range(length):
            for x in range(width):
                if (y,x) in [(0,0), (0, width-1), (length-1, 0), (length-1, width-1)]:
                    continue
                if data[y][x] == "#":
                    on = True
                else:
                    on = False
                neighbors_on = 0
                for a in [-1, 0, 1]:
                    for b in [-1, 0, 1]:
                        if (a, b) != (0,0) and 0 <= y+a < length and 0 <= x+b < width:
                            if data[y+a][x+b] == "#":
                                neighbors_on +=1
                if on and neighbors_on in [2,3]:
                    new_data[y][x] = "#"
                elif on:
                    new_data[y][x] = "."
                elif not on and neighbors_on == 3:
                    new_data[y][x] = "#"
                elif not on:
                    new_data[y][x] = "."
        data = deepcopy(new_data)
    
    return sum(1 for y in range(length) for x in range(width) if data[y][x] == "#") 


if __name__ == "__main__":
    main()