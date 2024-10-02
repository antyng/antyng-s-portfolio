"""
File: hailstone.py
Name:Anting
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print("This program computes Hailstone sequences.")
    print(" ")
    initial_number=int(input("Enter a number:"))
    step = 0
    if initial_number==1:
        print("It took 0 steps to reach 1.")
    while initial_number!=1:
        if initial_number%2==0:
            calculated_number=int(initial_number/2)
            print(str(initial_number)+" is even, so I take half:"+str(calculated_number))
            step+=1
        else:
            calculated_number = int(3*initial_number+1)
            print(str(initial_number) + " is odd, so I make 3n+1:" + str(calculated_number))
            step += 1
        if calculated_number!=1:
            initial_number = calculated_number
        else:
            break
    print ("It took "+str(step)+" steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
