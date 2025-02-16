import random  #random for choice number 
import time    #time for give sleepS


while True:
    print("-----Dic Roll Semuletor------")
    
    #this is a instraction how you play
    print("1. If you want to play  the dic roll game  type and press enter button --> yes!")
    print("2. If you do not want to roll the dic type and press enter button -->exit!")
    choice=input("enter your choice here = ")
    
    #logice for play a game 
    if choice=="yes":
    
        print("-----roll the dic------")
        print("1. write 'roll' and press enter button for play")
        print("2. write 'quite' and press enter button for play")
        
        turn = True#this is a turm that when this is true user turn to roll the dice after this is become false and second turn of computer
        user_win=0   # how many times user win count
        com_win=0  #how many times computer win count
        
        
        while True: #we use while loop for play infinity when we do not want play the this break by the quite command
            
            print("")
            
            if turn==True: # this for when turn true  user turn to roll the dice 
                
                user=input("1. user turn write here for play = ").lower()
                if user=="roll": 
                    total_your=0
                    user1=random.randint(1,6)
                    total_your+=int(user1)
                    print("your number = ",user1)
                    turn=False    #after this value false 
                    
                elif user=="quite":  #
                    print(f"this is a time for result who win more rounds\n user win: {user_win}\n com_win: {com_win}")
                    break
                    
                else:
                    print("🔴write valide command! commands already given please read command")
                
                #this logice for computer turn
            else: 
                    com=input("2. computer turn write here for play computer can`t qiute the game =").lower()
                    if com=="roll":
                        total_comp=0
                        comp=random.randint(1,6)
                        print("comp number  = ",comp)
                        print("")
                        total_comp+=comp
                        turn=True
                    
                    time.sleep(10)
                    # this logice for who win and who lose the game
                    if total_comp==total_your:
                        print("--Match draw--")
                        
                    elif total_your<total_comp:                    # conditions for win computer
                        print("🎆🎆🥳computer win this game!🎆🎆🥳 ")
                        print("this game is over")
                        com_win+=1
                       
                    elif total_comp<total_your:       # condition for win user
                        print("🎆🎆🥳you win this game!🎆🎆🥳 ")
                        print("this game is over")
                        user_win+=1
                 
                    else:
                      print("🔴write valide command! commands already given please read command")
                      
    
    #he command for exite the game
    elif choice == "exit":
        print("✅✅exite successefully")
        break               
                       
