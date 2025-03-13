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

    reindeer = {}
    for line in data:
        parts = line.strip().split()
        reindeer[parts[0]] = (int(parts[3]), int(parts[6]), int(parts[13]))

    return reindeer


def part1(data):

    Rudolph = True
    Dasher = True
    Dancer = True
    Comet = True
    Cupid = True
    Donner = True
    Prancer = True
    Vixen = True
    Blitzen = True
    Rudolph_dist = 0
    Dasher_dist = 0
    Dancer_dist = 0
    Comet_dist = 0
    Cupid_dist = 0
    Donner_dist = 0
    Prancer_dist = 0
    Vixen_dist = 0
    Blitzen_dist = 0
    Rudolph_pause = data["Rudolph"][2]
    Dasher_pause = data["Dasher"][2]
    Dancer_pause = data["Dancer"][2]
    Comet_pause = data["Comet"][2]
    Cupid_pause = data["Cupid"][2]
    Donner_pause = data["Donner"][2]
    Prancer_pause = data["Prancer"][2]
    Vixen_pause = data["Vixen"][2]
    Blitzen_pause = data["Blitzen"][2]
    Rudolph_go = data["Rudolph"][1]
    Dasher_go = data["Dasher"][1]
    Dancer_go = data["Dancer"][1]
    Comet_go = data["Comet"][1]
    Cupid_go = data["Cupid"][1]
    Donner_go = data["Donner"][1]
    Prancer_go = data["Prancer"][1]
    Vixen_go = data["Vixen"][1]
    Blitzen_go = data["Blitzen"][1]


    for _ in range(1,2504):
        if Rudolph:
            Rudolph_dist += data["Rudolph"][0]
            Rudolph_go -= 1
            if Rudolph_go == 0:
                Rudolph = False
                Rudolph_go = data["Rudolph"][1]
        else:
            Rudolph_pause -= 1
            if Rudolph_pause == 0:
                Rudolph = True
                Rudolph_pause = data["Rudolph"][2]

        if Dasher:
            Dasher_dist += data["Dasher"][0]
            Dasher_go -= 1
            if Dasher_go == 0:
                Dasher = False
                Dasher_go = data["Dasher"][1]
        else:
            Dasher_pause -= 1
            if Dasher_pause == 0:
                Dasher = True
                Dasher_pause = data["Dasher"][2]

        if Comet:
            Comet_dist += data["Comet"][0]
            Comet_go -= 1
            if Comet_go == 0:
                Comet = False
                Comet_go = data["Comet"][1]
        else:
            Comet_pause -= 1
            if Comet_pause == 0:
                Comet = True
                Comet_pause = data["Comet"][2]

        if Dancer:
            Dancer_dist += data["Dancer"][0]
            Dancer_go -= 1
            if Dancer_go == 0:
                Dancer = False
                Dancer_go = data["Dancer"][1]
        else:
            Dancer_pause -= 1
            if Dancer_pause == 0:
                Dancer = True
                Dancer_pause = data["Dancer"][2]

        if Cupid:
            Cupid_dist += data["Cupid"][0]
            Cupid_go -= 1
            if Cupid_go == 0:
                Cupid = False
                Cupid_go = data["Cupid"][1]
        else:
            Cupid_pause -= 1
            if Cupid_pause == 0:
                Cupid = True
                Cupid_pause = data["Cupid"][2]
        
        if Donner:
            Donner_dist += data["Donner"][0]
            Donner_go -= 1
            if Donner_go == 0:
                Donner = False
                Donner_go = data["Donner"][1]
        else:
            Donner_pause -= 1
            if Donner_pause == 0:
                Donner = True
                Donner_pause = data["Donner"][2]

        if Prancer:
            Prancer_dist += data["Prancer"][0]
            Prancer_go -= 1
            if Prancer_go == 0:
                Prancer = False
                Prancer_go = data["Prancer"][1]
        else:
            Prancer_pause -= 1
            if Prancer_pause == 0:
                Prancer = True
                Prancer_pause = data["Prancer"][2]

        if Vixen:
            Vixen_dist += data["Vixen"][0]
            Vixen_go -= 1
            if Vixen_go == 0:
                Vixen = False
                Vixen_go = data["Vixen"][1]
        else:
            Vixen_pause -= 1
            if Vixen_pause == 0:
                Vixen = True
                Vixen_pause = data["Vixen"][2]

        if Blitzen:
            Blitzen_dist += data["Blitzen"][0]
            Blitzen_go -= 1
            if Blitzen_go == 0:
                Blitzen = False
                Blitzen_go = data["Blitzen"][1]
        else:
            Blitzen_pause -= 1
            if Blitzen_pause == 0:
                Blitzen = True
                Blitzen_pause = data["Blitzen"][2]

    return max(Rudolph_dist, Dasher_dist, Comet_dist, Dancer_dist, Cupid_dist, Donner_dist, Prancer_dist, Vixen_dist, Blitzen_dist)


