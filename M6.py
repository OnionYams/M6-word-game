#M6 python word game

import random

#global vars controlling the game
numGuesses = 7
# 2 versions for a workaround later
realWord = remainWord = "chippy"
answer = ""
for i in range(len(remainWord)):
    answer += "_"
letters = []

while (numGuesses > 0):
    guess = str(input("Guess a letter: "))
    # validate input
    if not guess.isalpha():
        print("Must enter a letter or word")
        continue
    if guess in letters:
        print("Already guessed that")
        continue
    guess = guess.lower()
    if remainWord.find(guess) == -1:
        numGuesses -= 1
        print("Incorrect, remaining guesses: " + str(numGuesses))
        continue
    # essentially "moves" letter from a duplicate of the true word to the answer so find can be used for repeated letters and 
    # doesn't always find the first match
    while remainWord.find(guess) != -1:
        answer = answer[:remainWord.find(guess)] + guess + answer[remainWord.find(guess)+1:]
        remainWord = remainWord[:remainWord.find(guess)] + "_" + remainWord[remainWord.find(guess)+1:]
    if answer == realWord:
        print("You win. The word was " + realWord)
        break
    print(answer)

