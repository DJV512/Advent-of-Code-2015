## My original implementation in main2.py works, but is painfully
## slow. I wanted to try adding a set of "seen" states and check
## new additions to the heap before adding them to see if
## that would control the heap size and, thus, running time.

## This file does that, and wow did it work. CPython ran the original
## in 32 seconds, but now it's down to 0.3 seconds. pypy ran the original in
## 15 seconds, but the optimized version ran in 0.25 seconds, basically
## no different from CPython.

###### LESSON: Alawys track seen states!!!!!

import time
import utils
import heapq
from copy import deepcopy
from itertools import count

# Real input
Me = {
    "hp": 50,
    "armor": 0,
    "mana": 500
}

Boss = {
    "hp": 71,
    "damage": 10,
}

# Example input
# Me = {
#     "hp": 10,
#     "armor": 0,
#     "mana": 250
# }

# Boss = {
#     "hp": 14,
#     "damage": 8,
# }


Spells = {
    "m": {
        "cost": 53,
        "damage": 4,
        "heal": 0,
        "armor": 0,
        "add_mana": 0,
        "turns": 0,
    },
    "d": {
        "cost": 73,
        "damage": 2,
        "heal": 2,
        "armor": 0,
        "add_mana": 0,
        "turns": 0,
    },
    "s": {
        "cost": 113,
        "damage": 0,
        "heal": 0,
        "armor": 7,
        "add_mana": 0,
        "turns": 6,
    },
    "p": {
        "cost": 173,
        "damage": 3,
        "heal": 0,
        "armor": 0,
        "add_mana": 0,
        "turns": 6,
    },
    "r": {
        "cost": 229,
        "damage": 0,
        "heal": 0,
        "armor": 0,
        "add_mana": 101,
        "turns": 5,
    },
}


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


output = False # Toggle this flag to enable/disable prints
def debug_print(*args, **kwargs):
    if output:
        print(*args, **kwargs)


