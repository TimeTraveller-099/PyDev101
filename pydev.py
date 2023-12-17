print("-------- Made by Raman Bhardwaj {CSE AIML - C} --------")

commands = '''
[ Commands ]
1 - Create a Task
2 - Edit a Task
3 - List All Tasks
4 - Delete a Task
5 - Exit
'''

def reIndexDict(dict, deletedKey):
    reIndexingKeyNumbers = []
    
    for key in dict.keys():
        if key > deletedKey:
            reIndexingKeyNumbers.append(key)
    
    # Deleting Previous Key-Value Pair & Inserting new Key-Value Pair with (Deleted Index - 1)
    for key in reIndexingKeyNumbers: 
        dict[key - 1] = dict.pop(key)

taskList = {}
indexTrack = 0

while True:
    print(commands)
    user = int(input("Enter Command Number: "))

    # Adding a New Task
    if user == 1:
        print("\n[ Adding New Task ]\n")
        newTask = input("(Adding Mode) Enter Task name: ")
        taskList[indexTrack + 1] = newTask
        indexTrack += 1
        print(f"[ A new task was created with a name '{newTask}' ]")
        print("\n", "-"*70)

    # Editing Task
    elif user == 2:
        print("\n[ Editing Task ]\n")
        taskNumber = int(input("(Editing Mode) Enter task number: "))
        newTaskName = input("(Editing Mode) Enter new task name: ")
        for i in taskList.keys():
            if taskNumber == i:
                taskList[taskNumber] = newTaskName

        print(f"\n[ Edited Task {taskNumber} to '{newTaskName}' ]")
        print("\n", "-"*70)

    # Printing ALL Tasks
    elif user == 3:
        print("\n[ All Tasks ]")
        for task in taskList:
            print(task, ")", taskList[task])
        print("\n", "-"*70)

    # Deleting a Task
    elif user == 4: 
        print("\n[ Deleting a Task ]\n")
        taskNumberDelete = int(input("(Deleting Mode) Enter Task Number to delete: "))
        print(f"[ Successfully Deleted Task {taskNumberDelete}: {taskList[taskNumberDelete]} ]")
        del taskList[taskNumberDelete]

        # Updating Indexes After Deletion
        reIndexDict(taskList, taskNumberDelete)
        print("-"*70)

    elif user == 5:
        print("\n[ Program Closed Successfully ]\n")
        input("Press Any Key to EXIT")
        break
    else:
        print("[ Enter a Valid Command ]")
        print("\n", "-"*70)
