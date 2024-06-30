 # Prompt for a single task
'''task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Process the task based on priority and time sensitivity
reminder = f"Reminder: '{task}' is a {priority} priority task"
if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    # Provide a customized reminder
match priority:
        case "high":
            if time_bound == "yes":
                print(reminder)
            else:
                print(f"{reminder}.")
        case "medium":
            if time_bound == "yes":
                print(reminder)
            else:
                print(f"{reminder}. Try to complete it soon.")
        case "low":
            if time_bound == "yes":
                print(reminder)
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")'''


# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Provide a customized reminder
match priority:
        case "high":
            if time_bound == "yes":
             print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a {priority} priority task.")
        case "medium":
            if time_bound == "yes":
                print(f"Reminder: '{task}' is a {priority} priority task that requires attention today!")
            else:
                print(f"Reminder: '{task}' is a {priority} priority task. Try to complete it soon.")
        case "low":
            if time_bound == "yes":
               print(f"Reminder: '{task}' is a {priority} priority task, but it is time bound do it ")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority. Please enter high, medium, or low.")