def part1(part2=False):

    counter = count()
    pq = []
    heapq.heappush(pq, (0, Boss["hp"], 0, [], 0, next(counter), {"s":0, "p":0, "r":0}, Me, Boss))

    # heapsize = 0

    seen = set()
    
    while pq:

        mana_spent, _, turn, move_list, num_turns, _, active_effects, prev_me, prev_boss = heapq.heappop(pq)

        # output = False
        # if turn == 0:
        #     debug_print(f"{utils.RED}Popped off the queue for player turn:{utils.RESET}")
        # else:
        #     debug_print(f"{utils.RED}Popped off the queue for boss turn:{utils.RESET}")
        # debug_print(f"{mana_spent=}, {boss_health=}, {turn=}, {move_list=}, {num_turns=}, {active_effects=}, {prev_me=}, {prev_boss=}")
        # debug_print()

        current_me = deepcopy(prev_me)
        current_boss = deepcopy(prev_boss)
        new_active_effects = deepcopy(active_effects)

        if new_active_effects["s"] != 0:
            new_active_effects["s"] -= 1
            if new_active_effects["s"] > 0:
                current_me["armor"] = 7
            else:
                current_me["armor"] = 0

        if new_active_effects["p"] != 0:
            current_boss["hp"] -= 3
            new_active_effects["p"] -= 1
                
        if new_active_effects["r"] != 0:
            current_me["mana"] += 101
            new_active_effects["r"] -= 1
                
        if current_boss["hp"] <= 0:
            # debug_print(f"{utils.YELLOW}THE PLAYER HAS WON! ADDED TO WIN LIST!{utils.RESET}")
            # print(f"{counter=}")
            # print(f"{heapsize=}")
            return mana_spent

        if turn == 0:

            if part2:
                current_me["hp"] -= 1
                if current_me["hp"] <= 0:
                    continue

            for spell in Spells:
                if spell == "s" and new_active_effects["s"] > 0:
                    # debug_print(f"{utils.BLUE}Can't use sheild when shield is already active.{utils.RESET}")
                    continue
                elif spell == "s":
                    new_current_me = deepcopy(current_me)
                    new_current_boss = deepcopy(current_boss)
                    new_move_list = deepcopy(move_list)
                    newer_active_effects = deepcopy(new_active_effects)
                    new_move_list.append(spell)
                    new_current_me["armor"] = Spells[spell]["armor"]
                    newer_active_effects["s"] = Spells[spell]["turns"]
                    new_current_me["mana"] -= Spells[spell]["cost"]
                    if new_current_me["mana"] > 0:
                        state = (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], new_current_me["hp"], newer_active_effects["p"], newer_active_effects["r"], newer_active_effects["s"], 1)
                        if state not in seen:
                            seen.add(state)
                            heapq.heappush(pq, (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], 1, new_move_list, num_turns+1, next(counter), newer_active_effects, new_current_me, new_current_boss))
                    #     debug_print(f"{utils.GREEN}Adding to the queue after player turn:{utils.RESET}")
                    #     debug_print(f"{mana_spent+Spells[spell]["cost"]=}, {new_current_boss["hp"]=}, turn=1, {new_move_list=}, {num_turns+1=}, {newer_active_effects=}, {new_current_me=}, {new_current_boss=}")
                    # else:
                    #     debug_print(f"{utils.MAGENTA}Using shield will drop the player below 0 mana. Do not add to queue.{utils.RESET}")

                if spell == "p" and new_active_effects["p"] > 0:
                    # debug_print(f"{utils.BLUE}Can't use poison when poison is already active.{utils.RESET}")
                    continue
                elif spell == "p":
                    new_current_me = deepcopy(current_me)
                    new_current_boss = deepcopy(current_boss)
                    new_move_list = deepcopy(move_list)
                    newer_active_effects = deepcopy(new_active_effects)
                    new_move_list.append(spell)
                    newer_active_effects["p"] = Spells[spell]["turns"]
                    new_current_me["mana"] -= Spells[spell]["cost"]
                    if new_current_me["mana"] > 0:
                        state = (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], new_current_me["hp"], newer_active_effects["p"], newer_active_effects["r"], newer_active_effects["s"], 1)
                        if state not in seen:
                            seen.add(state)
                            heapq.heappush(pq, (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], 1, new_move_list, num_turns+1, next(counter), newer_active_effects, new_current_me, new_current_boss))
                    #     debug_print(f"{utils.GREEN}Adding to the queue after player turn:{utils.RESET}")
                    #     debug_print(f"{mana_spent+Spells[spell]["cost"]=}, {new_current_boss["hp"]=}, turn=1, {new_move_list=}, {num_turns+1=}, {newer_active_effects=}, {new_current_me=}, {new_current_boss=}")
                    # else:
                    #     debug_print(f"{utils.MAGENTA}Using poison will drop the player below 0 mana. Do not add to queue.{utils.RESET}")

                if spell == "r" and new_active_effects["r"] > 0:
                    # debug_print(f"{utils.BLUE}Can't use recharge when recharge is already active.{utils.RESET}")
                    continue
                elif spell == "r":
                    new_current_me = deepcopy(current_me)
                    new_current_boss = deepcopy(current_boss)
                    new_move_list = deepcopy(move_list)
                    newer_active_effects = deepcopy(new_active_effects)
                    new_move_list.append(spell)
                    newer_active_effects["r"] = Spells[spell]["turns"]
                    new_current_me["mana"] -= Spells[spell]["cost"]
                    if new_current_me["mana"] > 0:
                        state = (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], new_current_me["hp"], newer_active_effects["p"], newer_active_effects["r"], newer_active_effects["s"], 1)
                        if state not in seen:
                            seen.add(state)
                            heapq.heappush(pq, (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], 1, new_move_list, num_turns+1, next(counter), newer_active_effects, new_current_me, new_current_boss))
                    #     debug_print(f"{utils.GREEN}Adding to the queue after player turn:{utils.RESET}")
                    #     debug_print(f"{mana_spent+Spells[spell]["cost"]=}, {new_current_boss["hp"]=}, turn=1, {new_move_list=}, {num_turns+1=}, {newer_active_effects=}, {new_current_me=}, {new_current_boss=}")
                    # else:
                    #     debug_print(f"{utils.MAGENTA}Using recharge will drop the player below 0 mana. Do not add to queue.{utils.RESET}")

                if spell == "m":
                    new_current_me = deepcopy(current_me)
                    new_current_boss = deepcopy(current_boss)
                    new_move_list = deepcopy(move_list)
                    newer_active_effects = deepcopy(new_active_effects)
                    new_move_list.append(spell)
                    new_current_boss["hp"] -= Spells[spell]["damage"]
                    new_current_me["mana"] -= Spells[spell]["cost"]
                    if new_current_boss["hp"] <= 0:
                        # debug_print(f"{utils.YELLOW}THE PLAYER HAS WON! ADDED TO WIN LIST!{utils.RESET}")
                        # print(f"{counter=}")
                        # print(f"{heapsize=}")
                        return mana_spent+Spells[spell]["cost"]
                    if new_current_me["mana"] > 0:
                        state = (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], new_current_me["hp"], newer_active_effects["p"], newer_active_effects["r"], newer_active_effects["s"], 1)
                        if state not in seen:
                            seen.add(state)
                            heapq.heappush(pq, (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], 1, new_move_list, num_turns+1, next(counter), new_active_effects, new_current_me, new_current_boss))
                    #     debug_print(f"{utils.GREEN}Adding to the queue after player turn:{utils.RESET}")
                    #     debug_print(f"{mana_spent+Spells[spell]["cost"]=}, {new_current_boss["hp"]=}, turn=1, {new_move_list=}, {num_turns+1=}, {new_active_effects=}, {new_current_me=}, {new_current_boss=}")
                    # else:
                    #     debug_print(f"{utils.MAGENTA}Using magic missile will drop the player below 0 mana. Do not add to queue.{utils.RESET}")
                
                if spell == "d":
                    new_current_me = deepcopy(current_me)
                    new_current_boss = deepcopy(current_boss)
                    new_move_list = deepcopy(move_list)
                    newer_active_effects = deepcopy(new_active_effects)
                    new_move_list.append(spell)
                    new_current_boss["hp"] -= Spells[spell]["damage"]
                    new_current_me["hp"] += Spells[spell]["heal"]
                    new_current_me["mana"] -= Spells[spell]["cost"]
                    if new_current_boss["hp"] <= 0:
                        # debug_print(f"{utils.YELLOW}THE PLAYER HAS WON! ADDED TO WIN LIST!{utils.RESET}")
                        # print(f"{counter=}")
                        # print(f"{heapsize=}")
                        return mana_spent+Spells[spell]["cost"]
                    if new_current_me["mana"] > 0:
                        state = (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], new_current_me["hp"], newer_active_effects["p"], newer_active_effects["r"], newer_active_effects["s"], 1)
                        if state not in seen:
                            seen.add(state)
                            heapq.heappush(pq, (mana_spent+Spells[spell]["cost"], new_current_boss["hp"], 1, new_move_list, num_turns+1, next(counter), new_active_effects, new_current_me, new_current_boss))
                    #     debug_print(f"{utils.GREEN}Adding to the queue after player turn:{utils.RESET}")
                    #     debug_print(f"{mana_spent+Spells[spell]["cost"]=}, {new_current_boss["hp"]=}, turn=1, {new_move_list=}, {num_turns+1=}, {new_active_effects=}, {new_current_me=}, {new_current_boss=}")
                    # else:
                    #     debug_print(f"{utils.MAGENTA}Using drain will drop the player below 0 mana. Do not add to queue.{utils.RESET}")

        else:
            total_damage = current_boss["damage"] - current_me["armor"]
            new_move_list = deepcopy(move_list)
            new_move_list.append("B")
            if total_damage < 1:
                total_damage = 1
            current_me["hp"] -= total_damage
            if current_me["hp"] > 0:
                state = (mana_spent, current_boss["hp"], current_me["hp"], new_active_effects["p"], new_active_effects["r"], new_active_effects["s"], 0)
                if state not in seen:
                    seen.add(state)
                    heapq.heappush(pq, (mana_spent, current_boss["hp"], 0, new_move_list, num_turns+1, next(counter), new_active_effects, current_me, current_boss))
            #     debug_print(f"{utils.GREEN}Adding to the queue after boss turn:{utils.RESET}")
            #     debug_print(f"{mana_spent}, {current_boss["hp"]=}, turn=0, {new_move_list=}, {num_turns+1=}, {new_active_effects=}, {current_me=}, {current_boss=}")
            # else:
            #     debug_print(f"{utils.CYAN}The player has been killed by the boss. Game over.{utils.RESET}")

        # if len(pq) > heapsize:
        #     heapsize = len(pq)

    return "Could not solve."        


def part2(): 
    return part1(part2=True)


if __name__ == "__main__":
    main()