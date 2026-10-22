import json
import os

FILE_NAME = "tasks.json"


# Load saved tasks from JSON
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data

        return []

    except (json.JSONDecodeError, OSError):
        print("Could not load tasks. Starting with an empty list.")
        return []


# Save tasks into JSON
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()


# OPTION 1: ADD TASK
def add_task():
    task = input("Enter your study task: ").strip()

    if task == "":
        print("Task cannot be empty!")

    else:
        tasks.append([task, "Not completed"])
        save_tasks()
        print("Task added successfully!")


# OPTION 2: VIEW TASKS
def view_tasks():
    if len(tasks) == 0:
        print("No tasks added yet.")

    else:
        print("\n===== YOUR STUDY TASKS =====")

        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i][0], "-", tasks[i][1])


# OPTION 3: TAKE QUIZ
def take_quiz():
    print("\nChoose a subject:")
    print("1. Python")
    print("2. SQL")
    print("3. DSA")

    subject = input("Enter your choice: ")

    if subject == "1":
        subject_name = "Python"

        questions = [
            ["Which keyword defines a function in Python?",
             "a) function", "b) def", "c) fun", "b"],

            ["What is the data type of True?",
             "a) int", "b) str", "c) bool", "c"],

            ["Which symbol is used for Python comments?",
             "a) #", "b) //", "c) *", "a"]
        ]

    elif subject == "2":
        subject_name = "SQL"

        questions = [
            ["Which SQL command retrieves data?",
             "a) SELECT", "b) DELETE", "c) UPDATE", "a"],

            ["Which command adds a new record?",
             "a) DROP", "b) INSERT", "c) ALTER", "b"],

            ["Which clause filters records?",
             "a) ORDER BY", "b) GROUP BY", "c) WHERE", "c"]
        ]

    elif subject == "3":
        subject_name = "DSA"

        questions = [
            ["Which principle does a stack follow?",
             "a) FIFO", "b) LIFO", "c) Both", "b"],

            ["Which principle does a queue follow?",
             "a) FIFO", "b) LIFO", "c) Neither", "a"],

            ["Which search requires sorted data?",
             "a) Linear search", "b) Binary search", "c) Both", "b"]
        ]

    else:
        print("Invalid subject choice!")
        return

    score = 0

    print("\n=====", subject_name, "QUIZ =====")

    for question in questions:
        print("\n" + question[0])
        print(question[1])
        print(question[2])
        print(question[3])

        answer = input("Enter answer (a/b/c): ").strip().lower()

        if answer == question[4]:
            print("Correct!")
            score += 1

        else:
            print("Wrong! Correct answer:", question[4])

    print("\nQuiz completed!")
    print("Your score:", score, "/", len(questions))


# OPTION 4: COMPLETE TASK
def complete_task():
    if len(tasks) == 0:
        print("No tasks available.")
        return

    view_tasks()

    try:
        number = int(input("Enter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number!")

        elif tasks[number - 1][1] == "Completed":
            print("Task already completed!")

        else:
            tasks[number - 1][1] = "Completed"
            save_tasks()
            print("Task completed successfully!")

    except ValueError:
        print("Please enter a valid number!")


# OPTION 5: VIEW PROGRESS
def view_progress():
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task[1] == "Completed":
            completed += 1

    if total == 0:
        print("No tasks added yet.")

    else:
        percentage = (completed / total) * 100

        print("\n===== STUDY PROGRESS =====")
        print("Total tasks:", total)
        print("Completed tasks:", completed)
        print("Pending tasks:", total - completed)
        print("Progress:", round(percentage, 2), "%")


# MAIN MENU
while True:
    print("\n===== STUDENT STUDY ASSISTANT =====")
    print("1. Add Study Task")
    print("2. View Tasks")
    print("3. Take Quiz")
    print("4. Complete Task")
    print("5. View Progress")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        take_quiz()

    elif choice == "4":
        complete_task()

    elif choice == "5":
        view_progress()

    elif choice == "6":
        print("Thank you for using Student Study Assistant!")
        break

    else:
        print("Invalid choice! Please try again.")