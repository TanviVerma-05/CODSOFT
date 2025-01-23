def to_do_list() :
    print("1. View tasks\n2. Add tasks\n3. Remove tasks\n4. mark task as complete\n5. exit")

def View_tasks():
    if not Tasks:
        print("Currently no tasks to do!")
    
    else:
        ln=len(Tasks)
        for i in range(ln):
            if St[i]==True:
                status="✔️"
            else:
                status="❌"    
            print(i+1,".",Tasks[i],"-->",status)
            
    
def Add_tasks():
    inp=input("enter the task to be added:").lower()
    Tasks.append(inp)
    St.append("False")
    print("Task added successfully!")
    
    
def Remove_task():
    Rtask=input("Enter the task u want to remove:").lower()
    ln=len(Tasks)
    if Rtask in Tasks:
        for i in range(ln):
            if Rtask==Tasks[i]:
                Tasks.remove(Rtask)
                key=St[i]
                St.pop(i)
                break
        print("Task removed successfully!")        
    else:
        print("Task entered does not exist!")        
            
def Mark_task_as_complt():
    task_num=int(input("enter the task number to be marked as done:"))
    if 0<task_num<=len(Tasks):
        St[task_num - 1]=True
    else:
        print("Invalid task number entered!") 
          
                 
    
    
    
to_do_list()
    
Tasks=[]
St=[]

while True:
    while True:
        try:
            # Prompt the user to enter choice
            ch = int(input("Enter your choice: "))
            break  # Exit the loop if a valid integer is entered
        except ValueError:
            print("Invalid input. Please enter a valid choice.")
    
    if ch==1:
        View_tasks()
        
    elif ch==2:
        Add_tasks()
    
    elif ch==3:
        Remove_task()
    
    elif ch==4:
        Mark_task_as_complt()
    
    elif ch==5:
        print("exiting the To-do list application!")
        break
    
    else:
        print("Invalid choice!")
