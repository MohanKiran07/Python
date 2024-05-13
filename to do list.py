#tasks 
tasks=[] 

#add task
def add_task(task):
    tasks.append(task)
    print("Task Added")

#mark as complete 
def mrk_cmpt(index):
    if 0<= index < len(tasks):
        completed=tasks.pop(index)
        print(f"{index}.{completed} is marked as completed")
    else:
        print("Invalid task index")

#display
def display():
    if tasks:
        for index,task in enumerate(tasks,1):
            print(f"{index}.{task}")
    else:
        print("All tasks are completed")


#test cases
add_task("eat")

add_task("sleep")

add_task("code")

#Repeat😅

display()

mrk_cmpt(1)

display()
