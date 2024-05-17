import random
play = "yes"
QUESTION_FORMAT ="{}\nA.{}\nB.{}\nC.{}\nD.{}\n"
GOOD_COMMENTS=["Way To Go!","Keep It Up!","Fantastic!"]
BAD_COMMENTS=["Keep Trying","Maybe Next Time","Dont Give Up"]
QUESTIONS= ["First Question:What Is 1+1","Second Question:What Is 2x3","Third Question: 2x=7"]
OPTIONS = [["2","3","2.5","1"]["3","7","6","5"]["3","2.5","3","7"]]
SHORT_OPTIONS=["a","b","c","d"]


    #working on  quiz

name = input ("Hello, what is your name? \n")

if name == ("robert") or name == ("charlie"):
    surname = input("what is your surname?")
    if surname ==("mccrone") or surname == ("hill").upper():
            play = "NO!"
            print(play)
    else:
        print("Hello",name,"welcome to my quiz")
        print("My name is Tristram")
else:
    print("Hello",name,"welcome to my quiz")
    print("My name is Tristram")


while play== "yes" or  play == "y":
    score = 0
    
    try:
        tries= input("How many attempts do you want at each question? 1-4")
        tries= int(tries)
        if tries >4:
            print("Sorry but the maximum amount is 4, have some faith in yourself!")
            tries = 4
    except:
        print("Opps that didn't work!")




    print("score=",score)
    print("First Question")
    question_attempts=tries
    while question_attempts >0:
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
            print(GOOD_COMMENTS[1])
            break
        elif answer == "":
            print("What you didn't even try!")
            # != mean that it dose not equal
        elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print("Thants not even an option!")
            print("At least try!?")
           
        #if the question is wrong it will say so using the else statment, if the question is right it will answer using an if statement if they just hit enter
        #the question will answere with an elif statement
        else:
            question_attempts -=1
            print("Incorrect")
            print(BAD_COMMENTS[0])
        
    #indent to make sure the code knows that it had a following result and that the the code is instantly finished
    #this is another question
    question_attempts=tries
    while question_attempts >0:
        question ="2x3"
        a = "3"
        b = "7"
        c = "6"
        d = "5"
        answer= input (QUESTION_FORMAT.format(question, a, b ,c ,d)).lower()

        if answer =="6" or answer == "c":
            score+=10
            print("Correct")
            print(random.choice (GOOD_COMMENTS))
            break
        elif answer == "":
            print("What you didn't even try!")
        elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print("Thants not even an option!")
            print("At least Try")
        else:
            question_attempts -=1
            print("Incorrect")
            print(BAD_COMMENTS[3])
            
    question_attempts=tries
    while question_attempts >0:
        question = "2x=7"
        a = "3"
        b = "2.5"
        c = "2"
        d = "7"
        answer = input (QUESTION_FORMAT.format(question, a, b, c, d)).lower()
        if answer =="2.5" or answer == "b".lower():
            score+=10
            print("Correct") 
            print(GOOD_COMMENTS[3])
            break
        elif answer == "":
            print("What you didn't even try!")
        elif answer != a and answer != "a" and answer != b and answer != "b" and answer != c and answer != "c" and answer != d and answer != "d":
            print("Thats not even an option!")
            print("At least try")
        else:
            question_attempts -=1
            print("Incorrect")
            print(BAD_COMMENTS[2])
           



        

        #this tells the user that the quiz is over
        #end quiz
    play = input ("would you like to play again?").lower()
#print("Thank you for playing my quiz!")

