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
    
    ingredients = {}
    for i, line in enumerate(data):
        parts = line.strip().split()
        ingredients[i] = (int(parts[2][:-1]), int(parts[4][:-1]), int(parts[6][:-1]), int(parts[8][:-1]), int(parts[10]))

    return ingredients


def part1(data):
    possibles = {}
    for a in range(0,101):
        for b in range(0,101):
            for c in range(0,101):
                for d in range(0,101):
                    if a + b + c + d == 100:
                        capacity = a * data[0][0] + b * data[1][0] + c * data[2][0] + d * data[3][0]
                        if capacity < 0:
                            capacity = 0
                        durability = a * data[0][1] + b * data[1][1] + c * data[2][1] + d * data[3][1]
                        if durability < 0:
                            durability = 0
                        flavor = a * data[0][2] + b * data[1][2] + c * data[2][2] + d * data[3][2]
                        if flavor < 0:
                            flavor = 0
                        texture = a * data[0][3] + b * data[1][3] + c * data[2][3] + d * data[3][3]
                        if texture < 0:
                            texture = 0
                        
                        score = capacity * durability * flavor * texture
                        if score > 0:
                            possibles[(a,b,c,d,capacity,durability,flavor,texture)] = score

    return max(possibles.values())


def part2(data):

    possibles = {}
    for a in range(0,101):
        for b in range(0,101):
            for c in range(0,101):
                for d in range(0,101):
                    if a + b + c + d == 100:
                        capacity = a * data[0][0] + b * data[1][0] + c * data[2][0] + d * data[3][0]
                        if capacity < 0:
                            capacity = 0
                        durability = a * data[0][1] + b * data[1][1] + c * data[2][1] + d * data[3][1]
                        if durability < 0:
                            durability = 0
                        flavor = a * data[0][2] + b * data[1][2] + c * data[2][2] + d * data[3][2]
                        if flavor < 0:
                            flavor = 0
                        texture = a * data[0][3] + b * data[1][3] + c * data[2][3] + d * data[3][3]
                        if texture < 0:
                            texture = 0
                        calories = a * data[0][4] + b * data[1][4] + c * data[2][4] + d * data[3][4]
                        
                        
                        score = capacity * durability * flavor * texture
                        if score > 0:
                            possibles[(a,b,c,d,capacity,durability,flavor,texture)] = (calories, score)

    possible_scores = []
    for possible in possibles:
        if possibles[possible][0] == 500:
            possible_scores.append(possibles[possible][1])


    return max(possible_scores)


if __name__ == "__main__":
    main()