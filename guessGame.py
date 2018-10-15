from random import randint 
randomNumber = randint(1,100)
print('---PLEASE SELECT A NUMBER BETWEEN 1 AND 100----')

userGuessList = [0]

while True:
	userGuessNumber = int(input('Enter a your number Guess'))

	if (userGuessNumber < 1)  or (userGuessNumber > 100):
		print('OUT OF BOUNDS')
		continue


	if userGuessNumber == randomNumber:
		print('YOU WON')
		break

	##if the guess is incorret, add guess to the list
	userGuessList.append[userGuessNumber]

	if userGuessList[-2]:

		if (abs(randomNumber - userGuessNumber)  <abs(randomNumber - userGuessList[-2])):
			print('WARMER')
		else:
			print('COLDER')


	else:
		if abs(randomNumber - userGuessNumber) <= 10:
			print('WARM')
		else:
			print('COLD') 

	break
	

