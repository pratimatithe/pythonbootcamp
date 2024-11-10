import random
from colorama import Fore, Back

list_of_words = [
    "water",
    "ditto",
    "video",
    "audio",
    "witch",
    "magic",
    "prime",
]

answer = random.choice(list_of_words)

print(answer)

attemptsRemaining = 6
endOfGame = False

while not endOfGame and attemptsRemaining > 0:
    user = input("Guess your word: ").lower()

    correct_guesses = ""
    partially_correct_guesses = ""

    for i in range(len(user)):
        if user[i] == answer[i]:
            correct_guesses += Fore.GREEN + user[i]
        elif user[i] in answer:
            partially_correct_guesses += Fore.YELLOW + user[i]
        else:
            partially_correct_guesses += Fore.RED + user[i]
            attemptsRemaining -= 1

    print(correct_guesses + partially_correct_guesses)

    if user == answer:
        print(Fore.GREEN + "Congratulations! You guessed the word!")
        endOfGame = True
    elif attemptsRemaining == 0:
        print(Fore.RED + "Sorry, you ran out of attempts. The word was:", answer)
        endOfGame = True

print("Hello World")
print("Hello this is the demonstration of changing the branch so gotta edit it")
