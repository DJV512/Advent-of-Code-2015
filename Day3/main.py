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
        data = f.read()

    return data


def part1(data):

    visited = set()
    position = (0,0)
    visited.add(position)

    for char in data.strip():
        if char == ">":
            position = (position[0], position[1]+1)
            visited.add(position)
        elif char == "<":
            position = (position[0], position[1]-1)
            visited.add(position)
        elif char == "^":
            position = (position[0]-1, position[1])
            visited.add(position)
        elif char == "v":
            position = (position[0]+1, position[1])
            visited.add(position)

    return len(visited)


def part2(data):

    visited = set()
    santa_position = (0,0)
    robo_position = (0,0)
    visited.add(santa_position)

    for i, char in enumerate(data.strip()):
        if char == ">":
            if i % 2 == 0:
                santa_position = (santa_position[0], santa_position[1]+1)
                visited.add(santa_position)
            else:
                robo_position = (robo_position[0], robo_position[1]+1)
                visited.add(robo_position)
        elif char == "<":
            if i % 2 == 0:
                santa_position = (santa_position[0], santa_position[1]-1)
                visited.add(santa_position)
            else:
                robo_position = (robo_position[0], robo_position[1]-1)
                visited.add(robo_position)
        elif char == "^":
            if i % 2 == 0:
                santa_position = (santa_position[0]-1, santa_position[1])
                visited.add(santa_position)
            else:
                robo_position = (robo_position[0]-1, robo_position[1])
                visited.add(robo_position)
        elif char == "v":
            if i % 2 == 0:
                santa_position = (santa_position[0]+1, santa_position[1])
                visited.add(santa_position)
            else:
                robo_position = (robo_position[0]+1, robo_position[1])
                visited.add(robo_position)

    return len(visited)



if __name__ == "__main__":
    main()