def part2(data):
    Rudolph = True
    Dasher = True
    Dancer = True
    Comet = True
    Cupid = True
    Donner = True
    Prancer = True
    Vixen = True
    Blitzen = True
    Rudolph_dist = 0
    Dasher_dist = 0
    Dancer_dist = 0
    Comet_dist = 0
    Cupid_dist = 0
    Donner_dist = 0
    Prancer_dist = 0
    Vixen_dist = 0
    Blitzen_dist = 0
    Rudolph_pause = data["Rudolph"][2]
    Dasher_pause = data["Dasher"][2]
    Dancer_pause = data["Dancer"][2]
    Comet_pause = data["Comet"][2]
    Cupid_pause = data["Cupid"][2]
    Donner_pause = data["Donner"][2]
    Prancer_pause = data["Prancer"][2]
    Vixen_pause = data["Vixen"][2]
    Blitzen_pause = data["Blitzen"][2]
    Rudolph_go = data["Rudolph"][1]
    Dasher_go = data["Dasher"][1]
    Dancer_go = data["Dancer"][1]
    Comet_go = data["Comet"][1]
    Cupid_go = data["Cupid"][1]
    Donner_go = data["Donner"][1]
    Prancer_go = data["Prancer"][1]
    Vixen_go = data["Vixen"][1]
    Blitzen_go = data["Blitzen"][1]

    scores = [0,0,0,0,0,0,0,0]

    for _ in range(1,2504):
        if Rudolph:
            Rudolph_dist += data["Rudolph"][0]
            Rudolph_go -= 1
            if Rudolph_go == 0:
                Rudolph = False
                Rudolph_go = data["Rudolph"][1]
        else:
            Rudolph_pause -= 1
            if Rudolph_pause == 0:
                Rudolph = True
                Rudolph_pause = data["Rudolph"][2]

        if Dasher:
            Dasher_dist += data["Dasher"][0]
            Dasher_go -= 1
            if Dasher_go == 0:
                Dasher = False
                Dasher_go = data["Dasher"][1]
        else:
            Dasher_pause -= 1
            if Dasher_pause == 0:
                Dasher = True
                Dasher_pause = data["Dasher"][2]

        if Comet:
            Comet_dist += data["Comet"][0]
            Comet_go -= 1
            if Comet_go == 0:
                Comet = False
                Comet_go = data["Comet"][1]
        else:
            Comet_pause -= 1
            if Comet_pause == 0:
                Comet = True
                Comet_pause = data["Comet"][2]

        if Dancer:
            Dancer_dist += data["Dancer"][0]
            Dancer_go -= 1
            if Dancer_go == 0:
                Dancer = False
                Dancer_go = data["Dancer"][1]
        else:
            Dancer_pause -= 1
            if Dancer_pause == 0:
                Dancer = True
                Dancer_pause = data["Dancer"][2]

        if Cupid:
            Cupid_dist += data["Cupid"][0]
            Cupid_go -= 1
            if Cupid_go == 0:
                Cupid = False
                Cupid_go = data["Cupid"][1]
        else:
            Cupid_pause -= 1
            if Cupid_pause == 0:
                Cupid = True
                Cupid_pause = data["Cupid"][2]
        
        if Donner:
            Donner_dist += data["Donner"][0]
            Donner_go -= 1
            if Donner_go == 0:
                Donner = False
                Donner_go = data["Donner"][1]
        else:
            Donner_pause -= 1
            if Donner_pause == 0:
                Donner = True
                Donner_pause = data["Donner"][2]

        if Prancer:
            Prancer_dist += data["Prancer"][0]
            Prancer_go -= 1
            if Prancer_go == 0:
                Prancer = False
                Prancer_go = data["Prancer"][1]
        else:
            Prancer_pause -= 1
            if Prancer_pause == 0:
                Prancer = True
                Prancer_pause = data["Prancer"][2]

        if Vixen:
            Vixen_dist += data["Vixen"][0]
            Vixen_go -= 1
            if Vixen_go == 0:
                Vixen = False
                Vixen_go = data["Vixen"][1]
        else:
            Vixen_pause -= 1
            if Vixen_pause == 0:
                Vixen = True
                Vixen_pause = data["Vixen"][2]

        if Blitzen:
            Blitzen_dist += data["Blitzen"][0]
            Blitzen_go -= 1
            if Blitzen_go == 0:
                Blitzen = False
                Blitzen_go = data["Blitzen"][1]
        else:
            Blitzen_pause -= 1
            if Blitzen_pause == 0:
                Blitzen = True
                Blitzen_pause = data["Blitzen"][2]
        
        current_distances = [Rudolph_dist, Dasher_dist, Comet_dist, Dancer_dist, Cupid_dist, Donner_dist, Prancer_dist, Vixen_dist, Blitzen_dist]
        leader = max(current_distances)
        index = current_distances.index(leader)

        scores[index] += 1

    return max(scores)


if __name__ == "__main__":
    main()