import random

print(  "1. rock\n 2. paper\n 3. scissor")

def rps():
    
    #TAKING USER CHOICE
    UI=int(input("ENTER YOUR CHOICE : "))
    if UI==1:
        print("USER choice is Rock")
    elif UI==2:
        print("USER choice is Paper")
    elif UI==3:
        print("USER choice is Scissor")
    else:
        print("INVALID CHOICE BY USER")
    
    #TAKING COMPUTER CHOICE
    CompS=random.randrange(1,4)
    if CompS==1:
        print("COMPUTER choice is Rock")
    elif CompS==2:
        print("COMPUTER choice is Paper")
    elif CompS==3:
        print("COMPUTER choice is Scissor")
    else:
        pass
    
    
    #NOW CHECKING FOR THE WIN LOSE OR TIE CONDITIONS
    if ((UI==1 and CompS==3) or (UI==3 and CompS==2) or (UI==2 and CompS==1)):
        print("YOU WON THE GAME")
       
    elif ((CompS==1 and UI==3) or (CompS==3 and UI==2) or (CompS==2 and UI==1)):
        print("YOU LOSE THE GAME")
       
    elif (UI==CompS):
        print("IT'S A TIE")
    
    else:
        pass
rps( )        
while True:
        
    ch=input("enter (Y) if u want to play again else enter (N) : ")
    if ch=='Y' or ch=='y':
        continue
    elif ch=='N' or ch=='n':
        break
    else:
        print("INVALID ENTRY")
