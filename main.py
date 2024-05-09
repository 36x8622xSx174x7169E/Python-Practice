#working on  quiz
name = input ("Hello, what is your name?")
print("Hello",name,"welcome to my quiz")
print("My name is Tristram")

#asking  question and giving options
answer= input ("First Question: 1+1: \n a.2 \n b.3 \n c.2.5 ")
if answer == "2" or  answer == "a":
    print("Correct")
    print("Good Job!")
elif answer == "":
    print("What you didn't even try!")
#if the question is wrong it will say so using the else statment, if the question is right it will answer using an if statement if they just hit enter
#the question will answere with an elif statement
else:
    print("Incorrect")
    print("Try again")
#indent to make sure the code knows that it had a following result and that the the code is instantly finished
#this is another question
answer= input ("Secont Question: 2x3: \n a.3 \n b.7 \n c.6 ").lower()
if answer =="6" or answer == "c".lower:
    print("Correct")
    print("Good Job!")
elif answer == "":
    print("What you didn't even try!")
else:
    print("Incorrect")
    print("Try again")
    


   

#this tells the user that the quiz is over
    #end quiz
print("Thank you for playing my quiz!")

