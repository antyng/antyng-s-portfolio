"""
File: caesar.py
Name: Anting
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    user_keyin = int(input("Secret number: "))
    user_input = input("What's the ciphered string? ")
    upper_user_input(user_input)
    front = ALPHABET[26 - user_keyin:26]  #assemble a new alphabet base on user's input
    end = ALPHABET[:26 - user_keyin]
    new_alphabet = front + end
    original_text = decrypt(upper_user_input(user_input), user_keyin, new_alphabet)
    print("The deciphered string is: "+original_text)


def upper_user_input(s):  #transfer the lowercase to uppercase
    ans = ""
    for i in range(len(s)):
        ch = s[i]
        if ch.islower():
            ans += ch.upper()
        else:
            ans += ch
    return ans


def decrypt(a, b, c):
    ans = ""
    for i in a:
        if i.isalpha():
            if c.find(i)+b <= 25:
                ans += c[c.find(i)+b]
            else:
                ans += c[c.find(i)+b-26]
        else:
            ans += i
    return ans




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
