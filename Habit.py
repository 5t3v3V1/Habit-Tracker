import json

def load_habits():
    habit_dictionary = {}

    try:
        with open("habits.json", "r", encoding="utf-8") as file:
            habit_dictionary = json.load(file)       
    
    except FileNotFoundError:
        pass

    return habit_dictionary

habit_dictionary = load_habits()

def save_habits(habit_dictionary, no_habits):
    with open("habits.json", "w", encoding="utf-8") as file:
        habit_json = json.dump(habit_dictionary, file, indent = no_habits)

def add_habit(habit_dictionary):
    habit = input("Habit: ")
    habit_dictionary[habit] = []
    return habit_dictionary
        
