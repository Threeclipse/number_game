from random import randint

# Minimum number in range
minimum = 0

# Maximum number in range
maximum = 30

# Number of almined player-input guesses
guesses = 3

# Initiate a random number that will be the basis of the game
random_num = randint(minimum, maximum)

# The game chooses the first number for the player
first_num = randint(minimum, maximum)

# Input validation
def inputNumber(message):
	while True:
		try:
			userInput = int(input(message))
		except ValueError:
			print("\nThat's not a number, try again!\n")
			continue
		else:
			return userInput

# Initiate the while loop index
i = 0

while i < guesses:
	# Increment the while counter.
	i = i + 1
	# Automatic first guess made by system
	if i == 1:
		print(f"\nI'm thinking of a number between {minimum} and {maximum}.\nYou have {guesses} tries to find the number.\nTo make this more interesting, I'm going to make your first guess for you.\n\n...and that number is {first_num}.")
		if first_num < random_num:
			print(f"\n{first_num} is too low!\n")
		if first_num > random_num:
			print(f"\n{first_num} is too high!\n")
		if first_num == random_num:
			print("\nHeavens to Murgatroyd!!! We chose the right number for you!\n\n")
			break

	# User inputs guess 1 through max allowed guesses
	guess = inputNumber(f"You have [{4-i}] guesses left> ")

	if guess != random_num:
		if guess < random_num:
			print(f"\n{guess} is too low!\n")
	
		if guess > random_num:
			print(f"\n{guess} is too high!\n")

	else:
		print(f"\n{guess} is the right answer!\n\nᕕ( ᐛ )ᕗ  !!! Great job !!!\n\n")
		quit(0)

print(f"Sorry, the number was {random_num}.\nBetter luck next time.\n\n ｡ﾟヽ(ﾟ´Д｀)ﾉﾟ｡ \n\n")