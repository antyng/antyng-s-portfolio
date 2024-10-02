"""
File: hangman.py
Name:Anting
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    s = random_word()
    print("The word looks like:"+dashes(s))
    print("You have "+str(N_TURNS)+" wrong guesses left.")
    user_input = input("Your guess: ")
    k = dashes(s)

    lifes = N_TURNS
    while lifes >0 :
        #check the format
        if len(user_input) != 1:
            print("Illegal format.")
        else:
            if user_input.isalpha():
                # transfer the lowercase to uppercase
                if user_input.isupper():
                    pass
                else:
                    user_input = user_input.upper()
                if s.find(user_input) == -1:
                    print("There is no " + str(user_input) + "'s in the word.")
                    k = replace_letter(s, user_input, k)
                    lifes -= 1
                    if lifes == 0:
                        print("You are completely hung :(")
                        print("The answer is: " + str(s))
                        break
                    else:
                        print("The word looks like: " + replace_letter(s, user_input, k))
                        print("You have " + str(lifes) + " wrong guesses left.")
                        user_input = input("Your guess: ")
                else:
                    print ("You are correct!")
                    k = replace_letter(s, user_input, k)
                    if k.find("-") != -1:
                        print ("The word looks like: "+replace_letter(s, user_input, k))
                        print("You have " + str(lifes) + " wrong guesses left.")
                        user_input = input("Your guess: ")
                    else:
                        print("You win!!")
                        print("The answer is " + str(s))
                        break

            else:
                print("Illegal format.")


def replace_letter(s, a, k):
    ans = ""
    for i in range (len(s)):
        ch = s[i]
        if k[i] == "-":
            if ch == a:
                ans += a
            else:
                ans += "-"
        else:
            ans += k[i]
    return ans


def dashes(s):
    ans = ""
    for i in range(len(s)):
        ans += "-"
    return ans


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
