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

    return data


def part1(data):
    hex_chars = "abcdefg0123456789"

    total_code = 0
    total_memory = 0

    for line in data:
        code_length = len(line.strip())
        memory_length = code_length - 2
        skip = False

        for i in range(code_length):
            if skip:
                skip = False
                continue
            if line[i] == "\\":
                if line[i+1] == "\\":
                    memory_length -= 1
                    skip = True
                elif line[i+1] == '"':
                    memory_length -= 1
                elif line[i+1] == "x":
                    if line[i+2] in hex_chars and line[i+3] in hex_chars:
                        memory_length -= 3
    
        total_code += code_length
        total_memory += memory_length

    difference = total_code - total_memory         

    return difference


def part2(data):

    total_code = 0
    total_memory = 0

    for line in data:
        code_length = len(line.strip())
        memory_length = code_length + 2

        for i in range(code_length):
            if line[i] == '\"':
                memory_length += 1
            elif line[i] == "\\":
                memory_length += 1
        
        total_code += code_length
        total_memory += memory_length

    difference = total_memory - total_code

    return difference


if __name__ == "__main__":
    main()