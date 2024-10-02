"""
File: prime_checker.py
Name:Anting
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""
EXIT=-100

def main():
	print("Welcome to the prime checker!")
	initial_number=int(input("n: "))
	first_odd_prime=3
	if initial_number==EXIT:
		print("Have a good one!")
	else:
		while True:
			if initial_number==EXIT:
				print("Have a good one!")
				break
			elif initial_number%2==0 and initial_number!=2: #initial number is even but not 2
				print(str(initial_number) + " is not a prime number.")
				initial_number = int(input("n: "))
			elif initial_number==2:
				print(str(initial_number) + " is a prime number.")
				initial_number = int(input("n: "))
			elif initial_number==3:
				print(str(initial_number) + " is a prime number.")
				initial_number = int(input("n: "))
			else:
				while initial_number%2 !=0 and initial_number%first_odd_prime!=0:
				#check if initial number can be divided by any odd less than itself
					first_odd_prime += 2
				#check the next odd number until it is same with initial number or can be divided
				max_odd_prime=first_odd_prime
				if initial_number==max_odd_prime:
					print(str(initial_number) + " is a prime number.")
					initial_number = int(input("n: "))
					first_odd_prime=3
				else:
					print(str(initial_number) + " is not a prime number.")
					initial_number = int(input("n: "))

















# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
