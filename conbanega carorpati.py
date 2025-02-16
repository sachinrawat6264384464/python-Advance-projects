import time

# List of questions with options
questions = [
    {
        "ques": "Who is the Prime Minister of India?",
        "A": "Mahatma Gandhi",
        "B": "Narendra Singh Tomar",
        "C": "Yogi Adityanath",
        "D": "Narendra Modi"
    },
    {
        "ques": "Which field is related to Software Engineers?",
        "A": "IT",
        "B": "Mechanical",
        "C": "Civil",
        "D": "Hotel Management"
    }
]

# Correct answers
answers = ["D", "A"]

print("You have only **10 seconds** to answer each question!")

# Start game
command = input("Type 'start' to begin: ").lower()
if command == "start":
    prize = 10000
    index = 0

    for i in range(len(questions)):  # Loop through all questions
        print("\n-------- Welcome to Kaun Banega Crorepati --------")
        print(f"Q{index + 1}: {questions[i]['ques']}")
        
        # Display options
        for key, value in questions[i].items():
            if key != "ques":
                print(f"{key}: {value}")

        start_time = time.time()  # Start timer
        user_answer = input("Choose your answer (A, B, C, D): ").upper()
        end_time = time.time()  # End timer

        # Check time limit
        if end_time - start_time > 10:
            print("⏳ Time's up! You took too long to answer.")
            break

        # Check answer
        if user_answer == answers[i]:
            print(f"✅ Correct! You win ₹{prize}!")
            prize += 20000
            index += 1
        else:
            print("❌ Wrong answer! Game over.")
            break

    print("\n🎉 Thank you for playing! Your total prize money is: ₹", prize)
