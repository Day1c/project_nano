import os, time
from datetime import datetime

def return_main():
    times = 0
    os.system("clear")
    for x in range(4):
        times += 1
        print(f"Returning to \u001b[33m\u001b[1m2Day's Apps!\u001b[0m!\n\n{"." * times}")
        time.sleep(1)
        os.system('clear')

def get_time():
    format_time = datetime.now()
    return format_time.strftime('%Y-%m-%d'), format_time.strftime('%H:%M:%S')

def remove_empty():
    with open("/Users/dewan/School/project nano/goals_todo.txt", 'r') as df:
        lines = df.readlines()
    every_goal = []
    for line in lines:
        if line.strip() == "":
            continue
        every_goal.append(line)

    with open("/Users/dewan/School/project nano/goals_todo.txt", 'w') as fv:
        fv.writelines(every_goal)
    return every_goal

def new_goal():
    os.system("clear")
    date_made = get_time()[0]

    while True:
        new_goal = input("Enter your new goal (5-40 characters): ")
        os.system("clear")
        if "_" in new_goal or "-" in new_goal:
            print("\u001b[31mPlease dont use '-' or '_' in ur goal.\u001b[0m")
            continue
        if len(new_goal) < 5 or len(new_goal) > 40:
            print("\u001b[31mUr goal should be between 5 and 40 characters.\u001b[0m")
            continue
        break

    while True:
        due_date = input("Enter due date for this goal (YYYY/MM/DD) press enter for no due date: ")
        os.system("clear")
        if due_date.strip() == "":
            print("You did not want a due date for this goal!")
            due_date = "No due date"
            break
        else:
            if len(due_date) != 10:
                print("\u001b[31mYou did not give a valid date\u001b[0m\n")
                continue
            try:
                year,month,day = due_date.split("/")
                due_date = datetime(int(year), int(month), int(day)).date()
                break
            except ValueError:
                print("\u001b[31mYou did not give a valid date\u001b[0m")
    os.system("clear")
    with open("/Users/dewan/School/project nano/goals_todo.txt", "a") as df:
        df.write(f"\n{new_goal}_{due_date}_{date_made}")
    print(f"\u001b[32mGoal '{new_goal}' has been added!\n\u001b[0m")

def remove_goal(goals,due_dates, dates_made, every_goal):
    os.system("clear")
    while True:
        if not goals:
            return "nothing"
        print(f"""
                        Goals:                       |       Due:        |     Created:
    """+ "_" * 90 +"\n")
        for i in range(len(goals)):
            print(f"{i + 1:2}. {goals[i]:45} |    {due_dates[i]:15}|    {dates_made[i]}")
        remove_number =input("\nEnter the number you want to remove: ")
        os.system("clear")
        try:
            remove_number = int(remove_number)
            if remove_number < 1 or remove_number > len(goals):
                print("You didn't give a valid number from the list.")
            break
        except ValueError:
            print("\u001b[31mYou didn't give a valid answer.\u001b[0m")
            continue

    del every_goal [remove_number -1]
    with open("/Users/dewan/School/project nano/goals_todo.txt", "w") as df:
        df.writelines(every_goal)
    
    os.system("clear")
    print(f"\u001b[32mThe goal number '{remove_number}' has been removed!\n\u001b[0m")

def edit_goal(goals,due_dates, dates_made, every_goal):
    os.system("clear")
    while True:
        if not goals:
            return "nothing"
        print(f"""
                        Goals:                       |       Due:        |     Created:
    """+ "_" * 90 +"\n")
        for i in range(len(goals)):
            print(f"{i + 1:2}. {goals[i]:45} |    {due_dates[i]:15}|    {dates_made[i]}")
            edit_number =input("\nEnter the number of the goal you want to edit: ")
        try:
            edit_number = int(edit_number)
            if edit_number < 1 or edit_number > len(goals):
                print("You didn't give a valid number from the list.")
            break
        except ValueError:
            print("\u001b[31mYou didn't give a valid answer.\u001b[0m")
            continue
    while True:
        changed_goal = input(f"Enter what you want for goal {goals[edit_number-1]}(5-40 characters): ")
        os.system("clear")
        if "_" in changed_goal or "-" in changed_goal:
            print("\u001b[31mPlease dont use '-' or '_' in ur goal.\u001b[0m")
            continue
        if len(changed_goal) < 5 or len(changed_goal) > 40:
            print("\u001b[31mUr goal should be between 5 and 40 characters.\n\u001b[0m")
            continue
        break
        
    change = every_goal[edit_number -1].split("_")
    change[0] = changed_goal
    every_goal[edit_number-1] = "_".join(change)
    with open("/Users/dewan/School/project nano/goals_todo.txt", "w") as df:
        df.writelines(every_goal)
    print(f"\u001b[31mSuccessfully changed the goal {edit_number} to {change[0]}\u001b[0m")

def read_goal():
    with open ("/Users/dewan/School/project nano/goals_todo.txt") as df:
        lines = [line.strip()for line in df]
    goals = [line.split("_")[0] for line in lines]
    due_date = [line.split("_")[1] for line in lines]
    date_made = [line.split("_")[2] for line in lines]

    return goals,due_date, date_made

def main_todo():
    os.system("clear")
    while True:
        every_goal = remove_empty()
        goals = read_goal()[0]
        due_dates = read_goal()[1]
        dates_made = read_goal()[2]
        if not goals:
            print("There are no goals yet!")
        else:
            print(f"""{get_time()[0]} {get_time()[1]}
\u001b[36m  ______             __                         
 /_  __/___     ____/ /___     ____ _____  ____ 
  / / / __ \   / __  / __ \   / __ `/ __ \/ __ \\
 / / / /_/ /  / /_/ / /_/ /  / /_/ / /_/ / /_/ /
/_/  \____/   \__,_/\____/   \__,_/ .___/ .___/ 
                                 /_/   /_/      \u001b[0m
Welcome to the '\u001b[46mTo do app\u001b[0m'
These are all ur to do's:\n
|                      Goals:                       |       Due:        |     Created:     |
"""+ "_" * 91 +"\n")
            for i in range(len(goals)):
                print(f"| {i + 1:2}. {goals[i]:45} |    {due_dates[i]:15}|    {dates_made[i]}    |")
        print("_" * 91 +"""\n
(1) Add goal
(2) Remove goal
(3) Edit goal
""")
        action = input("What do you want to do (press q to quit)? ")
        os.system("clear")
        if action == "q":
            return_main()
            return
        try:
            action = int(action)
            if action == 1:
                new_goal()
            elif action == 2:
                result = remove_goal(goals,due_dates,dates_made, every_goal)
                if result == "nothing":
                    print("\u001b[31mThere are no goals to remove.\u001b[0m")
            elif action == 3:
                edit_goal(goals,due_dates, dates_made, every_goal)
            else:
                print("\u001b[31mPlease give a corresponding number.\u001b[0m")
        except ValueError:
            print("\u001b[31mThis was not a valid answer.\u001b[0m")
            continue
        
if __name__ == "__main__":
    main_todo()