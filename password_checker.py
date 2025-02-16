#this is a regex library that matches patterns
import re
print("1.Medium hard condition.")
print("2.Simple condition.")
print("type '1' or '2'")
command=int(input("give command here = "))
if command == 1:
        print("--- password checker with medium hard condition----")
        def check_password(password):
              """has_digit=any(char.isdigit() for char in password)
              has_lower=any(char.islower() for char in password)
              has_upper=any(char.isupper() for char in password)
              has_special_character=re.search(r"[~!@#$%^&*()_?><,.`-]",password)"""
              if len(password)<8:
                print("pass must be 8 cheracter long.")
              
              if not any(char.isdigit() for char in password):
                print(" 'weak' !password Atleast one number is required in password")
              if not any(char.isupper() for char in password):
                print("'weak'!password Atleast one upper case character is required")
              if not any(char.islower() for char in password):
                print("'weak'!password Atleast one lower case character is required")
              if not re.search(r"[~!@#$%^&*()_?><,.`-]",password):
                print(" 'weak' !password have Atleast one special character required")
              return "your!password is 'strong'"
        def check_passw():
              """this is a programe to check password strongness"""
              print("for check password or for exit type 'exit")
              while True: 
                    password=input("type password here:=")
            
                    if password.lower() =="exit":
                       print("Thank you for using password cheker")
                       break
                    outcome=check_password(password)
                    print(outcome)
        if __name__ == "__main__":
         check_passw()
elif command == 2:
        print("--- password checker with simple condition----")
        def check_password(password):
              has_digit=any(char.isdigit() for char in password)
              has_lower=any(char.islower() for char in password)
              has_upper=any(char.isupper() for char in password)
              has_special_character=re.search(r"[~!@#$%^&*()_?><,.`-]",password)
              lenght=len(password)<8
              if not has_digit and has_lower and has_upper and has_special_character and lenght:
                print("pass must be 8 cheracter long.")
              
              
              return "your!password is 'strong'"
        def check_condition():
              """this is a programe to check password strongness"""
              print("for check password or for exit type 'exit")
              while True: 
                    password=input("type password here:=")
            
                    if password.lower() =="exit":
                       print("Thank you for using password cheker")
                       break
                    outcome=check_password(password)
                    print(outcome)
        
        check_condition()
else:
  print("invalide choice!")