print("Welcome to the quiz")
score = 0
# Input is a pre defined function in python which allows user to take input
playing = input("Do you want to play (yes/no) - ")

if playing.lower() != "yes": # .lower() is a method in python which is used to lower the text
    quit() # Quit is a pre defined function in python used to terminate program

print("Okay! Let's play")
answer1 = input("Q.1 What does CPU stands for ? ")
if answer1.lower() == "central processing unit":
    print("Correct :)")
    score +=1
else:
    print("Incorrect!")
answer1 = input("Q.2 What does GPU stands for ? ")
if answer1.lower() == "graphics processing unit" :
    print("Correct :)")
    score +=1
else:
    print("Incorrect!")
answer1 = input("Q.3 What does RAM stands for ? ")
if answer1.lower() == "random access memory":
    print("Correct :)")
    score +=1
else:
    print("Incorrect!")
answer1 = input("Q.4 What does PSU stands for ? ")
if answer1.lower() == "power supply unit":
    print("Correct :)")
    score +=1
else:
    print("Incorrect!")

print("The total you scored is "+str(score))
print("You got "+str((score/4)*100)+"%")
