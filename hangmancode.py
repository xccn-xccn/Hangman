import random
from order import order
def show():
    pos = []
    for i,char in enumerate(word):
        if char == guess:
            pos.append(i)
    return pos

def plural(num):
    return "guess" if num == 1 else "guesses"

guessed = []
words = ['left', 'late', 'run','while', 'press', 'close', 'night', 'real', 'life', 'few', 'north', 'open', 'seem', 'together', 'next', 'white', 'children', 'begin', 'got', 'walk', 'example', 'ease', 'paper', 'group', 'always', 'music', 'those', 'both', 'mark', 'often', 'letter', 'until', 'mile', 'river', 'car', 'feet', 'care', 'second', 'book', 'carry', 'took', 'science', 'eat', 'room', 'friend', 'began', 'idea', 'fish', 'mountain', 'stop', 'once', 'base', 'hear', 'horse', 'cut', 'sure', 'watch', 'color', 'face', 'wood', 'main', 'enough', 'plain', 'girl', 'usual', 'young', 'ready', 'above', 'ever', 'red', 'list', 'though', 'feel', 'talk', 'bird', 'soon', 'body', 'dog', 'family', 'direct', 'pose', 'leave', 'song', 'measure', 'door', 'product', 'black', 'short', 'numeral', 'class', 'wind', 'question', 'happen', 'complete', 'ship', 'area', 'half', 'rock', 'order', 'fire', 'south', 'problem', 'piece', 'told', 'knew', 'pass', 'since', 'top', 'whole', 'king', 'space', 'heard', 'best', 'hour', 'better', 'true', 'during', 'hundred', 'five', 'remember', 'step', 'early', 'hold', 'west', 'ground', 'interest', 'reach', 'fast', 'verb', 'sing', 'listen']
word = random.choice(words)
#print(word)
guess_count,incorrect_count,invalid_count,repeat_count = 0,0,0,0
found = False
shown = ["_"]*len(word)
while not found:
    print(order[incorrect_count],"enter your character",shown,"You have already guessed",", ".join(guessed))
    guess_count += 1
    guess = input().lower()
    if len(guess) != 1 or (not guess.isalpha() and guess != "'"):
        print("enter a valid guess ")
        invalid_count += 1
        continue
    elif guess in guessed:
        print("that was a repeat guess")
        repeat_count += 1
        continue
    elif guess in word:
        print("your guess was in the word")
        for index in show():
            shown[index] = guess
    else:
        incorrect_count += 1
        print("your guess was not in the word")
    guessed.append(guess)
    if "".join(shown) == word:
        print(f"You win! The word was {word} you took {guess_count} {plural(guess_count)} ,had {invalid_count} invalid {plural(invalid_count)} and {repeat_count} repeat {plural(repeat_count)}")
        found = True
    elif incorrect_count > len(order) -1:
        print("Damn your trash .You lose the word was",word)
        break
        





