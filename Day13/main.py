# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import heapq
from copy import deepcopy


def main():
    start_time = time.time()

    happiness, people = parse_data()
    parse_time = time.time()

    answer1 = part1(happiness, people)
    part1_time = time.time()
    answer2 = part2(happiness, people)
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
    
    happiness = {}
    people = set()

    for line in data:
        parts = line.strip().split()
        people.add(parts[0])
        if "gain" in line:
            happiness[(parts[0], parts[-1][:-1])] = int(parts[3])
        elif "lose" in line:
            happiness[(parts[0], parts[-1][:-1])] = -int(parts[3])

    return happiness, people

def part1(happiness, people):
    pq = []
    possibles = []

    for person1 in people:
        for person2 in people:
            if person1 != person2:
                heapq.heappush(pq, (- happiness[(person1, person2)] - happiness[(person2, person1)], person2, [person1]))

    while pq:
        total_happiness, person, arrangement = heapq.heappop(pq)

        new_arrangement = deepcopy(arrangement)
        new_arrangement.append(person)

        if len(new_arrangement) == len(people):
            total_happiness -= happiness[(person, new_arrangement[0])] + happiness[new_arrangement[0], person]
            possibles.append(total_happiness)
            continue
        
        for new_person in people:
            if new_person not in new_arrangement:
                heapq.heappush(pq, (total_happiness - happiness[(person, new_person)] - happiness[(new_person, person)], new_person, new_arrangement))

    return min(possibles)


def part2(happiness, people):
    
    for person in people:
        happiness[(person, "Me")] = 0
        happiness[("Me", person)] = 0

    people.add("Me")

    pq = []
    possibles = []

    for person1 in people:
        for person2 in people:
            if person1 != person2:
                heapq.heappush(pq, (- happiness[(person1, person2)] - happiness[(person2, person1)], person2, [person1]))

    while pq:
        total_happiness, person, arrangement = heapq.heappop(pq)

        new_arrangement = deepcopy(arrangement)
        new_arrangement.append(person)

        if len(new_arrangement) == len(people):
            total_happiness -= happiness[(person, new_arrangement[0])] + happiness[new_arrangement[0], person]
            possibles.append(total_happiness)
            continue
        
        for new_person in people:
            if new_person not in new_arrangement:
                heapq.heappush(pq, (total_happiness - happiness[(person, new_person)] - happiness[(new_person, person)], new_person, new_arrangement))

    return min(possibles)


if __name__ == "__main__":
    main()