import random

list1=['s','p','r']
while(True):
    human_score=0
    computer_score=0
    for i in range(3):
        print("For stone= \'s\'\nFor Paper= \'p\'\nFor Scisor= \'r\'\n")
        print(50*"*")
        user_ip=input("Enter you choice here =   ")
        comp_ip=random.choice(list1)
        if(user_ip==comp_ip):
            print("it is tie\n")
        if(user_ip=='s' and comp_ip=='p'):
            computer_score+=1
            print("computer win this time\n")
        elif(comp_ip=='s' and user_ip=='p'):
            human_score+=1
            print("human win this time\n")
        if(user_ip=='r' and comp_ip=='p'):
            human_score+=1
            print("human win this time\n")
        elif(user_ip=='p' and comp_ip=='r'):
            computer_score+=1
            print("computer win this time\n")    
        if(user_ip=='s' and comp_ip=='r'):
            human_score+=1
            print("human win this time\n")
        elif(user_ip=='r' and comp_ip=='s'):
            computer_score+=1
            print("computer win this time\n")

    if(human_score==computer_score):
        print("it is a tie\n")
    elif(human_score>computer_score):
        print("human win \n")    
    else:
        print("computer win\n")
    print(50*"*")
    decision=input("if you want repeat this game then type and then enter yes  =   ")
    if(input=='yes'):
        break
