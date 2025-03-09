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
    
    presents = []
    for line in data:
        l, h, w = line.strip().split("x")
        presents.append((int(l),int(h),int(w)))

    return presents


def part1(data):

    paper = 0
    for l, h, w in data:
        side1 = 2*l*h
        side2 = 2*l*w
        side3 = 2*h*w
        this_paper = side1 + side2 + side3 + min(side1, side2, side3)/2
        paper += this_paper

    return paper


def part2(data):
    
    ribbon = 0
    for l, h, w in data:
        perim1 = 2*l+2*h
        perim2 = 2*l+2*w
        perim3 = 2*h+2*w
        this_ribbon = min(perim1, perim2, perim3) + l*h*w
        ribbon += this_ribbon

    return ribbon


if __name__ == "__main__":
    main()