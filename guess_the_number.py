import random

number = input("Type a number: ")

if number.isdigit():
    number = int(number)
    if number < 0:
        print("Please, type a number larger than 0 next time.")
        quit()
else:
    print("Please, type a number next time.")
    quit()

random_number = random.randint(0, number)
guesses = 0

while True:
    guess = input(f"Make a guess between 0 and {number}: ")
    if guess.isdigit():
        guess = int(guess)
    else:
        print("Please, type a number next time.")
        continue
    guesses += 1
    
    if guess == random_number:
        print("Congrats! You got it in", guesses, "guesses")
        break
    elif guess < random_number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")