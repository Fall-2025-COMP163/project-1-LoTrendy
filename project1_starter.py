#%%
# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Christopher Taylor
# Date: 10/27/25
# I used ChatGPT to help me clean up def save_character function/file to match the required format.

# === CHARACTER CREATION FUNCTION ===
# ChrisT Project 1.py
# ChrisT Project 1.py
# ChrisT Project 1.py
# ChrisT Project 1.py
import os
lvl = 1

def create_character(name, character_class):
    """Creates a new character dictionary with base stats and special ability"""
    global lvl
    lvl = 1

    if character_class in ["Warrior", "Mage", "Rogue", "Cleric"]:
        stats = calculate_stats(character_class, lvl)
        special = assign_special(character_class)
    else:
        print("Invalid choice! Defaulting to Rogue.")
        character_class = "Rogue"
        stats = calculate_stats(character_class, lvl)
        special = assign_special(character_class)

    char_dict = {
        "name": name,
        "class": character_class,
        "level": lvl,
        "strength": stats[0],
        "magic": stats[1],
        "health": stats[2],
        "gold": 150,
        "xp": 0,
        "special": special
    }

    return char_dict


def calculate_stats(character_class, lvl):
    """Assigns base stats based on class"""
    if character_class == "Warrior":
        return 16, 3, 110
    elif character_class == "Mage":
        return 4, 26, 65
    elif character_class == "Rogue":
        return 10, 10, 75
    elif character_class == "Cleric":
        return 8, 30, 100
    else:
        return 10, 10, 75


def assign_special(character_class):
    """Assigns special ability name based on class"""
    if character_class == "Warrior":
        return "TANK"
    elif character_class == "Mage":
        return "BLITZ"
    elif character_class == "Rogue":
        return "FRENZY"
    elif character_class == "Cleric":
        return "MR. POTS"
    else:
        return "FRENZY"


def xp_gain(character, amount):
    """Adds XP and levels up if XP >= 100"""
    character["xp"] += amount
    print("You gained", amount, "XP!")

    if character["xp"] >= 100:
        print("Congratulations, you gained 1 level!")
        character["xp"] -= 100
        character["level"] += 1
        character["strength"] += 4
        character["magic"] += 3
        character["health"] += 15
        character["gold"] += (35 * character["level"])
    return character


def save_character(character, filename):
    """Saves character data to text file"""
    if "/" in filename:
        return False

    f = open(filename, "w")
    f.write("Character Name: " + character["name"] + "\n")
    f.write("Class: " + character["class"] + "\n")
    f.write("Level: " + str(character["level"]) + "\n")
    f.write("Strength: " + str(character["strength"]) + "\n")
    f.write("Magic: " + str(character["magic"]) + "\n")
    f.write("Health: " + str(character["health"]) + "\n")
    f.write("Gold: " + str(character["gold"]) + "\n")
    f.write("XP: " + str(character["xp"]) + "\n")
    f.write("Special: " + character["special"] + "\n")
    f.close()

    print("Character saved successfully!")
    return True


def load_character(filename):
    """Loads character from text file if it exists"""
    if os.path.isfile(filename):
        f = open(filename, "r")
        lines = f.readlines()
        f.close()

        char_dict = {
            "name": lines[0].split(":")[1].strip(),
            "class": lines[1].split(":")[1].strip(),
            "level": int(lines[2].split(":")[1].strip()),
            "strength": int(lines[3].split(":")[1].strip()),
            "magic": int(lines[4].split(":")[1].strip()),
            "health": int(lines[5].split(":")[1].strip()),
            "gold": int(lines[6].split(":")[1].strip()),
            "xp": int(lines[7].split(":")[1].strip()),
            "special": lines[8].split(":")[1].strip()
        }
        print("Character loaded successfully!")
        return char_dict
    else:
        print("Save file not found.")
        return None


def display_character(character):
    """Displays formatted character stats"""
    print("=== CHARACTER SHEET ===")
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Magic:", character["magic"])
    print("Health:", character["health"])
    print("Gold:", character["gold"])
    print("XP:", character["xp"])
    print("Special:", character["special"])
    print()
    return None


def level_up(character):
    """Manually level up the character"""
    global lvl
    lvl += 1
    character["level"] = lvl
    character["strength"] += 4
    character["magic"] += 3
    character["health"] += 15
    print(character["name"], "leveled up to Level", character["level"])
    return None


if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
