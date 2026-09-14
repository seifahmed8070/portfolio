import time
import random
score = 20


def main():
    print("Welcome to the Adventure Game!")
    while True:
        play_game()
        while True:
            play_again = input("Do you want to"
                               "play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        if play_again != 'yes':
            print("Thanks for playing!")
            break


def play_game():
    print("\n--- Starting game ---")
    new_round()
# الجزء القادم هو اساس اللعبه و بدايتها


def new_round():
    lst = ["red", "blue", "black", "green"]
    lstt = [1, 2]
    time.sleep(2)
    print("You now found yourself in a bank,"
          "and now you are there and it is closed,"
          "and you have 20 points")
    time.sleep(2)
    print("There are three doors in front of you")
    time.sleep(2)
    print("The first door is")
    time.sleep(2)
    print(random.choice(lst))
    time.sleep(2)
    print("and says __forbidden entry__")
    time.sleep(2)
    print("The second door is")
    time.sleep(2)
    print(random.choice(lst))
    time.sleep(2)
    print("and has nothing written on it,"
          "but you must have the key to enter it")
    time.sleep(2)
    print("The third door is ")
    time.sleep(2)
    print(random.choice(lst))
    time.sleep(2)
    print("and says __push___ ")
    time.sleep(2)
    print("1. Enter the first door")
    time.sleep(2)
    print("2. Enter the second door")
    time.sleep(2)
    print("We will choose this selection at random")
    time.sleep(2)
    print("Please enter")
    time.sleep(2)
    print(random.choice(lstt))
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 ): ")
    if choice == '1':
        door1_()
    elif choice == '2':
        door3_()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        new_round()
#  الجزء القادم هو اذا اختار المستخدم 1 يظهر هذا الجزء


def door1_():
    print("\n--- Guess what's behind the first door ---")
    time.sleep(2)
    print("You now have many screens in"
          "front of you monitoring the entire bank")
    time.sleep(2)
    print("You are now in the bank's control room and the safes")
    time.sleep(2)
    print("This room should have an observer, but there is no one")
    time.sleep(2)
    print("But there is nothing else in the room."
          "There is a door on the right side")
    time.sleep(2)
    print("I expect the observer to be there")
    time.sleep(2)
    print("You have three choices")
    time.sleep(2)
    print("1. Sitting at the control desk to find out who is in the bank")
    time.sleep(2)
    print("2. Getting closer to the door to find out what is behind it")
    time.sleep(2)
    print("3. Exit the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        Sitting_at_the_control_desk_1_door()
    elif choice == '2':
        Getting_closer_to_the_1door()
    elif choice == '3':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        door1_()
    # vالجزء القادم هو اذا اختار المستخدم 1 سوف يظهر له هذه القصه


def Sitting_at_the_control_desk_1_door():
    print("You are now on his desk and you can see the bank")
    time.sleep(2)
    print("You see now that there is no one in a bank, but guess"
          "what room there must be a security man in it?")
    time.sleep(2)
    print("You also see the locked room that must be opened with"
          "a key that I mentioned to you before,"
          "but there is something strange in it")
    time.sleep(2)
    print("A man is standing alone in this room, but you are"
          "unable to see what he is doing,"
          "and his clothes do not pretend that he works in a bank")
    time.sleep(2)
    print("But be careful, you now hear the steps of the"
          "security man heading to the door and"
          "he will come out in front of you now")
    time.sleep(2)
    print("What do you want to do now? If I were you,"
          "I would look for a weapon to confront the security man")
    time.sleep(2)
    print("I will give you two weapons to confront the security man")
    time.sleep(2)
    print("1. Iron stick")
    time.sleep(2)
    print("2. Knife")
    time.sleep(2)
    print("3. Or leave the room before he sees you")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        global score
        print("Unfortunately, this weapon does not enable"
              "you to confront the security man because he"
              "had a gun and killed you when you tried to confront him")
        time.sleep(2)
        print("Your points before")
        time.sleep(2)
        print(score)
        score = score - 20
        print("Your points yet")
        time.sleep(2)
        print(score)
        if score < 0:
            exit()
    elif choice == '2':
        print("Unfortunately, this weapon does not enable"
              "you to confront the security man because"
              "he had a gun and killed you when you tried to confront him")
        time.sleep(2)
        print("Your points before")
        time.sleep(2)
        print(score)
        score = score - 20
        print("Your points yet")
        time.sleep(2)
        print(score)
        if score < 0:
            exit()
    elif choice == '3':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        Sitting_at_the_control_desk_1_door()


def Getting_closer_to_the_1door():
    print("You are now next to the door and you hear some sounds inside,"
          "as if it were a bathroom")
    time.sleep(2)
    print("There is a person inside who could be"
          "the observer I mentioned to you before")
    time.sleep(2)
    print("What do you want to do now? If I were you,"
          "I would leave the room because the security"
          "man was with him, and I would stop you if he saw you")
    time.sleep(2)
    print("You have two options")
    time.sleep(2)
    print("1. Sitting at the supervisor’s desk")
    time.sleep(2)
    print("2. Leave the room before he sees you")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 ): ")
    if choice == '1':
        Sitting_at_the_control_desk_1_door()
    elif choice == '2':
        global score
        print("You won 10 points because you chose"
              "to leave the room instead of venturing out and"
              "sitting at the control desk")
        time.sleep(2)
        print("Your points before")
        time.sleep(2)
        print(score)
        # النقاط زادت لانه لم يجلس علي مكتب المراقبه و اختار الاختيار الصحيح
        score = score + 10
        print("Your points yet")
        time.sleep(2)
        print(score)
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 ")
        Getting_closer_to_the_1door()
