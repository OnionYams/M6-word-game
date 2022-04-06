#M6 python word game

import random

f = open("test_words.txt", "r")
wordList = f.read().split()

usedWords = []
wins = losses = 0
playGame = True

def runGame():
    # vars controlling the game
    numGuesses = 7
    # generate non used random word from list
    tempWord = wordList[random.randint(0,len(wordList)-1)]
    global usedWords
    while tempWord in usedWords:
        tempWord = wordList[random.randint(0,len(wordList)-1)]
    usedWords += tempWord
    # 2 versions for a workaround later
    realWord = remainWord = tempWord
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
            if numGuesses == 0:
                print("You lose. the word was" + realWord)
                global losses
                losses += 1
            continue
        # essentially "moves" letter from a duplicate of the true word to the answer so find can be used for repeated letters and 
        # doesn't always find the first match
        while remainWord.find(guess) != -1:
            answer = answer[:remainWord.find(guess)] + guess + answer[remainWord.find(guess)+1:]
            remainWord = remainWord[:remainWord.find(guess)] + "_" + remainWord[remainWord.find(guess)+1:]
        if answer == realWord:
            print("You win. The word was " + realWord)
            global wins 
            wins += 1
            break
        print(answer)

while(playGame):
    runGame()
    print(f"Wins: {wins}  Losses: {losses}")
    if input("Enter 'Y' to play again or any other input to exit the game: ").upper() == "Y":
        continue
    else:
        playGame = False
        print("Goodbye") 
        
f.close()
