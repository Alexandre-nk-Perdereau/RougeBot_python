import random

def roll_dice(num_dice, sides):
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    rolls.sort(reverse=True)
    return rolls

def hexa_roll(num_dice):
    successes = 0
    initial_rolls = roll_dice(num_dice, 6)
    all_rolls = [initial_rolls]
    successes += sum(1 for roll in initial_rolls if roll >= 3)

    # Relancer les dés qui ont fait 6
    new_rolls = [roll for roll in initial_rolls if roll == 6]
    while new_rolls:
        next_rolls = roll_dice(len(new_rolls), 6)
        all_rolls.append(next_rolls)
        successes += sum(1 for roll in next_rolls if roll >= 3)
        new_rolls = [roll for roll in next_rolls if roll == 6]

    return successes, all_rolls
