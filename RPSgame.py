import random
rock=1
paper=2
scissor=3

print(  "1.rock\n 2.paper\n 3.scissor")

def rps():
    
    while True:
        
        #TAKING USER CHOICE
        UI=input("ENTER YOUR CHOICE :(rock,  paper, scissor or 'quit' to exit)").lower( )
        if UI=='rock':
            print("USER choice is Rock")
        elif UI=='paper':
            print("USER choice is Paper")
        elif UI=='scissor':
            print("USER choice is Scissor")
        elif UI=='quit':
            print("Thanks for playing!")
            break
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
        if ((UI=='rock' and CompS==3) or (UI=='scissor' and CompS==2) or (UI=='paper' and CompS==1)):
            print("YOU WON THE GAME")
        elif ((CompS==1 and UI=='scissor') or (CompS==3 and UI=='paper') or (CompS==2 and UI=='scissor')):
            print("YOU LOSE THE GAME")
        elif((CompS==1 and UI=='rock') or (CompS==2 and UI=='paper') or (CompS==3 and UI=='scissor')):
            print("IT'S A TIE")
        else:
            pass

rps( )        
