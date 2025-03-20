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
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time):.2f} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time):.2f} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time):.2f} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time):.2f} ms")
    print("---------------------------------------------------")


output = True  # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.readlines()

    instructions = []
    for line in data:
        parts = line.strip().split(" ")
        
        if "hlf" in line or "tpl" in line or "inc" in line:
            instructions.append((parts[0], parts[1]))
        elif "jmp" in line:
            if "+" in parts[1]:
                instructions.append((parts[0], int(parts[1][1:])))
            else:
                instructions.append((parts[0], int(parts[1])))
        elif "jie" in line:
            instructions.append((parts[0], parts[1][0:-1], int(parts[2][1:])))
        elif "jio" in line:
            instructions.append((parts[0], parts[1][0:-1], int(parts[2][1:])))
        else:
            raise ValueError("Unknown Instruction")
        
    return instructions


def part1(data):

    registers = {
        "a":0,
        "b":0,
    }

    num_instr = len(data)
    i = 0
    while i < num_instr:
        current = data[i]
        if "hlf" in current:
            registers[current[1]] //= 2
            i+=1
        elif "tpl" in current:
            registers[current[1]] *= 3
            i+=1
        elif "inc" in current:
            registers[current[1]] += 1
            i+=1
        elif "jmp" in current:
            i += current[1]
        elif "jie" in current:
            if registers[current[1]] % 2 == 0:
                i += current[2]
            else:
                i += 1
        elif "jio" in current:
            if registers[current[1]] == 1:
                i += current[2]
            else:
                i += 1

    return registers["b"]


def part2(data):

    registers = {
        "a":1,
        "b":0,
    }

    num_instr = len(data)
    i = 0
    while i < num_instr:
        current = data[i]
        if "hlf" in current:
            registers[current[1]] //= 2
            i+=1
        elif "tpl" in current:
            registers[current[1]] *= 3
            i+=1
        elif "inc" in current:
            registers[current[1]] += 1
            i+=1
        elif "jmp" in current:
            i += current[1]
        elif "jie" in current:
            if registers[current[1]] % 2 == 0:
                i += current[2]
            else:
                i += 1
        elif "jio" in current:
            if registers[current[1]] == 1:
                i += current[2]
            else:
                i += 1
    
    return registers["b"]


if __name__ == "__main__":
    main()