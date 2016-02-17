import random
from random import shuffle
secretWord = [
    'red',
   'green',
   'purple',
   'mengenta',
   'black',
   'balaji',
   'lol',
   'this',
   'is',
   'ingigo',
   'violet',]


while True:
    word = random.choice(secretWord)
    secret = list(word)
    random.shuffle(secret)
    anagram = ''.join(secret)
    print("Word anagram:",anagram)
    choice=input("Guess the anagram pls:")
    if choice == word:
        print("correct")
    else:
        print("please try again")
        




