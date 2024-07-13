task = input("Enter task:")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is task time bound? (yes or no):")

match priority:
    case 'high':
        reminder = f"The task '{task}' is of high priority"
    case 'medium':
        reminder = f"The task '{task}' is of medium priority"
    case 'low':
        reminder = f"The task '{task}' is of low priority"
    case _:
        print("Invalid priority. Please enter 'high', or 'low'.")
        exit()

if time_bound.lower() == 'yes':
    reminder += " It requires immediate attention today!."
    print(reminder)
    input("Press Enter to continue...")
    print("Task completed!")
