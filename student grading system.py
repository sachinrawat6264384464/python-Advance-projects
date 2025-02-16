#Project: Student Grading System 
#using for loop , while loop, function, 
#oops, and if-else

class Student:
    def __init__(self,name ,score):
         self.name=name
         self.score=score
         self.grade=determine_grade(score)
    def display_info(self):
        return f"students names: {self.name}\n students scores: {self.score}\n grades of students : {self.grade}"

def determine_grade(score):
           if score>=90:
              return "A"
           elif score>=70:
              return "B"
           elif score>=40:
              return "C"
           else:
              return "fail"
student_list=[]
while True:
      name=input("enter the name = ")
      score=int(input("enter the score = " ))
      student=Student(name,score)
      student_list.append(student)
      add_student=input("add another student typer yes/no = ")
    
      if add_student=="no":
            break
total=0
for student in student_list:
    total += student.score
average=total/len(student_list)
   
    
print("---student_list---")
for student in student_list:
    print(student.display_info())
print(f"average score of students = {average}")

if average>=90:
   print("excellent performance by students")
elif average>=60:
  print(" poor performance by students")
else:
  print("not good perfomance")


              

