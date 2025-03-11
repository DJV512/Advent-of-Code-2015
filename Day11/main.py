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
    print(f"Data Parse Execution Time: {1000*(parse_time - start_time)} ms")
    print(f"Part 1 Execution Time:     {1000*(part1_time - parse_time)} ms")
    print(f"Part 2 Execution Time:     {1000*(part2_time - part1_time)} ms")
    print(f"Total Execution Time:      {1000*(part2_time - start_time)} ms")
    print("---------------------------------------------------")


def parse_data():
    return


def part1():
    part1 = "hepxcrrq"
    part2 = "hepxxyzz"
    sample = "ghijklmn"

    not_allowed = [105, 108, 111]

    # number = [ord(x) for x in part1]
    number = [ord(x) for x in part2]
    # number = [ord(x) for x in sample]

    i = 0
    while True:
        skip = False
        potential = False
        more_potential = False
        i += 1
        number[-1] += 1
        if number[-1] > 122:
            number[-1] = 97
            number[-2] += 1
            if number[-2] > 122:
                number[-2] = 97
                number[-3] += 1
                if number[-3] > 122:
                    number[-3] = 97
                    number[-4] += 1
                    if number[-4] > 122:
                        number[-4] = 97
                        number[-5] += 1
                        if number[-5] > 122:
                            number[-5] = 97
                            number[-6] += 1
                            if number[-6] > 122:
                                number[-6] = 97
                                number[-7] += 1
                                if number[-7] > 122:
                                    number[-7] = 97
                                    number[-8] += 1
        
        if any(num in not_allowed for num in number):
            continue
        for i in range(6):
            if number[i+1] - number[i] == 1 and number[i+2]-number[i+1] == 1:
                potential = True
                break
        if potential:
            for i in range(7):
                if skip:
                    skip=False
                    more_potential = True
                    first_repeat = number[i]
                    continue
                if number[i] == number[i+1]:
                    skip = True
                    if more_potential and first_repeat != number[i]:
                        return "".join(map(chr, number))




def part2():
    # No need to write extra code for part 2. Just had to change the input
    # to part 1 to be the original part 1 answer to get the part 2 answer.
    return None


if __name__ == "__main__":
    main()