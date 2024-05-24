play = "yes"
while play == "yes" or "y":
    name =input("Hello what is your name?\n")
    print("Nice to meet you",name,"Welcome do The Number guessing game!")
    print("My Name is Tristram")
    print("Lets Start Shall We?")
    try:
        answer = input("Pick A Number From 1-1000\n")
        answer = int(answer)
    except:
        print("Sorry But Thats Not An Option")
    print("Was Your Number",answer)
    print("Thanks For Playing")
    play = input ("Would You Like To Play Again\n")

