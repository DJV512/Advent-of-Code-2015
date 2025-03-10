# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
from collections import deque

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

    directions = []
    for line in data:
        left, output  = line.strip().split(" -> ")

        if "NOT" in line:
            op, first = left.split()
            second = ""
        elif "AND" in line or "OR" in line or "RSHIFT" in line or "LSHIFT" in line:
            first, op, second = left.split()
        else:
            first = left
            second = ""
            op = "None"
        
        directions.append((op, first, second, output))

    return directions


def part1(data):
    wires = {}
    stack = deque(data)
    used = []

    while stack:
        op, first, second, output = stack.popleft()

        if (first.isdigit() or first in wires) and (second == "" or second.isdigit() or second in wires):

            if op == "None":
                if first.isdigit():
                    wires[output] = int(first)
                else:
                    wires[output] = wires[first]
            elif op == "AND":
                if first.isdigit():
                    wires[output] = int(first) & wires[second]
                else:
                    wires[output] = wires[first] & wires[second]
            elif op == "OR":
                wires[output] = wires[first] | wires[second]
            elif op == "RSHIFT":
                wires[output] = wires[first] >> int(second)
            elif op == "LSHIFT":
                wires[output] = wires[first] << int(second)
            elif op == "NOT":
                wires[output] = ~wires[first]
                if wires[output] < 0:
                    wires[output] += 65536
            
            used.append((op, first, second, output))
        
        else:
            stack.append((op, first, second, output))

        if "a" in wires:
            return wires["a"]


def part2(data):

    # No need to implement code. Just had to change the 4th line of the input to store
    # the answer to part 1 into wire b and rerun the part 1 code again to get the answer
    # to part 2.

    return None


if __name__ == "__main__":
    main()