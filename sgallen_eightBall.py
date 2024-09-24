keepGoing = True
while keepGoing:
    import random
    response = ["Absolutely!", "Definitely not.", "Sure, why not.", "No way, Jose.", "Maybe, I guess.", "The spirits are unclear. Ask again later.", "What a terrible question!", "The fortunes are in your favor!", "Why would you even ask me that?", "Never mind that question, I sense great riches in your future!", "No clue!"]
    print(f"What do you want me to do, master? ")
    print(f"   1: Print all the fortunes.")
    print(f"   2: Print a specific fortune.")
    print(f"   3: Print a random fortune.")
    print(f"   4: Tell me my future!")
    print(f"   5: Exit the program.")
    print("")
    answer = input(f"Please choose 1, 2, 3, 4, or 5: ")
    print("")
    for punctuation in "`~!@#$%^&*()_+=[]\{}|;':,/<>?":
        answer = answer.replace(punctuation, "")
    if answer == "1":
        print("Why of course, Master!")
        print("")
        for (specificFortune, response) in enumerate(response):
            print(f"{specificFortune}: {response}")
    elif answer == "2":
        askFortune = input("What fortune do you want? (0-10): ")
        askFortune = int(askFortune)
        if askFortune >= 0:
            if askFortune <= 10:
                print("")
                print(f"Your fortune is '{askFortune}: {response[askFortune]}'")
            elif askFortune >= 10:
                print("Come on. I can't tell you your future if you don't choose a number between 0 and 10!")
        elif askFortune  <= 0:
            print("Come on. I can't tell you your future if you don't choose a number between 0 and 10!")
        elif askFortune != 5:
            print("Come on. I can't tell you your future if you don't choose a number between 0 and 10!")
    elif answer == "3":
        randomFortune = random.randint(0, 10)
        randomFortune = int(randomFortune)
        print("Let me think...")
        print("Ooh, here's a good one!")
        print(f"{randomFortune}: '{response[randomFortune]}'")
    elif answer == "4":
        input(f"THE ALL-POWERFUL EIGHT BALL IS READY FOR YOUR QUESTION! (In yes or no format, pretty please.): ")
        randomFortune = random.randint(0, 10)
        randomFortune = int(randomFortune)
        print("")
        print(f"{response[randomFortune]}")
        print("")
        print("")
    elif answer == "5":
        keepGoing = False
    elif answer != "5":
        print("Come on, you've got to choose a whole number between 1 and 4 if you want to play!")