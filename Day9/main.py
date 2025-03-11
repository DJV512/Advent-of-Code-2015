# FILENAME = "sample_input.txt"
FILENAME = "input.txt"

import time
import utils
import heapq
from copy import deepcopy


def main():
    start_time = time.time()

    routes, locations = parse_data()
    parse_time = time.time()

    answer1 = part1(routes, locations)
    part1_time = time.time()
    answer2 = part2(routes, locations)
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

    routes = {}
    locations = set()
    for line in data:
        left, distance = line.strip().split(" = ")
        dest1, dest2 = left.split(" to ")
        routes[(dest1, dest2)] = int(distance)
        routes[(dest2, dest1)] = int(distance)
        locations.add(dest1)
        locations.add(dest2)

    return routes, locations


def part1(routes, locations):
    total_locations = len(locations)
    pq = []
    for location1 in locations:
        for location2 in locations:
            if location1 != location2:
                heapq.heappush(pq, (routes[(location1, location2)], location2, [location1]))

    while pq:
        total_distance, end_location, path = heapq.heappop(pq)

        new_path = deepcopy(path)
        new_path.append(end_location)

        if len(new_path) == total_locations:
            return total_distance
    
        for location in locations:
            if location not in new_path:
                heapq.heappush(pq, (total_distance + routes[(end_location, location)], location, new_path))


def part2(routes, locations):
    total_locations = len(locations)
    pq = []
    for location1 in locations:
        for location2 in locations:
            if location1 != location2:
                heapq.heappush(pq, (-routes[(location1, location2)], location2, [location1]))

    possible_lengths = []

    while pq:
        total_distance, end_location, path = heapq.heappop(pq)

        new_path = deepcopy(path)
        new_path.append(end_location)

        if len(new_path) == total_locations:
            possible_lengths.append(total_distance)
            continue
    
        for location in locations:
            if location not in new_path:
                heapq.heappush(pq, (total_distance - routes[(end_location, location)], location, new_path))
    
    return -1*min(possible_lengths)


if __name__ == "__main__":
    main()