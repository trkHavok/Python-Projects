import random

words = ['Anime','Basketball','Albany','Python']
randomWord = random.choice(words)
brokenWord = list(randomWord)
lettersUsed = []
amount_guess = 6


def convertWtoD(word):
    dashWord = ''
    for i in word:
     dashWord += '-'
    return dashWord

def swap(letter):
    global brokenWord
    global dashword
    dashword = list(dashword)
    for i in range(len(brokenWord)):
        if brokenWord[i] == letter:
            dashword[i] = letter
    return dashword

def randomLetter(letter, guess):
    global brokenWord
    global randomWord
    if letter in brokenWord:
        newdash = swap(letter)            
    print(newdash)

dashword = convertWtoD(brokenWord)
for i in range(amount_guess):
    print("***************************************************************** \n")
    print("The board looks like this:")    
    print(*dashword,'\n')
    print("Letter used so far:", *lettersUsed, sep=' ')

    guessedLorW = input("what letter (or enter your guess if you'd like to guess the word):")
    if guessedLorW not in lettersUsed:
        lettersUsed.append(guessedLorW)
    if guessedLorW in dashword:
        print("Sorry, you already used:",guessedLorW,"try again" )
    elif guessedLorW == randomWord:
        print("Correct!! the word now looks like:")
        print(randomWord)
        break
    elif guessedLorW in brokenWord:
        print("Correct!! the word now looks like:")
        randomLetter(guessedLorW, amount_guess)      
    if amount_guess != 0:
        amount_guess -= 1
        print("Nope, that letter(word) isn't in the word, try again. you have", amount_guess, "more tries")
        if amount_guess == 0:
            print("Sorry you are out of guess")
            print("The word was:",randomWord)
            break
            
        
