
import random
play = "yes"
QUESTION_FORMAT ="{}\nA.{}\nB.{}\nC.{}\nD.{}\n"
GOOD_COMMENTS=["Way To Go!","Keep It Up!","Fantastic!"]
BAD_COMMENTS=["Keep Trying","Maybe Next Time","Dont Give Up"]
QUESTIONS= ["First Question:What Is 1+1","Second Question:What Is 2x3","Third Question: 2x=7"]
OPTIONS = [["2","3","2.5","1"],["3","7","6","5"],["2.5","3.5","3","7"]]
SHORT_OPTIONS=["a","b","c","d"]
ANSWERS = [0,2,1]

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




    for i in range(len(QUESTIONS)):
        question_attempts=tries
        while question_attempts >0:
            answer=input(QUESTION_FORMAT.format(QUESTIONS[i],OPTIONS [i][0],OPTIONS [i][1],OPTIONS [i][2],OPTIONS [i][3])).lower()
            if answer == (OPTIONS[i][ANSWERS[i]]) or answer == (SHORT_OPTIONS[ANSWERS[i]]):
                print(random.choice(GOOD_COMMENTS))
                score +=10
                print("score =",score)
                break
            elif answer in SHORT_OPTIONS or answer in OPTIONS[i]:
                print("Incorrect!")
                print(random.choice(BAD_COMMENTS))
                question_attempts -=1
            else:
                print("Thats Not Even An Option!")
    

        



        

        #this tells the user that the quiz is over
        #end quiz
    play = input ("would you like to play again?").lower()
#print("Thank you for playing my quiz!")

