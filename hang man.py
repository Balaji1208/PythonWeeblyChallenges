import random # this part imports the "random" function
print('time to play hangman')
secret = random.choice([
   'tiger',
   'panda',
   'mouse',
   'elephant',
   'crocodile',
   'balaji',
   'parmesh',
   'ganesan',
   'gandhi',
   'rukumani',
   'penguin',
   'pelican',
   'leopard',
   'hamster',
   'saravanan',
   'triplets',
   'pythagoras',
   'dumbledore',
   'captain hook',
 ]) # this is where the random function is used to choose which word to play
guesses = 'aeiou' #this tells the variable "guesses" = my chosen letters

turns = 5         #this tells the computer that the player only has 5 turns

while turns > 0: #this is a loop function 

   missed = 0    #this tells the computer the player still has 5 turns
 

   for letter in secret: # this part tells the computer to print out any letters that are in the secret from variable "guesses"
    if letter in guesses:
      print (letter,end=" ")
    else:
        print ('_',end=" ")# here we see that if the player wrote the wrong letter the number of turns decreases
        missed += 1

   print

   if missed == 0: #here we are telling the computer what to do if he did the right letter
     print('You Win !!!!')
     break

   guess = input('guess a letter: ')#we are telling that the input by the user = "guess"
   guesses +=guess
      
   if guess not in secret:#here we are asking the computer to print part of the body every time the player gets the worng answer
      turns -= 1
      print ('Nope')
      print (turns, 'more turns')
      if turns < 5: print('  0  ') # here i have used a conditional statement
      if turns < 4: print('\_!_/') # the command compares the turns to the numbers
      if turns < 3: print('  !  ') # if the numbers are true than the program prints and adds to turns
      if turns < 2: print(' / \ ') # if it is false then turns still is the same
      if turns < 1: print('d   b')
      if turns == 0:
        print ('The answer is' , secret)



   
        while turns < 0:
           import random 
print('time to play hangman true ')
secret = random.choice([
   'tiger',
   'panda',
   'mouse',
   'elephant',
   'crocodile',
   'balaji',
   'parmesh',
   'ganesan',
   'gandhi',
   'rukumani',
   'penguin',
   'pelican',
   'leopard',
   'hamster',
   'saravanan',
   'triplets',
   'pythagoras',
   'dumbledore',
   'captain hook',
 ])
guesses = 'aeiou'

turns = 5

while turns > 0:

   missed = 0
 

   for letter in secret:
    if letter in guesses:
      print (letter,end=" ")
    else:
        print ('_',end=" ")
        missed += 1

   print

   if missed == 0:
     print('You Win !!!!')
     break

   guess = input('guess a letter: ')
   guesses +=guess
      
   if guess not in secret:
      turns -= 1
      print ('Nope')
      print (turns, 'more turns')
      if turns < 5: print('  0  ')
      if turns < 4: print('\_!_/')
      if turns < 3: print('  !  ')
      if turns < 2: print(' / \ ')
      if turns < 1: print('d   b')
      if turns == 0:
        print ('The answer is' , secret)

