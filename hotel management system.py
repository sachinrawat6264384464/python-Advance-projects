# cafe management system using database mysql and python  module mysql.connector
import mysql.connector as mycon
mydb=mycon.connect(host="localhost", user="root", password="",database="cafe_management")
db_cursor=mydb.cursor()
"""
query="create database cafe_management"   # create database
query2="create table menu(item_name varchar(30), price int(10))"
query3="create table fast_food(item_name varchar(30), price int(10))"
query5="create table chapati(item_name varchar(30), price int(10))"
query5="create table drink_items(item_name varchar(30), price int(10))"
query4="insert into drink_items(item_name, price) values(%s,%s)"
values=("sprite",64)
db_cursor.execute(query4,values)
mydb.commit()
print("table created successfully")

"""
#system  start from here on
count=0
total=0
order_food=[]
while True:
    print("----welcome to foody cafe -----")
    print("1. call better for order food type ---> better")
    print("1. call better for bill type ---> bill")
      
    person=input("write  the call here = ").lower()
      
    if person=="better":
      
        while True:
            print()
            print("-----weldth of food---------")
            print("1.😋 light food enter---> 1")
            print("2.😋 heavy food enter---> 2")
            print("3.😋 chapati category enter---> 3")
            print("4.🍵🍻🍹🍺 drink catagary enter---> 4")
            print("5.💸💸 for exit and time of payment --> 5")
            food_choice=int(input("write your choice here = "))
            
            if food_choice==1:
            
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    
                    if choice==1:
                        query="select item_name,price from fast_food"
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found")
                    elif choice==2:
                        quentity =int(input("enter how much items you want to oredr ="))
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from fast_food where item_name= %s"
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                              
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break
            
            elif food_choice==2:
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    
                    if choice==1:
                        query="select item_name,price from menu"
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found") 
                    elif choice==2:
                        quentity =int(input("enter how much items you want to oredr ="))
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from menu where item_name= %s"
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break
            elif food_choice==3:
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    
                    if choice==1:
                        query="select item_name,price from chapati"
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found")
                    
                    elif choice==2:
                        food_name=input("write the name of your orders = ")
                        order_food.append(food_name)
                        query="select price from chapati where item_name= %s"
                        db_cursor.execute(query,(food_name,))
                        result=db_cursor.fetchone()
                        price=int(result[0])
                        quentity =int(input("enter quentity of chapati ="))
                        for _ in range(quentity):
                            total+=price
                        
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break    
            
            elif food_choice==4:
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    
                    if choice==1:
                        query="select item_name,price from drink_items"
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found") 
                    elif choice==2:
                        quentity =int(input("enter how much items you want to oredr ="))
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from drink_items where item_name= %s"
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break
            elif food_choice==5:
                break
            
            
            
            else:
               print("enter valide food choice! try again")
               
    elif person=="bill":
        print("💸💸Oreder food and total billings")
        index=1
        for i in order_food:
           print(f"{index}. {i}")
           print("---------------")
           index+=1
        print("total items: |",len(order_food))
        print("💸💸 total amount: |",total)
        print()
        break
                 
                  
                     
                