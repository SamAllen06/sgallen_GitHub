userName = input("What's your name? ")
wantJoke = input(f"Hi {userName}, do you want to hear a joke? (Yes/No) ")
if wantJoke.lower().startswith(f"y"):
    rememberTomorrow = input(f"Will you remember me tomorrow? (Yes/No) ")
    if rememberTomorrow.lower().startswith("y"):
        rememberHour = input(f"Will you remember me in an hour? (Yes/No) ")
        if rememberHour.lower().startswith("y"):
            knock = input(f"Knock knock. ")
            for punctuation in "'?":
                knock = knock.replace(punctuation, "")
            if knock.lower() == "whos there":
                me = input(f"It's me. ")
                for punctuation in "'?":
                    me = me.replace(punctuation, "")
                if me.lower() == "its me who":
                    print(f"Aw man, I can't believe you forgot about me already.")
                elif me != "It's me who?":
                    print(f"I can't tell you my joke if you don't play along! Try again, but say 'It's me who?'")
            elif knock != "Who's there?":
                print(f"We can try again later when you'll follow the proper structure of the joke! Try saying 'Who's there?'")
        elif rememberHour != "Yes":
            print(f"I thought I was more memorable than that. :(")
    elif rememberTomorrow != "Yes":
        print(f"I thought I was more memorable than that. :(")
elif wantJoke != "Yes":
     print(f"Aw, that's sad. It would've been funny!")