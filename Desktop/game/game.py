import random
''' 
1 for stone
-1 for paper
0 for scissors
'''
computer =random.choice ([-1,0,1])
youstr=input("Enter your choice: ")
youdict={"s":1,"p":-1,"sc":0}
reversedict={1:"stone",-1:"paper",0:"scissors"}
you =youdict[youstr]
print(f"You chose {reversedict[you]}\n Computer chose {reversedict[computer]}")
if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
         print("You loose")
         
    elif(computer==-1 and you==0):
         print("You win ")
    elif(computer==1 and you==-1):
        print("you win")       
    elif(computer==1 and you==0):
        print("You lose")
    elif(computer==0 and you==-1):
        print("You loose")
    elif(computer ==0 and you==1):
        print("You win")
    else:
        print("Something went wrong...")