import random
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d = (random.choice(list))
x = input("Pick a number One to Ten! ")
if x ==d:
  print("WINNER! (nice)")
else:
  print("You lost! the number was " + str( + d))
