# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
Reminder = f"Reminder: '{task}' is a {priority} priority task"
if time_bound == "yes":
        print(f"{Reminder} that requires immediate attention today!")

    # Provide a customized reminder
match priority:
        case "high":
            if time_bound == "yes":
                print(Reminder)
            else:
                print(f"{Reminder}.")
        case "medium":
            if time_bound == "yes":
                print(Reminder)
            else:
                print(f"{Reminder}. Try to complete it soon.")
        case "low":
            if time_bound == "yes":
                print(Reminder)
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")