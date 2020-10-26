import random

list1=['s','p','r']
while(True):
    print("--------------------------------welcome-----------------------------")
    print("\n\nThis game is of 3 round those who win  2 round is the winner of the game")
    human_score=0
    computer_score=0
    i=0
    while(i<3):
        if i==2:
            if(human_score>computer_score):
                print("\nNo need of 3rd round bcoz human's score is obviously greater thean computer's.\n")
                break
            elif(human_score<computer_score):
                print("\nNo need of 3rd round bcoz computer's score is obviously greater thean human's.\n")
                break

        print("\n\nFor stone= \'s\'\nFor Paper= \'p\'\nFor Scissor= \'r\'\n")
        print(50*"*")
        while(True):
            user_ip=input("Enter you choice here =   ").lower()
            if(user_ip=='s' or user_ip=='p' or user_ip=='r'):
                break
            else:
                print("\nplease enter right choice")
        comp_ip=random.choice(list1)
        if(user_ip==comp_ip):
            print("\nIt is a tie, so it is not considered as a round.\n")
            print(f"\nComputre choice was = {comp_ip}")

        elif((user_ip=='s' and comp_ip=='p') or (user_ip=='p' and comp_ip=='r') or (user_ip=='r' and comp_ip=='s') ):
            computer_score+=1
            print("\nComputer win this round\n")
            print(f"\nComputre choice was = {comp_ip}\n")
            print(50*"+")
            i+=1
        elif((comp_ip=='s' and user_ip=='p') or (user_ip=='r' and comp_ip=='p') or (user_ip=='s' and comp_ip=='r')):
            human_score+=1
            print("\nHuman win this round\n")
            print(f"\nComputre choice was = {comp_ip}\n")
            print(50*"+")
            i+=1
    
        
        
    if(human_score==computer_score):
        print("\nIt is a tie\n")
    elif(human_score>computer_score):
        print("\nHuman is the winner of this game \n")    
    else:
        print("\nComputer is the winner of this game\n")
    print(50*"*")
    decision=input("If you want repeat this game then type and then enter \"yes\"  =   ")
    if(decision!='yes'):
        break
