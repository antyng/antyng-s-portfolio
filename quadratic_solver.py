"""
File: quadratic_solver.py
Name:Anting
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math

def main():
    print("stanCode Quadratic Solver!")
    enter_a=float(input("Enter a:"))
    enter_b=float(input("Enter b:"))
    enter_c=float(input("Enter c:"))
    root=enter_b*enter_b-4*enter_a*enter_c
    if root>0:
        root_outcomes1 = (-enter_b + math.sqrt(root)) / 2 * enter_a
        root_outcomes2 = (-enter_b - math.sqrt(root)) / 2 * enter_a
        print("Two roots:"+str(root_outcomes1)+","+str(root_outcomes2))
    elif root==0:
        root_outcomes1 = (-enter_b + math.sqrt(root)) / 2 * enter_a
        root_outcomes2 = (-enter_b - math.sqrt(root)) / 2 * enter_a
        print("One root:"+str(root_outcomes1))
    elif root<0:
        print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
