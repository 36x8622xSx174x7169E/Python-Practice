
play = "yes"
QUESTION_FORMAT ="{}\nA.{}\nB.{}\nC.{}\nD.{}\n"
    #working on  quiz

name = input ("Hello, what is your name? \n")

if name == ("robert") or name == ("charlie").upper():
    surname = input("what is your surname?")
    if surname == ("mccrone") or surname == ("hill").upper():
        play = "NO!"
    print(play)
print("Hello",name,"welcome to my quiz")
print("My name is Tristram")
while play== "yes" or  play == "y":
    score = 0
    print("score=",score)
attempts = int(input("how many attempts do you want 1-4"))
if attempts >4:
    print("Come on believe in youself")

        



    #asking  question and giving options



    print("First Question")
    question = "1+1"
    a = "2"
    b = "3"
    c = "2.5"
    d = "1"
    answer= input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer == a or  answer == "a":
        score+=10
        print ("score=",score)
        print("Correct")
        print("Good Job!")
    elif answer == "":
        print("What you didn't even try!")
        # 1= mean that it dose not equal
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print("Thants not even an option!")
        print("At least try!?")
    #if the question is wrong it will say so using the else statment, if the question is right it will answer using an if statement if they just hit enter
    #the question will answere with an elif statement
    else:
        print("Incorrect")
        print("Try again")
    #indent to make sure the code knows that it had a following result and that the the code is instantly finished
    #this is another question
    question ="2x3"
    a = "3"
    b = "7"
    c = "6"
    d = "5"
    answer= input (QUESTION_FORMAT.format(question, a, b ,c ,d)).lower()

    if answer =="6" or answer == "c":
        score+=10
        print("Correct")
        print("Good Job!")
    elif answer == "":
        print("What you didn't even try!")
    elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
        print("Thants not even an option!")
        print("At least Try")
    else:
        print("Incorrect")
        print("Try again")
        


    

    #this tells the user that the quiz is over
        #end quiz
    play = input ("would you like to play again?").lower()
print("Thank you for playing my quiz!")

