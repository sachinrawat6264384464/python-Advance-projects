# cafe management system using database mysql and python  module mysql.connector
import mysql.connector as mycon
mydb=mycon.connect(host="localhost", user="root", password="",database="cafe_management") # create a connect with database mysql
db_cursor=mydb.cursor()
#all query we use inthis project
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
#this is a starting point when we enter a hotel
    print("----welcome to foody cafe -----")
    print("1. call better for order food type ---> better")
    print("1. call better for bill type ---> bill")
      
    person=input("write  the call here = ").lower()
      
    if person=="better":
      
        while True:
            #this is a menu list with different items 
            print()
            print("-----weldth of food---------")
            print("1.😋 light food enter---> 1")
            print("2.😋 heavy food enter---> 2")
            print("3.😋 chapati category enter---> 3")
            print("4.🍵🍻🍹🍺 drink catagary enter---> 4")
            print("5.💸💸 for exit and time of payment --> 5")
            food_choice=int(input("write your choice here = "))# this is use for choice a items that you want to eat
            
            if food_choice==1:# choice 1 you are enter into light food items  and follow the command for order 
            
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    
                    if choice==1:   # choice 1 for display all items list withh price
                        query="select item_name,price from fast_food"  # query use for fetch items form database mysql
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found")
                            
                    # if you choice 2 now you can order the items        
                    elif choice==2:
                        quentity =int(input("enter how much items you want to order ="))  #this is for quentity of order
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from fast_food where item_name= %s"  #query for fetch data from database
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                              
                    elif choice==3: # this choice for conformed order
                       print("✅✅ your order conform successfully! injoy food!")
                       break
                       
                    else:# no item found show this
                       print("you try to choice invalide choice!🔴")
            
            elif food_choice==2:# choice 2 you are enter into heavy food items  and follow the command for order 
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    # choice 1 for display all items list withh price
                    if choice==1:
                        query="select item_name,price from menu"# query use for fetch items form database mysql
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        try:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        except FileExistsError:
                            print("no item found") 
                    # if you choice 2 now you can order the items 
                    elif choice==2:
                        quentity =int(input("enter how much items you want to order ="))#this is for quentity of orde
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from menu where item_name= %s" #query for fetch data from database
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                              
                    elif choice==3:# this choice for conformed order
                       print("✅✅ your order conform successfully! injoy food!")
                       break
                       
                    else:# no item found show this
                       print("you try to choice invalide choice!🔴")
            # choice 3 you are enter into chapati category items  and follow the command for order
            elif food_choice==3:
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    # choice 1 for display all items list withh price
                    if choice==1:
                        query="select item_name,price from chapati"# query use for fetch items form database mysql
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found")
                    # if you choice 2 now you can order the items
                    elif choice==2:
                        food_name=input("write the name of your orders = ")
                        order_food.append(food_name)
                        query="select price from chapati where item_name= %s"#query for fetch data from database
                        db_cursor.execute(query,(food_name,))
                        result=db_cursor.fetchone()
                        price=int(result[0])
                        quentity =int(input("enter quentity of chapati ="))
                        for _ in range(quentity):
                            total+=price
                    # this choice for conformed order
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break  
                       
                    else:# no item found show this
                       print("you try to choice invalide choice!🔴")
            # choice 4 you are enter into drink catagary enter items  and follow the command for order
            elif food_choice==4:
                while True:
                    print()
                    print("1.display all item enter--> 1")
                    print("2. for order enter --> 2")
                    print("3. for conform order enter --> 3")
                    choice=int(input("enter your choice here = "))
                    # choice 1 for display all items list withh price
                    if choice==1:
                        query="select item_name,price from drink_items"# query use for fetch items form database mysql
                        db_cursor.execute(query)
                        result=db_cursor.fetchall()
                        if result:
                            print("\n😋fast_food order now")
                            
                            for result in enumerate(result):
                               print(result ) 
                            print("--------items ends---------")
                        else:
                            print("no item found") 
                    # if you choice 2 now you can order the items
                    elif choice==2:
                        quentity =int(input("enter how much items you want to oredr ="))
                        for i in range(1,quentity+1):
                            food_name=input("write the name of your orders = ")
                            order_food.append(food_name)
                            
                            query="select price from drink_items where item_name= %s"#query for fetch data from database
                            db_cursor.execute(query,(food_name,))
                            result=db_cursor.fetchone()
                            for i in result:
                              total+=i
                    # this choice for conformed order
                    elif choice==3:
                       print("✅✅ your order conform successfully! injoy food!")
                       break
                       
                    else:# no item found show this
                       print("you try to choice invalide choice!🔴")
                       
            #this command for exite form the loop while and time for bill
            elif food_choice==5:
                break
            
            
            
            else:
               print("enter valide food choice! try again")
     #this is for the time of bill count all the items you order and with total payment          
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
                 
                  
                     
                
