# daily_reminder.py

# Prompt for task description
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ").lower()

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case on priority to customize reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unspecified priority"

# Modify reminder if task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"Note: {reminder}. Consider completing it when you have free time."

# Print the final reminder
print("\nReminder:", reminder)
