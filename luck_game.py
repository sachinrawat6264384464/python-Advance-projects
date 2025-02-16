#start the luck game this is a use full game for every one
import random
balance=50
while True:
    print("this is a new game  enjoy the game")
    print("welcome to lucky gameing!")
    print("1.do you want to play the game? ---> y/n")
    user=input("write your choice here = ").lower()
    if user=="y":
       while True:
        print("-------game start dependce on you-----")
        print("1.check your balance --> 1")
        print("2. for exite --->2")
        print("3.Diposit fill your wallet --> 3")
        print("4.for play enter amount --> 4")
        choice=int(input("enter the amonut = "))
        
        if choice==4:
            list1=["🍉","🔴","🎁"]
            list2=["🎁","🔴","🍉"]
            list3=["🔴","🎁","🍉"]
            role1=random.choice(list1)
            role2=random.choice(list3)
            role3=random.choice(list2)
            amount1=int(input("enter your waiting amount = "))
            if balance<amount1:
               print("🔴 warning:  amount is higher then balance diposit now! 💸💸 for big bets, please")
            elif role1==role2 and role1==role3:
                 print(f"{role1} | {role2} | {role3}\n")
                 win=amount1*2
                 print(f"🏆😏you win congratulations amount daouble = {win}")
                 balance=win
            
            elif role1==role2 and role1!=role3:
                print(f"{role1} | {role2} | {role3}\n")
                print(f"🧐you are very close to winning but you lose {amount1}")
                
                balance-=amount1
            elif role2==role3 and role2!=role1:
                print(f"{role1} | {role2} | {role3}\n")
                print(f"🛑you are very close to winning but you lose {amount1}")
                balance-=amount1
            elif role3==role2 and role3!=role1:
                print(f"{role1} | {role2} | {role3}\n")
                print(f"🚫you are very close to winning but you lose {amount1}")
                balanc=balance[0]-int(amount1)
                balance=balanc
            elif role3==role1 and role3!=role2:
                print(f"{role1} | {role2} | {role3}\n")
                print(f"🔴you are very close to winning but you lose {amount1}")
                balance-=amount1
            elif role3!=role1 and role3!=role2:
                print("🔴🛑🚫 you lose ")
                balance-=amount1
        elif choice==1:
            if balance<100:
               print("🚀🚀 wallet have not more money! diposit now = ",balance)
            else:print(f"💸💸wallet have enough money {balance} ")
        elif choice==2:
            print("🤞🤞 try you luck next time")
            break
        elif choice==3:
            user=int(input("enter diposit amount = "))
            balance+=user
            print("✅✅✅ diposit successfully ")
    elif user=="n":
        print(" 🚀🚀 byyy try your luck next time ")
        break
   
              
            
             
        
        