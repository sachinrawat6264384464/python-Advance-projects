import time
list1=[{"1.ques":"how is the prime minister  of india ","A":"matma gandhi","B":"narendra singh tomar","C":"yogi","D":"modi"},{"2.ques":"which fild releted to this softwere enginears","A":"IT","B":"mechanical","C":"civil","D":"hotel"}]
answer=["D","A"]
print("you have only 10 seconds time for every question!")

command=input("command type start = ").lower()
if command=="start":
 while True:
    price=10000
    index=0
    for i in list1,answer:
        print("--------welcome to conbanega cororpai----------")
        print(list1[index])
        print()
        user=input("choice your answer A,B,C,D = ").upper()
        if user==answer[index]:
           print(f"✅correct answer you win price = {price} ")
           
           price=price+20000
           index+=1
           time.sleep(10)
        else:
            print(" ❌you select a wrong answer")
    if index==2:
       break