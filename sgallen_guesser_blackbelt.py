import random
highGuess = 101
lowGuess = 0
tryNumber = 0
print("Backwards number guesser! You think of a number between 1 and 100 and I'll try and guess it in 7 tries!")
correctAnswer = input("Type your number here. I promise I won't look! ")
if correctAnswer.isdigit() == True:
    correctAnswer = int(correctAnswer)
    if correctAnswer > 100:
        print("I totally didn't mean to look at your number, but it's a good thing that I did because you evidently tried to cheat! Try again.")
    if correctAnswer < 1:
        print("I totally didn't mean to look at your number, but it's a good thing that I did because you evidently tried to cheat! Try again.")
    elif correctAnswer <= 100:
        firstGuess = random.randint(1, 100)
        firstAnswer = input(f"Is it {firstGuess}? (Say 'Too high', 'Too low', or 'Yes') ")
        keepGoing = True
        while keepGoing:
            tryNumber += 1
            if tryNumber > 6:
                if firstGuess == correctAnswer:
                    print("Woo hoo! In your face!")
                    keepGoing = False
                elif firstGuess != correctAnswer:
                    print("Darn it, I ran out of tries")
                    keepGoing = False
            elif tryNumber <= 7:
                firstGuess = int(firstGuess)
                for punctuation in "~!@#$%^&*()_+`-=[]\{}|;':,./ <>?":
                    firstAnswer = firstAnswer.replace(punctuation, "")
                if firstAnswer.lower() == "yes":
                    print("Woo hoo! In your face!")
                    keepGoing = False
                elif firstAnswer.lower() != "yes":
                    if firstAnswer.lower() == "toohigh":
                        if firstGuess <= correctAnswer:
                            print("I know I'm not supposed to peek at the number you gave me, but it's a good thing I did because you lied to me! :( Try again")
                            keepGoing = False
                        elif firstGuess > correctAnswer:
                            highGuess = firstGuess
                            firstGuess = random.randint(int(lowGuess)+1, int(firstGuess)-1)
                            firstAnswer = input(f"Is it {firstGuess}? (Say 'Too high', 'Too low', or 'Yes') ")
                    elif firstAnswer.lower() == "toolow":
                        if firstGuess >= correctAnswer:
                            print("I know I'm not supposed to peek at the number you gave me, but it's a good thing I did because you lied to me! :( Try again")
                            keepGoing = False
                        elif firstGuess < correctAnswer:
                            lowGuess = firstGuess
                            firstGuess = random.randint(int(firstGuess)+1, int(highGuess)-1)
                            firstAnswer = input(f"Is it {firstGuess}? (Say 'Too high', 'Too low', or 'Yes') ")
                    elif firstAnswer.lower() != "too low":
                        print("Try again and give me a valid response next time!")
                        keepGoing = False
elif correctAnswer.isdigit() == False:
    print("No special characters allowed! Try again. ")