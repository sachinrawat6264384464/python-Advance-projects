import random
import time


while True:
    print("-----Dic Roll Semuletor------")
    
    print("1. If you want to play  the dic roll game  type 'yes'!")
    print("2. If you do not want to roll the dic type 'equet'!")
    choice=input("enter your choice here = ")
    if choice=="yes":
        print("-----roll the dic------")
        turn = True
        while True:
            
            print("")
            
            if turn==True:
                
                user=input("1. now is your turn type roll/quite= ").lower()
                if user=="roll": 
                    total_your=0
                    user1=random.randint(1,6)
                    total_your+=int(user1)
                    print("your number = ",user1)
                    turn=False
                elif user=="quite":
                    print("computer win this game beacause you quite the game")
                    break
                
            else: 
                    com=input("2,now is comp turn type roll/quite=").lower()
                    if com=="roll":
                      total_comp=0
                      comp=random.randint(1,6)
                      print("comp number  = ",comp)
                      print("")
                      total_comp+=comp
                      turn=True
                    elif user=="quite":
                      print("you win this game beacause comp quite the game")
                      break
                    time.sleep(10)
                    if total_comp==total_your:
                        print("--Match draw--")
                    elif total_your<total_comp:
                       print("🎆🎆🥳computer win this game!🎆🎆🥳 ")
                       print("this game is over")
                       
                    elif total_comp<total_your:
                       print("🎆🎆🥳computer win this game!🎆🎆🥳 ")
                       print("this game is over")
                       
                       