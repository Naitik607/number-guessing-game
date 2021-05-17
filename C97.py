import random

number = random.randint(1,20)


name = "Number Guessing Game"
nm = "Guess a number between (1 and 20)"
chances = 0

print(name)
print(nm)

while chances < 5:
  chances += 1
 
  guess = int(input('Enter Your Guess:- '))
    
  if number == guess:
    print("Congratulation You Won")
    break    
  elif number < guess:
    print("Your Guess is too high,guess a number lower than",guess)
  elif number > guess:
    print("Your guess was too low,guess a number higher than",guess)
    

if not chances < 5:
  print("You lose,the number is ",number)