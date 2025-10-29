#%%
# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Christopher Taylor
# Date: 10/27/25
# I used ChatGPT to help me clean up def save_character function/file to match the required format.

# === CHARACTER CREATION FUNCTION ===
character_name = "ChrisT"
level = 1
class_choice = 3
def create_character(character_name, level, class_choice):
    if class_choice == 1:
        character_class = "Warrior"
        strength = 16
        magic = 3
        health = 110
    elif class_choice == 2:
        character_class = "Mage"
        strength = 4
        magic = 26
        health = 65
    elif class_choice == 3:
        character_class = "Rogue"
        strength = 10
        magic = 10
        health = 75
    elif class_choice == 4:
        character_class = "Cleric"
        strength = 8
        magic = 30
        health = 100
    else:
        character_class = "Rogue"
        strength = 10
        magic = 10
        health = 75

    gold = 150
    xp = 0
    return [character_class, strength, magic, health, gold, xp]

def calculate_stats(starter_stats, level, xp_gain_amount):
    starter_stats[5] += xp_gain_amount
    if starter_stats[5] >= 100:
        starter_stats[5] -= 100
        level += 1
        starter_stats[1] += 4
        starter_stats[2] += 3
        starter_stats[3] += 15
        starter_stats[4] += 35 * level
    return starter_stats, level

def save_character(character_name, level, starter_stats):
    try:
        with open("character_save1.txt", "w") as f:
            f.write(f"Character Name: {character_name}\n")
            f.write(f"Class: {starter_stats[0]}\n")
            f.write(f"Level: {level}\n")
            f.write(f"Strength: {starter_stats[1]}\n")
            f.write(f"Magic: {starter_stats[2]}\n")
            f.write(f"Health: {starter_stats[3]}\n")
            f.write(f"Gold: {starter_stats[4]}\n")
            f.write(f"XP: {starter_stats[5]}\n")
        return True
    except Exception:
        return False


def load_character():
    try:
        with open("character_save1.txt", "r") as f:
            lines = f.readlines()
        loaded_stats = {}
        for line in lines:
            key, value = line.strip().split(": ")
            loaded_stats[key] = value
        return loaded_stats
    except Exception:
        return None





starter_stats = character_create(character_name, level, class_choice)

save_success = save_character(character_name, level, starter_stats)

loaded_data = load_character()
