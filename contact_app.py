import mysql.connector as myconn

mydb = myconn.connect(host="localhost", user="root", password="", database="library_system")
db_cursor = mydb.cursor()
"""squery="create table contact(name varchar(20), email varchar(20),phone int(10))"
db_cursor.execute(query)
print("contact created successfully")
mydb.commit()
"""
  # all contact store into datbase mysql database
count=0
while True:
    
    # choice for contact app
    print("\n")
    print("--☎️☎️contact dairy app---")
    print("1. contact create press ---> 1")
    print("2. search contact press ---> 2")
    print("3. count contact press ---> 3")
    print("4. delete one by one contact press ---> 4")
    print("5. delete all contact press ---> 5")
    print("6. exit from contact press ---> 6")
    #logic start from here
    choice=int(input("enter choice for contact 📞 = "))
    if choice==1:
        def contact_create(name,email,phone):
            
            query="insert into contact (name,email,phone) values(%s,%s,%s)" 
            values=(name,email,phone)
            db_cursor.execute(query,values)
            mydb.commit()
            print("✅📞contact created successfully!")
            
        name=input("Enter name for contact = ").lower()
        email=input("Enter email for contact = ").lower()
        phone=int(input("Enter phone number for contact = "))
        contact_create(name,email,phone)
    elif choice==2:
        print()
        print("1. search contact by the  1. name 2. phone ")
        command=input("write choice here = ").lower()
        # contact search by the name 
        if command=="name":
            def search_contact(name):
                query="select name,email,phone from contact where name=%s"
                (name)
                db_cursor.execute(query,(name,))
                result=db_cursor.fetchone()
                if name==result:
                     print("📞✅ contact is found successefully\n" ,result)
                else:
                    print("🔴 not found contact is not in contact list")
                mydb.commit()
            name=input("write name for search = ").lower()
            search_contact(name)
            
        #contact search by the phone number
        elif command == "phone":
            def search_contact(phone):
                query="select name,email,phone from contact where name=%s"
                db_cursor.execute(query,(phone,))
                result=db_cursor.fetchone()
                if phone==result:
                     print("📞✅ contact is found successefully\n" ,result)
                     print("")
                else:
                    print("🔴 not found contact is not in contact list")
                mydb.commit()
            phone=int(input("Enter phone number for search = "))
            search_contact(phone)
        else:
           print("invalid command type")
    
    # count contacts
    elif choice==3:
        query="select name from contact"
        db_cursor.execute(query)
        result=db_cursor.fetchall()
        for i in result:
            count+=1
        print(" ✅☎️ total contact count = ",count)
        mydb.commit()
    
    # delete contact one by one  form contact table by the name ...
    elif choice==4:
        print()
        print("1. search contact by the  1. name 2. phone ")
        command=input("write choice here = ").lower()
         
         # delete contact by the name...
        if command=="name":
            def delete_contact(name):
                query="delete from contact where name=%s"
                result=db_cursor.execute(query,(name,))
                if result:
                   print("☎️✅ contact deleted successfully")
                else:
                   print("this contact is not in contact table")
            
            name=input("write delete contact name = ").lower()
            delete_contact(name)
            
        # delete contact by the phone number
        elif command=="phone":
            def delete_contact(phone):
                query="delete from contact where name=%s"
                result=db_cursor.execute(query,(phone,))
                if result:
                   print("☎️✅ contact deleted successfully")
                else:
                   print("this contact is not in contact table")
            
            phone=int(input("Enter delete contact phone number = "))
            delete_contact(phone)
        
        else:
            print("your type invalide command")
        
    #delete all contact form contact database table  
    elif choice==5:
        query="delete from contact"
        db_cursor.execute(query)
        mydb.commit()
        print("✅✅ deleted  all contact successfully ✅✅")
    
    
    elif choice==6:
        print("🚀🚀 exit successefully from contact application")
        print("🔴 NOTE: your contact is save sefly in your database and you will be able to continue to contact again")
        break
    
    else:
        print("😊 you type invalid choice for contact application! try again")
        
        
             
db_cursor.close()
mydb.commit()