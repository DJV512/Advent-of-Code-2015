# FILENAME = "sample_input.txt"
FILENAME = "input.txt"
# FILENAME = "sample2.txt"

import time
import utils
from collections import defaultdict
import heapq
import re


def main():
    start_time = time.time()

    molecule, replacements = parse_data()
    parse_time = time.time()

    answer1 = part1(molecule, replacements)
    part1_time = time.time()
    answer2 = part2(molecule, replacements)
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


def parse_data():
    with open(FILENAME, "r") as f:
        data = f.read()

    parts = data.split("\n\n")
    molecule = parts[1].strip()

    replacements = defaultdict(list)
    for line in parts[0].split("\n"):
        splits = line.strip().split(" => ")
        replacements[splits[0]].append(splits[1])

    return molecule, replacements


def part1(molecule, replacements):

    possibles = set()
    for to_be_replaced in replacements:
        for replacement in replacements[to_be_replaced]:
            matches = re.finditer(to_be_replaced, molecule)
            for match in matches:
                match_start = match.span()[0]
                match_end = match.span()[1]
                m1 = molecule[0:match_start]
                m2 = molecule[match_end:]
                new_molecule = m1+replacement+m2
                possibles.add(new_molecule)
    
    return len(possibles)


def part2(end_molecule, replacements):

    new_replacements = defaultdict(list)
    for key in replacements:
        for value in replacements[key]:
            new_replacements[value].append(key)

    pq = []

    heapq.heappush(pq, (len(end_molecule), 0, end_molecule))

    while pq:
        _, steps, current_molecule = heapq.heappop(pq)

        if current_molecule == "e":
            return steps
        
        for to_be_replaced in new_replacements:
            if to_be_replaced in current_molecule:
                for replacement in new_replacements[to_be_replaced]:
                    matches = re.finditer(to_be_replaced, current_molecule)
                    for match in matches:
                        match_start = match.span()[0]
                        match_end = match.span()[1]
                        m1 = current_molecule[0:match_start]
                        m2 = current_molecule[match_end:]
                        new_molecule = m1+replacement+m2
                        if "e" in new_molecule and len(new_molecule) != 1:
                            continue
                        else:
                            heapq.heappush(pq,(len(new_molecule), steps+1, new_molecule))

    return "Can't solve the problem"


if __name__ == "__main__":
    main()