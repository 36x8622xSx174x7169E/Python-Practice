#working on  quiz
name = input ("hello, what is your name?")
print("Hello",name,"welcome to my quiz")
print("My name is Tristram")

#asking  question and giving options
answer= input ("First Question: 1+1: \n a.2 \n a. 3 \n a.2.5 ")
if answer == "2":
    print("correct")
    print("good job!")
#if the question is wrong it will say so using the else statment, if the question is right it will do the same

else:
    print("Incorrect")
    print("Try again")
#this is another question
answer= input ("Secont Question: 2x3: \n a.6 \n a. 3 \n a.7 ")
if answer =="6":
    print("correct")
    print("Good Job")
else:
    print("Incorrect")
    print("Try again")
    


   

#this tells the user that the quiz is over
    #end quiz
print("thank you for playing my quiz")

