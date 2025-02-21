import random
import time
jokes=[
  {
    "ques": "1. Teacher: Sabse zyada mehnat kaun karta hai?",
    "answer": "Student, kyunki usi se to sab copy karte hain!"
  },
  {
    "ques": "2. Doctor: Yeh kaise hua?",
    "answer": "Mareez: Biwi mayke jaane ko keh rahi thi, main khushi se uchal pada aur pair fisal gaya!"
  },
  {
    "ques": "3. Pappu: Yaar, meri biwi bahut gusse mein hai!",
    "answer": "Golu: Kyon?\nPappu: Maine use bol diya ki tum meri zindagi ki sabse badi galti ho, aur wo Google pe search karne lagi ki galti kaise sudharen!"
  },
  {
    "ques": "4. Ladka: I love you!",
    "answer": "Ladki: Par main tumhe sirf ek dost ki tarah maanti hoon.\nLadka: Koi baat nahi, main bhi to timepass kar raha tha!"
  },
  {
    "ques": "5. Santa ne doctor se kaha: Meri biwi mujhse bahut pyaar karti hai!",
    "answer": "Doctor: Wo kaise?\nSanta: Jab bhi main bahar jata hoon, wo kehti hai, ‘Jaan, jaldi wapas aana!’"
  },
  {
    "ques": "6. Pati-patni ki ladai ho rahi thi...",
    "answer": "Pati: Tumhe mujhse shaadi kyon karni padi?\nPatni: Papa nahi maan rahe the ki tumse door rehna chahiye!"
  },
  {
    "ques": "7. Gabbar: Are o Samba, kitne aadmi the?",
    "answer": "Samba: Sir, ab to jangana online hoti hai, khud dekh lo!"
  },
  {
    "ques": "8. Pappu pariksha mein nakal kar raha tha, achanak teacher aa gayi!",
    "answer": "Teacher: Kya kar rahe ho?\nPappu: Ma'am, kuch nahi, bas bhagwan se connection bana raha hoon!"
  },
  {
    "ques": "9. Shaadi ke mandap mein pandit: Ab var-vadhu phere lein!",
    "answer": "Ladka: Pehle mujhe Instagram pe follow to kar lo!"
  },
  {
    "ques": "10. Mummy: Beta, uth ja warna school ke liye der ho jayegi!",
    "answer": "Baccha: Mummy, aaj school nahi jaunga!\nMummy: Kyon?\nBaccha: Aaj teacher ne poocha tha ki bada hoke kya banoge, maine mazaak mein 'Chhutti manane wala' bol diya, aur unhone agle din parents meeting rakh di!"
  }
]

while True:
   print("for new joke press -->1")
   print("for exit  press -->2")
   command=int(input("for display a new joke follow the command = "))
   
   if command==1:
    
      for index,ques in enumerate(jokes):
            print("")
         
            
            next=int(input("enter 2 for next joke or 3 for exit = "))
            if next ==2:
               print("😂🤣 jokes")
               print(f"{ques["ques"]}")
               print(f"jabab={ques["answer"]}")
            elif next==3:
               break
            
            elif next!= 2 :
                  print("⚠️ कृपया 2 या 3 ही दबाएं।")
                  
        
   elif command==2:
    break
    
   else:
     print("you type invalid command, please")
