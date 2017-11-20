import random
import os
import sys


pos = ["Heads" , "Tails"]


while True:
	print("Say H for heads and T for tails")
	choice = input("")
	if (choice == "T") or (choice == "t"):
		print("You chose tails")
		choice = "T"
		break
	elif (choice=="H") or (choice=="h"):
		print("You chose heads")
		choice = "H"
		break
	else:
		print("Dude, choose either T or H")
		print("")

outcome = random.choice(pos)

print("")

print("The computer flips the coin at it lands on ...")
print(outcome , "!!!")

if ((outcome == "Heads") and (choice == "H")) or ((outcome == "Tails") and (choice == "T")):
	print("YOU WIN!")
else:
	print("Better luck next time...")

print("")
input("Press any key to exit")


