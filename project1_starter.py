#COMP 163 - Project 1: Character Creator & Saving/Loading
#Name: Christopher Taylor
#Date: 10/27/25
#I used ChatGPT to help me clean up def save_creator function/file to match the required format.
# COMP 163 - Project 1: Character Creator & Saving/Loading
# Name: Christopher Taylor
# Date: 10/27/25
# I used ChatGPT to help me clean up def save_character function/file to match the required format.

# --- PRESET CHARACTER VALUES (no input needed) ---
character_name = "ChrisT"
level = 1
xp = 0
character_class_choice = 2  # 1 = Warrior, 2 = Mage, 3 = Rogue, 4 = Cleric

print("Character Name:", character_name)
print("Level:", level)
print()

# === CHARACTER CREATION FUNCTION ===
def character_create(character_name, level, class_choice):
    print("Creating character with preset values...")
    print()

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
        print("Invalid choice! Defaulting to Rogue.")
        character_class = "Rogue"
        strength = 10
        magic = 10
        health = 75

    gold = 150
    xp = 0
    return [character_class, strength, magic, health, gold, xp]


# Create starter stats using preset values
starter_stats = character_create(character_name, level, character_class_choice)

# Display starter info
print(f"Your character is {character_name} the {starter_stats[0]}")
print()
print("Starter Stats:")
print(f"Strength: {starter_stats[1]}")
print(f"Magic: {starter_stats[2]}")
print(f"Health: {starter_stats[3]}")
print(f"Gold: {starter_stats[4]}")
print(f"XP: {starter_stats[5]}")
print()


# === XP GAIN FUNCTION ===
def xp_gain(amount):
    global level
    starter_stats[5] += amount
    print(f"You gained {amount} XP!")

    if starter_stats[5] >= 100:
        print("Congratulations, you gained 1 level!")
        starter_stats[5] -= 100
        level += 1
        starter_stats[1] += 4
        starter_stats[2] += 3
        starter_stats[3] += 15
        starter_stats[4] += (35 * level)
    return starter_stats


# === SAVE CHARACTER FUNCTION ===
def save_character(character_name, level, starter_stats):
    """
    Saves character data to a text file in the required format.
    Returns True if successful, False if an error occurs.
    """
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
        print("Character saved successfully!")
        return True
    except Exception as e:
        print("Trouble with save:", e)
        return False


# Save the character automatically
save_character(character_name, level, starter_stats)
print()


# === LOAD CHARACTER FUNCTION ===
def load_character():
    try:
        with open("character_save1.txt", "r") as f:
            lines = f.readlines()

        # Clean up the data and extract stats
        loaded_stats = {}
        for line in lines:
            key, value = line.strip().split(": ")
            loaded_stats[key] = value

        print("Character loaded successfully!")
        return loaded_stats
    except Exception as e:
        print("Error loading character:", e)
        return None


# Automatically load and print character
loaded_data = load_character()
print()
if loaded_data:
    print("Loaded Character:")
    for key, value in loaded_data.items():
        print(f"{key}: {value}")



"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: [Your Name Here]
Date: [Date]

AI Usage: [Document any AI assistance used]
Example: AI helped with file I/O error handling logic in save_character function
"""

# def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    # TODO: Implement this function
    # Remember to use calculate_stats() function for stat calculation
    pass

# def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level
    Returns: tuple of (strength, magic, health)
    
    Design your own formulas! Ideas:
    - Warriors: High strength, low magic, high health
    - Mages: Low strength, high magic, medium health  
    - Rogues: Medium strength, medium magic, low health
    - Clerics: Medium strength, high magic, high health
    """
    # TODO: Implement this function
    # Return a tuple: (strength, magic, health)
    pass

# def save_character(character, filename):
    """
    Saves character to text file in specific format
    Returns: True if successful, False if error occurred
    
    Required file format:
    Character Name: [name]
    Class: [class]
    Level: [level]
    Strength: [strength]
    Magic: [magic]
    Health: [health]
    Gold: [gold]
    """
    # TODO: Implement this function
    # Remember to handle file errors gracefully
    pass

# def load_character(filename):
    """
    Loads character from text file
    Returns: character dictionary if successful, None if file not found
    """
    # TODO: Implement this function
    # Remember to handle file not found errors
    pass

# def display_character(character):
    """
    Prints formatted character sheet
    Returns: None (prints to console)
    
    Example output:
    === CHARACTER SHEET ===
    Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """
    # TODO: Implement this function
    # pass

# def level_up(character):
    """
    Increases character level and recalculates stats
    Modifies the character dictionary directly
    Returns: None
    """
    # TODO: Implement this function
    # Remember to recalculate stats for the new level
    # pass

# Main program area (optional - for testing your functions)
# if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")
    
    # Example usage:
    # char = create_character("TestHero", "Warrior")
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
