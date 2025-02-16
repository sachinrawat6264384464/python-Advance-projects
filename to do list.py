#to do list using mysql database project
import mysql.connector as myconn
mydb=myconn.connect(host="localhost",username="root", password="",database="library_system")
db_cursor=mydb.cursor()
"""
query="create table task_info(t_name varchar(20), t_status varchar(20))"
db_cursor.execute(query)

mydb.commit()

print("create successefully")
"""
task_list=[]
while True:
    count=0
    print("\n\n")
    print("welcome to task manager...")
    print("1.Create  tasks press '1'!")
    print("2.Add  tasks press '2'!")
    print("3.Update  tasks press '3'!")
    print("4.Delete  tasks press '4'!")
    print("5.Show  tasks press '5'!")
    print("6.for exit type '6'!")
    command=int(input("give command write here = "))
    
    
    if command==1:
        while True:
            print(" ")
            print(" ")
            print("--------- create  task page--------")
            print("1.create task  type command 'yes'")
            print("2.No more task  type command 'NO'")
            command=input("write command here = ").lower()
            if command=="yes":
                print("--------------------")
                print("1 How many tasks you want to create!")
                user=int(input("enter tasks quintty in numbers = "))
                for i in range(1,user+1):
                  task=input("type name of task here = ").lower()
                  task_list.append(task)
                  count+=1
                print("task added successfully➕")
            elif command=="no":
              print(" focus on your tasks")
              break
            else:
               print("invalid command type! try again")
               
               
               
    elif command==2:
         while True:
            print("")
            print("")
            print("------------Add task page----------")
            print("1.Add new tasks type 'yes'!")
            print("2.No moreAdd new tasks type 'NO'!")
            command1=input("write choice here = ").lower()
            if command1=="yes":
                print("1.How many task do you want to add !") 
                command2=int(input("enetr the tasks quintty here = "))
                for i in range(1,command2+1):
                    new_task=input("type new tasks here = ").lower()
                    task_list.append(new_task)
                    count+=1
                print("new tasks added successfully👍!")
            elif command1=="no":
                print("follow taks Estrictly😒")
                break
            else:
               print("invalid command type! try again")
               
               
               
    elif command==3:
          while True:
            print("")
            print("------update page-------")
            print("1. for update tasks type 'yes'.")
            print("2. No more  update tasks type 'NO'.")
            command1=input("write command here = ").lower()
            if command1=="yes":
                print()
                print("1. how many task do you want to update!")
                command2=int(input("write total quantty = "))
                for i in range(1,command2+1):
                    old_task=input("write the name of old  task that you want to update = ").lower()
                    new_task=input("write the name of new task here = ").lower()
                    for index,value in enumerate(task_list):
                        if value== old_task:
                          task_list[index]=new_task
                          print("New task added successfully")
                        
                print("  👍 All task updated successfully ")
            elif command1=="no":
               print("follow  your new tasks !")
               break
            else:
               print("invalide command type! try again")
               
               
               
    elif command==4:
        while True:
            print("")
            print("--------detele task page--------")
            print("1.delete the tasks type 'yes' !")
            print("2. NO more delete the tasks type 'no' !") 
            command1=input("write command here = ").lower()
            if command1=="yes":
                def delete(num):
                    for i in range(1,num+1):
                        name_task=input("eter the tasks name here = ").lower()
                        for index,value in enumerate(task_list):
                            if value== name_task:
                               del task_list[index]
                               count= count-1
                               print("tasks deleted")
                            else:
                              print("this task is not ina task_list! try again!")
                    print("delete tasks successfully 👍")
                command2=int(input("How many tasks do you want to delete = "))
                delete(command2)
            elif command1=="no":
                print(" 🙋 goodbye")
                break
            else:
                print("Please enter right command ! try again")
                
                
                
                
                
    elif command==5:
          print("Total tasks = ",count)
          print("tasks list\n",task_list)
          
          
          
          
          
    elif command==6:
          print("hope you enjoy this system ! ")
          break
            
db_cursor.close()
mydb.close()
            
            
            
            
            
          