#%%
# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Christopher Taylor
# Date: 10/27/25
# I used ChatGPT to help me clean up def save_character function/file to match the required format.

# === CHARACTER CREATION FUNCTION ===
print("=======CHARACTER CREATION=======")
character_name = "ChrisT"
level = 1
xp = 0
print()
print("Name:", character_name)
print("Level:", level)
print()

def character_create(character_name, level):
    print("Select your class: ")
    print()
    print("1. Warrior: Very Strong, Very Low Magic, and High Health. Special: TANK (Take no damage for a short duration) ")
    print("2. Mage: Very Weak, Large amounts of Offensive Magic, Medium Health. Special: BLITZ (Unlimited Mana for a short duration) ")
    print("3. Rogue: Medium Strength, Medium Magic, medium health. Special: FRENZY (50% Crit Chance on attacks for a short duration)")
    print("4. Cleric: Medium Strength, High Magic, High Health. Special: MR. Pots (Activates 3 random buffs for a short duration)")
    print()
    character_class = 3
    if character_class == 1:
        character_class = "Warrior"
        strength = 16
        magic = 3
        health = 110
    elif character_class == 2:
        character_class = "Mage"
        strength = 4
        magic = 26
        health = 65
    elif character_class == 3:
        character_class = "Rogue"
        strength = 10
        magic = 10
        health = 75
    elif character_class == 4:
        character_class = "Cleric"
        strength = 8
        magic = 30
        health = 100
    else:
        print("Invalid choice! Defaulting to Rogue.")
        character_class = "Rogue"
        strength = 10
        magic = 10
        health = 75
    gold = 150
    xp = 0
    return [character_class, strength, magic, health, gold, xp]

base_stats = character_create({character_name}, 1)
print()
print(f"Your Character is", character_name, "the", base_stats[0])
print()
print("Starter Stats: ")
print(f"Strength:", base_stats[1])
print(f"Magic:", base_stats[2])
print(f"Health:", base_stats[3])
print(f"Gold:", base_stats[4])
print(f"XP:", base_stats[5])
print()
def xp_gain(character_name, amount):
    base_stats[5] += amount
    print("You gained {amount} XP!")
    if base_stats[5] >= 100:
        print("Congratulations, You gained 1 level")
        base_stats[5] -= 100
        level += 1
        base_stats[1] += 4
        base_stats[2] += 3
        base_stats[3] += 15
        base_stats[4] += ( 35 * level)
        return starter_stats

def save_character(character_name, level, base_stats):
    file = open("character_save1.txt", "w")
    file.write("Character Name: " + character_name + "\n")
    file.write("Class: " + base_stats[0] + "\n")
    file.write("Level: " + str(level) + "\n")
    file.write("Strength: " + str(base_stats[1]) + "\n")
    file.write("Magic: " + str(base_stats[2]) + "\n")
    file.write("Health: " + str(base_stats[3]) + "\n")
    file.write("Gold: " + str(base_stats[4]) + "\n")
    file.write("XP: " + str(base_stats[5]) + "\n")
    file.close()
    print("Character saved successfully!")
   
    return True

save = save_character(character_name, level, base_stats)
print()

def load_character(character_name):
    character_load = open("character_save1.txt","r")
    lines = character_load.readlines()
    character_load.close()
    return base_stats

base_stats = load_character(character_name)
print("Loaded Character")
print()
print(character_name)
print("level:", level)
print("Class:", base_stats[0])
print("Strength:", base_stats[1])
print("Magic:", base_stats[2])
print("Health:", base_stats[3])
print("Gold:", base_stats[4])
print("XP:", base_stats[5])
print()

def display_character(base_stats):
    print("Character Display")
    print(character_name)
    print("level:", level)
    print("Class:", base_stats[0])
    print("Strength:", base_stats[1])
    print("Magic:", base_stats[2])
    print("Health:", base_stats[3])
    print("Gold:", base_stats[4])
    print("XP:", base_stats[5])
    return base_stats

display = display_character(base_stats)
print("Current Chacter and Stats")
print(display)
