# File: daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Note: '{task}' is a medium priority task."
    case "low":
        message = f"Note: '{task}' is a low priority task."
    case _:
        message = f"Note: '{task}' has an unrecognized priority level."

# Time sensitivity adjustment
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."

# Display final reminder
print(message)
