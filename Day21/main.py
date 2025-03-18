import time
import utils
from itertools import combinations


Weapons = {
        "Dagger": {
            "Cost": 8,
            "Damage": 4
            },
        "Shortsword": {
            "Cost": 10,
            "Damage": 5
            },
        "Warhammer": {
            "Cost": 25,
            "Damage": 6
            },
        "Longsword": {
            "Cost": 40,
            "Damage": 7
            },
        "Greataxe": {
            "Cost": 74,
            "Damage": 8
            },
    }

Armors = {
    "Leather": {
        "Cost": 13,
        "Armor": 1,
        },
    "Chainmail": {
        "Cost": 31,
        "Armor": 2,
        }, 
    "Splintmail": {
        "Cost": 53,
        "Armor": 3,
        }, 
    "Bandedmail": {
        "Cost": 75,
        "Armor": 4,
        },
    "Platemail": {
        "Cost": 102,
        "Armor": 5,
        },
}

Rings = { 
    "Damage1": {
        "Cost": 25,
        "Damage": 1
    },
    "Damage2": {
        "Cost": 50,
        "Damage": 2
    },
    "Damage3": {
        "Cost": 100,
        "Damage": 3
    },
    "Defense1": {
        "Cost": 20,
        "Armor": 1
    },
    "Defense2": {
        "Cost": 40,
        "Armor": 2
    }, 
    "Defense3": {
        "Cost": 80,
        "Armor": 3
    },
}

weapon_combinations = list(combinations(Weapons.items(), 1))
armor_combinations = [()] + list(combinations(Armors.items(), 1))
ring_combinations_1 = list(combinations(Rings.items(), 1))
ring_combinations_2 = list(combinations(Rings.items(), 2))
all_ring_combos = [()] + ring_combinations_1 + ring_combinations_2

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


def simulate_game(Me):

    Boss = {
            "Hit_Points": 103,
            "Damage": 9,
            "Armor": 2,
        }
    
    keep_playing = True
    turn = 0
    while keep_playing:
        if turn == 0:
            total_damage = Me["Damage"]-Boss["Armor"]
            if total_damage < 1:
                total_damage = 1
            Boss["Hit_Points"] -= total_damage
            if Boss["Hit_Points"] <= 0:
                keep_playing = False
                winner = "ME"
            turn = 1
        else:
            total_damage = Boss["Damage"]-Me["Armor"]
            if total_damage < 1:
                total_damage = 1
            Me["Hit_Points"] -= total_damage
            if Me["Hit_Points"] <= 0:
                keep_playing = False
                winner = "BOSS"
            turn = 0
    
    return winner, (Me["Hit_Points"], Boss["Hit_Points"])



def part1():

    results = []
    for weapon in weapon_combinations:
        total_spent1 = weapon[0][1]["Cost"]
        total_damage1 = weapon[0][1]["Damage"]
        for armor in armor_combinations:
            total_armor1 = 0
            total_spent2 = total_spent1
            try:
                total_spent2 += armor[0][1]["Cost"]
                total_armor1 += armor[0][1]["Armor"]
            except (KeyError, IndexError):
                pass
            for ring in all_ring_combos:
                num_rings = len(ring)
                total_damage2 = total_damage1
                total_spent3 = total_spent2
                total_armor2 = total_armor1
                for i in range(num_rings):
                    total_spent3 += ring[i][1]["Cost"]
                    try:
                        total_damage2 += ring[i][1]["Damage"]
                    except (KeyError, IndexError):
                        pass
                    try:
                        total_armor2 += ring[i][1]["Armor"]
                    except (KeyError, IndexError):
                        pass

                Me = {
                    "Hit_Points": 100,
                    "Damage": total_damage2,
                    "Armor": total_armor2,
                }

                Me2 = {
                    "Hit_Points": 100,
                    "Damage": total_damage2,
                    "Armor": total_armor2,
                }

                winner, score = simulate_game(Me)
                if winner == "ME":
                    results.append((Me2, score, total_spent3))

    return min(results, key=lambda x: x[2])[2]


def part2():

    results = []
    for weapon in weapon_combinations:
        total_spent1 = weapon[0][1]["Cost"]
        total_damage1 = weapon[0][1]["Damage"]
        for armor in armor_combinations:
            total_armor1 = 0
            total_spent2 = total_spent1
            try:
                total_spent2 += armor[0][1]["Cost"]
                total_armor1 += armor[0][1]["Armor"]
            except (KeyError, IndexError):
                pass
            for ring in all_ring_combos:
                num_rings = len(ring)
                total_damage2 = total_damage1
                total_spent3 = total_spent2
                total_armor2 = total_armor1
                for i in range(num_rings):
                    total_spent3 += ring[i][1]["Cost"]
                    try:
                        total_damage2 += ring[i][1]["Damage"]
                    except (KeyError, IndexError):
                        pass
                    try:
                        total_armor2 += ring[i][1]["Armor"]
                    except (KeyError, IndexError):
                        pass

                Me = {
                    "Hit_Points": 100,
                    "Damage": total_damage2,
                    "Armor": total_armor2,
                }

                Me2 = {
                    "Hit_Points": 100,
                    "Damage": total_damage2,
                    "Armor": total_armor2,
                }

                winner, score = simulate_game(Me)
                if winner == "BOSS":
                    results.append((Me2, score, total_spent3))
            

    return max(results, key=lambda x: x[2])[2]


if __name__ == "__main__":
    main()