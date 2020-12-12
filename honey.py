
from random import *
from pprint import pprint
import random

# Function prototyping
def validate(char):
    # Input validation
	while char != 'Y' and char != 'y' and char != 'N' and char != 'n':
            char = input("Would you like to enter another inquiry? (Y/N) ")

# Prompts user and defines variables
while True:
    message = input("Please enter a secret message to store: ")
    userPass = input("Please enter a password: ")
    passwordsToSeeds = {}   # dictionary
    seedsToMessages = {}    # dictionary
    trueSeed = random.randint(10, 30)    # Random seed value
    states = {
        'A': 'The Bank account number is 8437293469',
        'B': 'The Bank account number is 7456328198',
        'C': 'The Bank account number is 3564927154',
        'D': 'The Bank account number is 5639201638',
        'E': 'The Bank account number is 9362018467',
        'F': 'The Bank account number is 7284038137',
        'G': 'The Bank account number is 2743856743',
        'H': 'The Bank account number is 8364810473',
        'I': 'The Bank account number is 6418403728',
        'J': 'The Bank account number is 8642016748',
        'K': 'The Bank account number is 6493712746',
    }
    ' Verify input with the user '
    print("Your password is " + userPass
          + ", your seed value is " + str(trueSeed)
          + ", and your secret message is " + message
          + "\n======================================================")

    # Seed generator + Sweetwords generator
    # Manipulate the password input by the user
    #   Add a string to that password
    #   Seeds should remain as integers that
    #   be converted into binary digits
    passwordsToSeeds[userPass] = trueSeed
    seedsToMessages[trueSeed] = message

    passwordsToSeeds[userPass + str(trueSeed - 1)] = trueSeed + 1
    seedsToMessages[trueSeed + 1] = states['A']

    passwordsToSeeds[userPass + str(trueSeed - 2) + "1"] = trueSeed + 2
    seedsToMessages[trueSeed + 2] = states['B']

    passwordsToSeeds[userPass.lower()] = trueSeed + 3
    seedsToMessages[trueSeed + 3] = states['C']

    passwordsToSeeds[userPass.lower() + str(trueSeed + 1) + "3"] = trueSeed + 4
    seedsToMessages[trueSeed + 4] = states['D']

    passwordsToSeeds[userPass.upper()] = trueSeed + 5
    seedsToMessages[trueSeed + 5] = states['E']

    passwordsToSeeds[userPass.upper() + str(trueSeed + 2) + "5"] = trueSeed + 6
    seedsToMessages[trueSeed + 6] = states['F']

    passwordsToSeeds[userPass.lower()] = trueSeed + 7
    seedsToMessages[trueSeed + 7] = states['G']

    passwordsToSeeds[userPass.lower() + str(trueSeed + 5) + "3"] = trueSeed + 8
    seedsToMessages[trueSeed + 8] = states['H']

    passwordsToSeeds[userPass.upper()] = trueSeed + 9
    seedsToMessages[trueSeed + 9] = states['I']

    passwordsToSeeds[userPass.upper() + str(trueSeed + 7) + "5"] = trueSeed + 10
    seedsToMessages[trueSeed + 10] = states['J']

    # ENCRYPTION: c = sk XOR sm
    cipher = int(passwordsToSeeds[userPass]) ^ trueSeed

    # Shuffle the passwords and display them on the screen to begin the game
    passwords = list(passwordsToSeeds.keys())
    random.shuffle(passwords)                   # Shuffle the passwords
    print(passwords)                           # Display results

    # Prompt the user to crack this password
    try:
        query = input("Enter a password to crack: ")
        keySeed = passwordsToSeeds[query]
        # DECRYPTION: m = sk XOR c
        m = keySeed ^ cipher                        # ^ == XOR

        if m != trueSeed:                       # Honey checker
            print("Intruder! SOUNDING ALARM!")  # If seeds don’t match, this is an intruder

        # Check seeds
        print(seedsToMessages[m])
    except KeyError:
        print("Password not found or incorrect. ")

    # Prompt the user to try another password
    retry = input("Would you like to enter another inquiry (Y/N):  ")
    validate(retry)  # Validates input

    # Ends program by breaking out of the loop
    if retry == 'N' or retry == 'n':
        break

# Goodbye message
print("\nThank you for testing Honey Encryption")

'''
    DEBUGGING

    print(str(cipher) + "\n" +
          str(int(passwordsToSeeds[userPass])) + "\n" +
          str(trueSeed))
    print("\n" + str(m) + "\n" +
          str(keySeed) + "\n" +
          str(cipher))

    for x in seedsToMessages.keys():           # Display results
        print(str(x) + "\t" + str(seedsToMessages[x]))
'''
