def todo_list():
    tasks = []
    while True:
        task = input("Enter a task (or type 'done' to finish): ")
        if task.lower() == 'done':
            break
        tasks.append(task)
    print("Your To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

todo_list()