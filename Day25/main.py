FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils


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
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


def part1():

    target = (2980, 3074)

    start = 20151125
    multiplicand = 252533
    divisor = 33554393
    location = (0,0)
    last_y = 0

    while True:
        start = (start * multiplicand) % divisor
        if location[0] == 0:
            last_y += 1
            location = (last_y, 0)
        else:
            location = (location[0]-1, location[1]+1)
        
        if location == target:
            return start



def part2():
    return None


if __name__ == "__main__":
    main()