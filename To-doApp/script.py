def task():
    tasks = []
    print("---Welcome to Task Management App")

    total_task = int(input("Enter how many task you want to add = "))

    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)
    
    print(f"Today's tasks are \n {tasks}")

    while True:
        operation = int(input("Enter 1 to Add \n 2 to Update \n 3 to delete \n 4 to View \n 5 to Exit "))
        if operation == 1:
            add = input("Enter task you want to add ")
            tasks.append(add)
            print(f"The task {add} has been added")
        elif operation == 2:
            updated_value = input("enter the task name you want to update ")
            if updated_value in tasks:
                up = input("Enter the new task ")
                index = tasks.index(updated_value)
                tasks[index] = up
                print(f"Updated task {up}")
            else:
                print("Your task is not availble in task list")
        elif operation == 3:
            delete_value = input("enter the task name you want to delete ")
            if delete_value in tasks:
                index = tasks.index(delete_value)
                del tasks[index]
                print(f"Deleted task: {delete_value}")
            else:
                print("Your task is not availble in task list")
        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Closing the app")
            break

        else:
            print("Invalid input")


task()


