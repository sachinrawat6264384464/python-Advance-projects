from textblob import TextBlob 
def speling_check(leters):

        word=TextBlob(leters)
        correct=str(word.correct())
        if correct==word:
            return f"this is a correct speling {correct}"
        else:
           return f"{word} wrong speling! correct is {correct}"

data=input("write speling here = ")
result=speling_check(data)
print(result)





