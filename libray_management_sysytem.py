import mysql.connector as myconn
import bcrypt
from datetime import date
import sqlite3

# Connect to the database
mydb = myconn.connect(host="localhost", user="root", password="", database="library_system")
db_cursor = mydb.cursor()

while True: 
    print("\nWelcome to the Library System")
    print("1.🔓 Teachers login Type --> t_login")
    print("2.🔓 Student login Type --> s_login")
    print("3.🔓 Admin login Type --> admin")
    print("4.🚀 Logout Type --> exit")

    command = input(" ⌘ Type command: ").lower() 
    
    
    
#teacher login command
    if command == "t_login":
        print("--------page🙋2nd------------")
        print("\n👤➡️🔒 verifing authority of teacher\n")
        #this is a Authentication section for teacher
        class signup:
            def __init__(self, name, password):
                #salt=bcrypt.gensalt()
                #hashed_password=bcrypt.hashpw(password.encode("utf-8"),salt)
                #🔗🗄️this is a database connection name and password fetch from database with sql queries
                query = "select * from teacher_info where name=%s and password=%s"
                values = (name, password)
                db_cursor.execute(query, values)
                result=db_cursor.fetchone()
                if result: # 🔗🗄️Save changes to the database
                   print(f"\n✅ login successful! welcom, {name}\n")
                   while True:
                   #command lines follow and injoy 
                        print("")
                        print("1.show all books type -->'show'!")
                        print("2. borrow normal berzon books --> 'normanl'!")
                        print("3. borrow advance books --> 'advance'!")
                        print("4. return books all type here type --> 'return'!")
                        print("5. show time lines for retunr and 💸🤑charges type --> 'display'!")
                        print("6. for log out type write --> 'exit'!")
                        command=input("write command  here = ").lower()
                        if command=="show":
                            query="select name,code,date from book_info"
                            db_cursor.execute(query)
                            result=db_cursor.fetchall()
                            print("📖🔍all books are available\n",result)
                            
                        elif command=="normal":   #borrow books for study and use mysql database   connection
                            def borrow(code):
                            
                                Date=date.today()
                                query="select name,code from book_info where code=%s"
                                db_cursor.execute(query,(code,))
                                result=db_cursor.fetchone()
                                if result:
                                    book_code=result[1]
                                    query="insert into T_borrow_books(teacher_name,book_code,date) values(%s,%s,%s)"
                                    values=(name,book_code,Date.strftime("%Y-%m-%d"))
                                    db_cursor.execute(query,values)
                                    print("✅✅ Book borrowed successfully! You can bring your book back after some time.")
                                    mydb.commit()
                                else:
                                    print("1. ❌book is not available in database\n2.❌ or code is invalide ! please write something to the database")
                            code=input("write code here for borrow book = ")
                            borrow(code)
                        elif command=="advance":
                            print("⚒️ still working on  borrow page....")
                            
                        elif command=="return":  #return book  to datbace or library
                            
                            def returns(code):
                                Date=date.today()
                                query="insert into T_return_books(teacher_name, book_code ,date ) values(%s,%s,%s)"
                                values=(name,code,Date.strftime("%Y-%m-%d"))
                                db_cursor.execute(query,values)
                                print("✅✅ return successefully! now your are free")
                            code=input("write your code here = ").lower()
                            returns(code)
                        elif command=="show":
                        #this a page of show pay and timeline for reurn books
                            print("----------ℹ️ℹ️importance notice----------")
                            print("1. please read and understant every lines.")
                            print("2. 💸🤑ones you borrow book your charge start from now.")
                            print("3. ⌛after 20 days you will have to pay 50 rupees.")
                            print("4. ⌛20 days after you will have to pay 30+ rupeesfor⌛ 5 days")
                        elif command=="exit":
                             print("🙋🙋 logout successfully!")
                             break
                        
                else:
                    print("\n❌ Invalid username or ID. Please try again.")
        #enter the name and password for authorizetion
        user_name = input("Enter user_name:= ").lower()
        user_password = input("Enter user_password:= ").lower()
        signup(user_name, user_password)
        
        
        
