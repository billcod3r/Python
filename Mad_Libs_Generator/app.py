import random

randomNum = random.randrange(0 , 101)
userGuess = input("What is your number?")
numUserGuess = int(userGuess)

# guess = 55
# random = 65
#

lowGuess = randomNum - numUserGuess

# guess = 75
# random = 5
# 

highGuess = numUserGuess - randomNum

if (randomNum > numUserGuess):
    print("Your guess was too low by " + str(lowGuess) + ".")
elif (randomNum < numUserGuess):
    print("Your guess was over by " + str(highGuess) + ".")
else:
    print("You guessed correctly! The winning number is " + str(numUserGuess) + ".")