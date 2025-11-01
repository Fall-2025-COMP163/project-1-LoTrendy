[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/JTXl4WMa)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21346433&assignment_repo_type=AssignmentRepo)
# COMP 163 - Project 1: Character Creator & Chronicles
# 🎯 Project Overview

Build a text-based RPG character creation and story progression system that demonstrates mastery of functions and file I/O operations.

# Required Functions 
Complete these functions in project1_starter.py:

create_character(name, character_class) - Create new character

calculate_stats(character_class, level) - Calculate character stats

save_character(character, filename) - Save character to file

load_character(filename) - Load character from file

display_character(character) - Display character info

level_up(character) - Increase character level

# 🎭 Character Classes
Implement these character classes with unique stat distributions:


Warrior: High strength, low magic, high health

Mage: Low strength, high magic, medium health

Rogue: Medium strength, medium magic, low health

Cleric: Medium strength, high magic, high health

# 📁 Required File Format
Your save_character() function must create files in this exact format:

Character Name: [name]

Class: [class]

Level: [level]

Strength: [strength]

Magic: [magic]

Health: [health]

Gold: [gold]


# Run specific test file
python -m pytest tests/test_character_creation.py -v

# Test your main program
python project1_starter.py

GitHub Testing:

After pushing your code, check the Actions tab to see automated test results:

✅ Green checkmarks = tests passed
❌ Red X's = tests failed (click to see details)

# ⚠️ Important Notes
Protected Files

DO NOT MODIFY files in the tests/ directory

DO NOT MODIFY files in the .github/ directory

Modifying protected files will result in automatic academic integrity violation

# AI Usage Policy

✅ Allowed: AI assistance for implementation, debugging, learning

📝 Required: Document AI usage in code comments

🎯 Must be able to explain: Every line of code during interview

# 📝 Submission Checklist

 All required functions implemented
 
 Code passes all automated tests
 
 README updated with your documentation
 
 Interview scheduled and completed
 
 AI usage documented in code comments

# 🏆 Grading

Implementation (70%): Function correctness, file operations, error handling

Interview (30%): Code explanation and live coding challenge


# MY PERSONAL DOCUMENTATION

# Game concept

My RPG world is built around a fantasy adventure where the player creates a neutral character, neither a hero or a villain who can be a Warrior, Mage, Rogue, or Cleric. As we code more I will work on allowing the character to make good choices or bad choices. Each class has unique stats that affect gameplay — Warriors are strong and durable, Mages are powerful spellcasters, Rogues are balanced and quick, and Clerics specialize in healing and support. The player gains XP through battles, levels up, and improves their abilities over time.

#Design 

I chose my stat formulas to make each class feel distinct:

Warrior: High strength and health for melee combat.

Mage: Low health but very high magic power.

Rogue: Balanced stats for flexibility.

Cleric: High magic and moderate health for support roles.

When a character levels up, they gain:

+4 Strength

+3 Magic

+15 Health
This gives a sense of steady progression without over-powering the player too quickly.

#Bonus/Unique Features

I added a “special ability” system, where each class gets a unique title or power name such as:

Warrior → "TANK"  (Take no damage for a short duration) ")

Mage → "BLITZ"  (Unlimited Mana for a short duration)

Rogue → "FRENZY"  (50% Crit Chance on attacks for a short duration)

Cleric → "MR. POTS"  (Activates 3 random buffs for a short duration)

# AI USAGE

I used ChatGPT (GPT-5) to help:

Clean/Debug functions for saving and loading. I had a lot of trouble with the save function because I gave the function the wrong name in the test cases causing it to fail over and over. 

Debug small issues like the calculate_stats tuple output. I also named a ot of the functions wrong if you check back at the first 

Improve documentation and commenting to make the code easier to understand. Just cleaned comments in the code to understand it better. Helped me learn it as I went.

All logic and design choices (stat formulas, class names, level-up rules) were decided by me.

# How to Run

Make sure your file is named ChrisT Project 1.py.

Open it in your Python IDE or text editor (no extra libraries needed).

Run the program.

The script automatically creates a character, levels it up, and saves it to a file called character_save1.txt.

The program then loads the saved character and displays the stats again.

No user input is required — it’s fully automated for testing.
