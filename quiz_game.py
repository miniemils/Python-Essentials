print("Welcome to the quiz game!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    print("Sorry to see you go.")
    quit()

print("Okay! Let's play.")
score = 0

answer = input("What does CPU stands for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stands for? ").lower()
if answer == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " question(s) correct.")
print("You got " + str((score * 100) / 4) + "%.")