# الجزء القادم هو يخص الباب الثاني الذي عرف عنوا المستخدم في بداية اللعبه


def door2_():
    print("You are now in front of a room that may be"
          "the one with the closed door")
    time.sleep(2)
    print("It has many offices, and most of them have desks with"
          "computers on them, similar to employee offices")
    time.sleep(2)
    print("There is an office on the right that you can see from afar,"
          "closed and surrounded by glass"
          ", unlike the other open offices")
    time.sleep(2)
    print("There is also a locked safe at the end of the room")
    time.sleep(2)
    print("But there is something else strange. There is a person next"
          "to the closed office that"
          "I mentioned to you before, standing alone, and his clothes"
          "do not indicate that he works in the bank.")
    time.sleep(2)
    print("If I were you, I would leave the room because this"
          "man might be a thief, and if I approached him,"
          "he might kill me")
    time.sleep(2)
    print("But you must choose. You have three options")
    time.sleep(2)
    print("1. Approach the man to see what he is doing")
    time.sleep(2)
    print("2. Stay away from the man and walk quietly to the safe")
    time.sleep(2)
    print("3. Exit the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        Approach_the_man_2door()
    elif choice == '2':
        Stay_away_from_the_man_2door()
    elif choice == '3':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        door2_()


def Approach_the_man_2door():
    print("When you approach the man, you see that he"
          "is trying to open the locked office."
          "You also see that there is a safe inside"
          "the room, so this man is a thief because"
          "he does not have the key.")
    time.sleep(2)
    print("You can now leave the room or face this man. You must choose")
    time.sleep(2)
    print("I will give you two weapons")
    time.sleep(2)
    print("1. Iron stick")
    time.sleep(2)
    print("2. Pistol")
    time.sleep(2)
    print("3. Or walk away quietly and leave the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        print("Good, you killed the man, so what are you going to do?")
        time.sleep(2)
        print("1. Trying to enter the closed office")
        time.sleep(2)
        print("2. Go to the safe")
        time.sleep(2)
        print("3. Exit the room")
        choice = input("What do you choose? (1 or 2 or 3): ")
        if choice == '1':
            global score
            print("You lost all your points because"
                  "when you tried to enter the office,"
                  "the emergency alarm rang and the police were on the way")
            time.sleep(2)
            print("Your points before")
            time.sleep(2)
            print(score)
    # هنا المستخدم خسر لانه اختار انه يفتح الباب الذي كان السارق يحاول فتحه
            score = score - score
            time.sleep(2)
            print("Your points yet")
            time.sleep(2)
            print(score)
            if score <= 0:
                exit()
        elif choice == '2':
            Stay_away_from_the_man_2door()
        elif choice == '3':
            new_round()
        else:
            print("Invalid choice. Please enter 1 or 2 or 3")
            Approach_the_man_2door()
    elif choice == '2':
        print("you killed this man, but this was a wrong"
              "choice because the gun makes a loud sound and"
              "the alarm rings in the bank"
              "after the security man heard the sound.")
        time.sleep(2)
        print("You lost 20 points and they are your total points")
    elif choice == '3':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        Approach_the_man_2door()


def Stay_away_from_the_man_2door():
    print("You have now headed to the safe, but you must walk"
          " quietly so as not to attract the man's attention")
    time.sleep(2)
    print("When you are in front of the safe,"
          "you usually find that you must have the password with you")
    time.sleep(2)
    print("But there is a message written"
          "“Search for the password and you will find it.”")
    time.sleep(2)
    print("You can now search the surroundings of the safe,"
          "or the password may be in a remote place or"
          "outside the room")
    time.sleep(2)
    print("You have two options")
    time.sleep(2)
    print("1. Try to search for the password around the safe")
    time.sleep(2)
    print("2. Exit the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        print("After searching extensively, you did not find the password")
        time.sleep(2)
        print("You have two options")
        time.sleep(2)
        print("1. To stay away from the closet and do something else")
        time.sleep(2)
        print("2. Exit the room")
        time.sleep(2)
        choice = input("What do you choose? (1 or 2 ): ")
        if choice == '1':
            door2_()
        elif choice == '2':
            new_round()
    elif choice == '2':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3")
        Stay_away_from_the_man_2door()


def door3_():
    print("\n--- Guess what's behind the third door  ---")
    time.sleep(2)
    print("In front of you are servers, electricity generators,"
          "electricity wires, and other things that"
          "are dangerous for the bank if any untrusted person enters them.")
    time.sleep(3)
    print("The strange thing is that this room does not"
          "have warnings from the outside or is closed"
          "like the room I mentioned to you before")
    time.sleep(3)
    print("Only electrical and server engineers should enter it")
    time.sleep(3)
    print("But there is something else. The door at the end of the"
          "room is white and there is nothing written on it")
    time.sleep(3)
    print("There is another thing: a computer connected to the server")
    time.sleep(2)
    print("If I were you, I would go to the computer because it"
          "may be the most important computer in the bank so I"
          "can see the information on it, but you must choose.")
    time.sleep(3)
    print("You have three choices")
    time.sleep(2)
    print("1. Open the white door")
    time.sleep(2)
    print("2. Approaching the computer and using it")
    time.sleep(2)
    print("3. Exit the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        Open_the_white_door_3door()
    elif choice == '2':
        Approaching_the_computer_3door()
    elif choice == '3':
        new_round()
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")
        door3_()


def Open_the_white_door_3door():
    print("You are now in front of a corridor,"
          "at the end of which there is a light indicating"
          "the presence of something wide at the end")
    time.sleep(2)
    print("It is possible that this corridor is the"
          "exit to the room with the closed door that"
          "I mentioned to you before")
    time.sleep(2)
    print("Or could this passage lead to something"
          "else dangerous, I don't know")
    time.sleep(2)
    print("So you have two options")
    time.sleep(2)
    print("1. Enter the corridor and walk to the end")
    time.sleep(2)
    print("2. Close the door and do something else")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 ): ")
    if choice == '1':
        global score
        print("Good, now you have won 10 points"
              "because you chose to enter the corridor and"
              "were not afraid that there would be something"
              "strange that would lose you points.")    
        time.sleep(2)
        print("Your points before")
        time.sleep(2)
        print(score)
        # هنا اللعب ذادت نقاطه لانه اختار ان يدخل الممر و هذا اختيار موفق له 
        score = score + 10
        time.sleep(2)
        print("Your points yet") 
        time.sleep(2)
        print(score)
        time.sleep(2)
        print("Predict what is at the end of the corridor")
        door2_()
    elif choice == '2':
        door3_()         
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")
        Open_the_white_door_3door()


def Approaching_the_computer_3door():
    print("You are sitting at the computer and you"
          "must open it and have the password")
    time.sleep(2)
    print("But there is something written on the computer:"
          "“You can search for the password and you will find it.”")
    time.sleep(2)
    print("This is strange. I don't know why this"
          "is written, but what I do know is that you have to search for"
          " the password to open the computer")
    time.sleep(2)
    print("There may be something on the computer"
          "that will help you earn points")
    time.sleep(2)
    print("Therefore, you must search for the password"
          "in order to be able to open the computer or"
          " not care about the computer")
    time.sleep(2)
    print("You have there choices")
    time.sleep(2)
    print("1. Open the door in the room")
    time.sleep(2)
    print("2. Try to search for the password")
    time.sleep(2)
    print("3. Exit the room")
    time.sleep(2)
    choice = input("What do you choose? (1 or 2 or 3): ")
    if choice == '1':
        Open_the_white_door_3door()     
    elif choice == '2':
        print("Good, you won 10 points because"
              "you chose to search for the password,"
              "and it is possible that you will not"
              "find the password in the room.")
        time.sleep(2)
        print("Your insistence on searching helped you"
              "earn points without finding the password")
        time.sleep(2)
        print("After searching extensively, you did not find the"
              "password, so what will you do?")
        time.sleep(2)
        print("You have two options")
        time.sleep(2)
        print("1. Open the door in the room")
        time.sleep(2)
        print("2. Exit the room")
        time.sleep(2)
        choice = input("What do you choose? (1 or 2 ): ")
        if choice == '1' :
            Open_the_white_door_3door()
        elif choice == '2' :
            new_round()
    elif choice == '3':
        new_round()     
    else:
        print("Invalid choice. Please enter 1 or 2 or 3.")
        Approaching_the_computer_3door()
if __name__ == "__main__":
    main()
