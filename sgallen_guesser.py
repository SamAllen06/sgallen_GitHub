import random
print("Number Guesser: Try to guess the number I'm thinking of in 7 tries or less!")
correctAnswer = random.randint(1, 100)
attemptNumber = 0
keepGoing = True
while keepGoing:
    attemptNumber += 1
    userGuess = input(f"{attemptNumber}) What is your guess? ")
    if userGuess.isdigit() == True:
        userGuess = int(userGuess)
        if userGuess == correctAnswer:
            print("Correct! You win! ")
            keepGoing = False
        if attemptNumber > 6:
            if userGuess == correctAnswer:
                keepGoing = False
            elif userGuess != correctAnswer:
                print("Darn it, you ran out of tries! You fail.")
                keepGoing = False
        elif userGuess < correctAnswer:
            print("Nope, that's too low!")
        elif userGuess > correctAnswer:
            print("Nope, that's too high!")
    elif userGuess.isdigit() == False:
        print("No special characters allowed! ")
        if attemptNumber > 6:
            print("Darn it, you ran out of tries! You fail.")
            keepGoing = False