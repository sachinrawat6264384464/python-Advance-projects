import os
def create_file(filename):
    try:
        with open(filename,'x') as f:
         print(f"✅ file {filename} created successfully")
    except FileExistsError:
         print("🔴 file is abelable already")
      
    except Exception as f:
         print("an error occupied")
def read_file(filename):
    try:
        with open(filename,'r') as f:
            filename=f.read()
            for read in filename:
            
              print(read,end="")
    
    except Exception as f:
            print("an error occured")

def write_file(filename):
    try:
        with open(filename,'w') as f:
         data=input(" write here about info/tasks = ")
         f.write(data)
         print(f" data write in to file = {filename} successfully")
    except IOError:
         print("data not write file  file = {filename}")


def delete_file(file_name):
    try: 
          data_delete=os.remove(file_name)
          print(f" ✅ file name is {file_name} deleted successefully")
    except FileExistsError:
          print(f" file name is {file_name} is not found")

def edit_info(file_name):
    try:
        with open(file_name,'a') as f:
         info=input(" write here about info/tasks = ")
         f.write(info)
         print("✅ info added successfully")
    except IOError:
       print("❌ not added some errors found please check")
        
          
          
if __name__ == '__main__':
 while True:
    
    print("\n🧐 welcome to file manager system...")
    print("1. create file type --> 1")
    print("2. read file all content --> 2")
    print("3. write in a  file all content --> 3")
    print("4. delete file permanent --> 4")
    print("5. edit file contet -->5")
    choice=int(input("enter the nuber = "))
    file_name=input("write a file name here = ")
    if choice==1:
        create_file(file_name)
        
    elif choice==2:
        read_file(file_name)
        
    elif choice==3:
        write_file(file_name)
        
    elif choice==4:
       
        delete_file(file_name)
        
    elif choice==5:
        edit_info(file_name)
        
        
    elif choice==6:
         print("now your are exit")
         break