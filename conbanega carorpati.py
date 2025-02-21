import time
question=[
  {
    "ques": "1. Who developed the theory of relativity?",
    "A": "Isaac Newton",
    "B": "Albert Einstein",
    "C": "Galileo Galilei",
    "D": "Nikola Tesla",
    
  },
  {
    "ques": "2. What is the capital of Japan?",
    "A": "Seoul",
    "B": "Beijing",
    "C": "Tokyo",
    "D": "Bangkok",
   
  },
  {
    "ques": "3. Which planet is known as the Red Planet?",
    "A": "Venus",
    "B": "Mars",
    "C": "Jupiter",
    "D": "Saturn",
 
  },
  {
    "ques": "4. What is the chemical symbol for gold?",
    "A": "Ag",
    "B": "Fe",
    "C": "Au",
    "D": "Pb",
   
  },
  {
    "ques": "5. Who wrote 'Romeo and Juliet'?",
    "A": "Charles Dickens",
    "B": "William Shakespeare",
    "C": "Mark Twain",
    "D": "Jane Austen",
    
  },
  {
    "ques": "6. What is the hardest natural substance on Earth?",
    "A": "Gold",
    "B": "Iron",
    "C": "Diamond",
    "D": "Quartz",
    
  },
  {
    "ques": "7. Which is the longest river in the world?",
    "A": "Amazon River",
    "B": "Nile River",
    "C": "Yangtze River",
    "D": "Mississippi River",
    
  },
  {
    "ques": "8. Who was the first President of the United States?",
    "A": "Abraham Lincoln",
    "B": "George Washington",
    "C": "John Adams",
    "D": "Thomas Jefferson",
    
  },
  {
    "ques": "9. What is the currency of the United Kingdom?",
    "A": "Euro",
    "B": "Dollar",
    "C": "Pound Sterling",
    "D": "Rupee",
    
  },
  {
    "ques": "10. What is the boiling point of water at sea level?",
    "A": "90°C",
    "B": "100°C",
    "C": "80°C",
    "D": "110°C",
    
  },
  {
    "ques": "11. What is the largest mammal in the world?",
    "A": "Elephant",
    "B": "Blue Whale",
    "C": "Giraffe",
    "D": "Great White Shark",
  
  },
  {
    "ques": "12. Which continent has the most countries?",
    "A": "Asia",
    "B": "Europe",
    "C": "Africa",
    "D": "South America",
    
  },
  {
    "ques": "13. How many colors are in a rainbow?",
    "A": "5",
    "B": "6",
    "C": "7",
    "D": "8",
   
  },
  {
    "ques": "14. What is the national bird of the United States?",
    "A": "Bald Eagle",
    "B": "Peacock",
    "C": "Sparrow",
    "D": "Hawk",
    
  },
  {
    "ques": "15. Which gas do plants absorb from the atmosphere during photosynthesis?",
    "A": "Oxygen",
    "B": "Carbon Dioxide",
    "C": "Nitrogen",
    "D": "Hydrogen",
    
  }
]



answer=["B","C","B","C","B","c","B","B","C","B","B","C","C","A","B"]
write=0
wrong=0
amount=0
print("remender ! you have only 10 second for each question.!")
for index,ques in enumerate((question)):
   print(f"{ques["ques"]}")
   print(f"A: {ques["A"]}")
   print(f"B: {ques["B"]}")
   print(f"C: {ques["C"]}")
   print(f"D: {ques["D"]}")
   start_time=time.time()
   ans=input("enter the answer here a,b,c,d = ").upper()
   end_time=time.time()-start_time
   if end_time>10:
      print("⌚⌚you time line is over")
      wrong+=1
   elif ans==answer[index]:
      write+=1
      amount+=1000
   elif ans!=answer[index]:
      wrong+=1
print("total score:")
print("total write answer= ",write)
print("total wrong answer= ",wrong)
print("total wining amount= ",amount)
      
   