#student logn command 
    elif command == "s_login":
        print("\n👤➡️🔒 verifing authority of student\n")
        class signin:
            def __init__(self,name,password):
                query="select * from user_info where name =%s and Password =%s"
                values=(name,password)
                db_cursor.execute(query,values)
                result=db_cursor.fetchone()
                if result:
                   print("\n✅ Login successful! Welcome,", name)
                   
                   while True:
                    print("welcome to knowledge world!")
                    print("1.📖🔍command for display books type --> 'Display'!")
                    print("2.📕🛒command for borrow book type --> 'borrow'!")
                    print("3.📖➡️🏛️command for return book type --> 'return'!")
                    print("4.⌛📖command for check return timeline book type --> 're-time'!")
                    print("5.🚀command for logout type --> exit")
                    command=input("enter command here = ")
                    if command=="display":
                        print()
                        print(" ⚒️ still working on  search page....")
                        print("1. Dispaly all books type --> 'yes'") 
                        query="select name,code,date from book_info"
                        db_cursor.execute(query)
                        print("✅✅books display successfully")
                        print(db_cursor.fetchall())
                        
                           
                    elif command=="borrow":
                       print(" ------  borrow page....")
                       while True:
                            print("1.now you can borrow the books")
                            print("2.please understand this commands!")
                            print("3.borrow  books type --> 'yes'")
                            print("3.No more  books type --> 'NO'")
                            command=input("type command here = ").lower()
                            if command=="yes":
                                print("1.firtsly type your name then type book code ")
                                def borrow(code):
                                     date_time=date.today()
                                     now_dt=date_time.strftime("%Y-%m-%d")
                                     qeury1="select name,code from book_info where code=%s"
                                     db_cursor.execute(qeury1,(code,))
                                     result=db_cursor.fetchone()
                                     if result:
                                        book_code=result[1]
                                        query2="insert into borrow_books(student_name,book_code,date) values(%s,%s,%s)"
                                        values=(name,book_code,now_dt)  #✅ Correct way to store values
                                        db_cursor.execute(query2,values)
                                        print("✅✅ borrow successefully")
                                        mydb.commit()
                                     else:
                                        print("❌ Book not found!")
                            
                               
                                book_code=input("enter the book code here = ").strip().lower()
                                borrow(name,book_code)
                            elif command == "no":
                                   print("😒😒achhe se padna leto ja rahe ho")
                                   break
                       
                    elif command=="return":
                       print(" ----------return book page....")
                       while True:
                            print("1.this is a time for return book")
                            print("2.return book type --> 'return")
                            print("3.if you return type --> 'exit'")
                            command=input("type your name here = ").lower()
                            if command=="return":
                                def return_b(book_name,book_code):
                                        now_date=date.today()
                                        query="insert into return_book(student_name,book_name,book_code.date) values(%s,%s,%s,%s)"
                                        values=(name,book_name,book_code,now_date)
                                        db_cursor.execute(query,values)
                                        mydb.commit()
                                        print("✅✅ book return successefully")
                                #name=input("write your name here = ").lower()
                                book_name=input("write book name here = ").lower()
                                book_code=input("write book code here = ").lower()
                                return_b(name,book_name,book_code)
                            elif command=="exit":
                                print("👌👌now you are free")
                            
                                  
                       
                    elif command=="re-time":
                       print(" ⚒️ still working on re-time page....")
                       print("1.the return time before 5 days after this you have to pay 100 rupees")
                       print("2.this is your last time ")
                       print("3.do wll study okh you")
                    elif command=="exit":
                       print("😊🚀👋Goodbye!")
                       break
                    else:
                       print("❌ Invalid command. please try again")
                   
                else:
                   print("\n❌ Invalid username or ID. Please try again.")
                
        user_name=input("🔘Eneter user_name here =").lower()
        user_password=input("🔑Eneter user_password here =").lower()
          
        signin(user_name,user_password)
        
        
        
        
    #administrator login command fi this match with command you can enter the admin section
    elif command == "admin":
    
        print("\n👤➡️🔒 verifing authority of admin\n")
        #here authentication is required to check admin
            
        admin_name=input("enter admin_name here = ").lower()
        password=input("enter password here = ").lower()
        #from there to authenticate admin with database mysql fetch data and check password and admin name  
        query="select * from admin where name = %s and password = %s" 
        values=(admin_name,password)
        db_cursor.execute(query,values)
        result=db_cursor.fetchone()
        #here check password and admin  name correct or not if is corect admin can perform tasks
        if result:
            #this is a message for authorized admin
            print("\n✅ Login successful! Welcome,", admin_name)
            print("")
            #this is a true while loop when the condition is not true this is not break
            #if condition true this break
            while True:
                #this is a command list 
                print("welcome to  admin duniya!")
                print("1.➕command for add teacher type --> teacher!")
                print("2.➕command for add student type --> student!")
                print("2.➕command for add book type --> book!")
                print("3.🚀command for logout type --> exit !")
                #here we type command for performing tasks
                command=input("enter command here! = ")
                
                
                
                #admin can easily create account of teacher 
                if command == "teacher":
                    print("---------teacher adding page.....")
                    while True:
                        print("add new teacher type --> yes!")
                        print("for not added type --> No!")
                        command=input("enter command here =").lower()
                        if command == "yes":
                            class teacher:
                                def __init__(self,name,password):
                                    salt=bcrypt.gensalt()
                                    hashed_password=bcrypt.hashpw(password.encode("utf-8"),salt)
                                    query="insert into teacher_info(name,password) values(%s,%s)"
                                    values=(name,hashed_password)
                                    db_cursor.execute(query,values)
                                    mydb.commit()
                                    print(f"\n✅ create successful! , {name}\n")
                            name=input("enter name of teacher = ").lower()
                            password=input("enter password of teacher = ").lower()
                            teacher(name,password)
                        elif command == "no":
                            print("😊🚀 👋Goodbye!")
                            break
                        else:
                           print("❌ Invalid command. please try again")  
                           
                           
                           
                #admin can easily create account of student
                elif command == "student":
                    print(" -------student adding page...")
                    while True:
                        print("add student type --> yes!")
                        print("for not added type --> NO!")
                        command=input("enter command = ").lower()
                        if command == "yes":
                            #using oops for adding student
                            class student:
                               def __init__(self,name,password):
                                   self.name=name
                                   self.__password=password               
                                   salt=bcrypt.gensalt()
                                   hashed_password=bcrypt.hashpw(self.__password.encode("utf-8"),salt)
                                   query="insert into user_info(name,password) values(%s,%s)"
                                   values=(self.name,hashed_password)
                                   db_cursor.execute(query,values)
                                   mydb.commit()
                                   print(f"\n✅ create successful! , {self.name}\n")
                            name=input("enter student name = ").lower()
                            password=input("enter password for student = ").lower()
                            student(name,password)
                        elif command=="no":
                           print("😊🚀 👋Goodbye!")
                           break
                        else:
                           print("❌ Invalid command. please try again")
                           
                           
                           
                #admin can  add more books
                elif command == "book":
                    print("---------book adding page.....")
                    while True:
                    # adding more books while loop
                        print("1.add more books type --> yes!")
                        print("2.No more add books type --> no!")
                        command=input("enter command here = ").lower()
                        if command=="yes":
                            #using oops for adding books in reposetery
                            class books:
                                def __init__(self,name,code):
                                    #database query for inert info
                                    now_date=date.today()
                                    query=" insert into book_info(name,code,date) values(%s,%s,%s)"
                                    values=(name,code,now_date.strftime("%Y-%m-%d"))
                                    db_cursor.execute(query,values)
                                    mydb.commit()
                                    print(f"\n✅ add successful! , {name}\n")
                            name=input("enter book name here = ").lower()
                            price=input("enter book code here = ").lower()
                            books(name,price)
                            
                            
                        #break loop statemen
                        elif command == "no":
                           print("😊🚀 👋Goodbye!")
                           break
                        else:
                           print("❌ Invalid command. please try again")    
                #tthis is a command for logout from admin panale
                elif command == "exit":
                    print("👋😊🚀GODbye!")
                    break
                else:
                    print("❌ERROR: Unknown command")
         # if admin nam and password not match  this shw this error and break the process         
        else:
            print("\n❌ Invalid username or ID. Please try again.")  
            
            
            
            
            

    elif command == "exit":
        print("\n😊🚀 Exiting the Library System. 👋Goodbye!\n")
        break  # Exit the loop

    else:
        print("\n❌ Invalid command! Please type 'signup', 'signin', or 'exit'.\n")

# Closing the database connection
db_cursor.close()
mydb.close()
