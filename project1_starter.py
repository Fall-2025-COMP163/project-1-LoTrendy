print("=======CHARACTER CREATION=======")
character_name = "ChrisT"
level = 1
xp = 0
print("Level: ", level)
print()
def character_create(character_name, level):
    print("Select your class: ")
    print()
    print("1. Warrior: Very Strong, Very Low Magic, and High Health. Special: TANK (Take no damage for a short duration) ")
    print("2. Mage: Very Weak, Large amounts of Offensive Magic, Medium Health. Special: BLITZ (Unlimited Mana for a short duration) ")
    print("3. Rogue: Medium Strength, Medium Magic, medium health. Special: FRENZY (50% Crit Chance on attacks for a short duration)")
    print("4. Cleric: Medium Strength, High Magic, High Health. Special: MR. Pots (Activates 3 random buffs for a short duration)")
    print()
    character_class = int(input("Choose a class for your character: "))
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
starter_stats = character_create({character_name}, 1)
print()
print(f"Your Character is", character_name, "the", starter_stats[0])
print()
print("Starter Stats: ")
print(f"Strength:", starter_stats[1])
print(f"Magic:", starter_stats[2])
print(f"Health:", starter_stats[3])
print(f"Gold:", starter_stats[4])
print(f"XP:", starter_stats[5])
print()
def xp_gain(character_name, amount):
    starter_stats[5] += amount
    print("You gained {amount} XP!")
    if starter_stats[5] >= 100:
        print("Congratulations, You gained 1 level")
        starter_stats[5] -= 100
        level += 1
        starter_stats[1] += 4
        starter_stats[2] += 3
        starter_stats[3] += 15
        starter_stats[4] += ( 35 * level)
        return starter_stats
def save_character(character_name, level, starter_stats):
    try:
        with open ("character_save1.txt","w") as f:
            f.write(f"Character Name: {character_name}\n")
            f.write(f"Class: {starter_stats[0]}\n")
            f.write(f"Level: {level}\n")
            f.write(f"Strength: {starter_stats[1]}\n")
            f.write(f"Magic: {starter_stats[2]}\n")
            f.write(f"Health: {starter_stats[3]}\n")
            f.write(f"Gold: {starter_stats[4]}\n")
            f.write(f"XP: {starter_stats[5]}\n")
        print("Character saved successfully!")
        return True
    except:
        print("Trouble With Save.")
        return False
save = save_character(character_name, level, starter_stats)
print()

def load_character(character_name):
    character_load = open("character_save1.txt","r")
    lines = character_load.readlines()
    character_load.close()
    return starter_stats
starter_stats = load_character(character_name)
print("Loaded Character")
print()
print(character_name)
print("level:", level)
print("Class:", starter_stats[0])
print("Strength:", starter_stats[1])
print("Magic:", starter_stats[2])
print("Health:", starter_stats[3])
print("Gold:", starter_stats[4])
print("XP:", starter_stats[5])
