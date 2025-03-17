FILENAME = "sample_input.txt"
#FILENAME = "input.txt"

import time
import utils
import math


def main():
    start_time = time.time()

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


def sum_divisors_part1(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)  
            divisors.add(n // i) 
    divisor_sum = sum(10*x for x in divisors)
    return divisor_sum


def sum_divisors_part2(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i) 
            divisors.add(n // i)
    divisor_sum = sum(11*x for x in divisors if x*50>=n)
    return divisor_sum

# Used this function to find a reasonable range of numbers to check
def find_smallest_number_with_divisors(target_divisors):
    primes = [2, 3, 5, 7, 11, 13, 17] 
    exponents = [1] * len(primes) 
    divisor_sum = 1

    while divisor_sum < target_divisors:
        number = 1
       
        for i in range(len(primes)):
            number *= primes[i] ** exponents[i]
        
        divisor_sum = sum_divisors_part1(number)
        
        min_exponent_index = exponents.index(min(exponents))
        exponents[min_exponent_index] += 1
          
    return number


def part1():
    target_divisor_sum = 29000000

    # smallest_number = find_smallest_number_with_divisors(target_divisor_sum)

    # Once I had a reasonable range, I used this brute force method,
    # continuously narrowing the range, until I found the right answer,
    # which is now the only number this processes
    possibles = []
    for i in range(665280, 665281):
        result = sum_divisors_part1(i)
        if result > target_divisor_sum:
            possibles.append((i, result))

    # for possible in possibles:
    #     print(possible)

    return possibles[0][0]


def part2():
    target_divisor_sum = 29000000

    # Based on the problem description it was likely that the part2 answer would
    # be higher than the part1 answer, so I just started playing with higher ranges
    # until I found the right answer.
    possibles = []
    for i in range(705600, 705601):
        result = sum_divisors_part2(i)
        if result > target_divisor_sum:
            possibles.append((i, result))

    # for possible in possibles:
    #     print(possible)

    return possibles[0][0]


if __name__ == "__main__":
    main()