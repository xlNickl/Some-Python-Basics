#guess.py
guess = 0 
tries = 0

while guess != 6 and tries < 5:
  guess = int(input("Guess the number: "))
  tries += 1
if tries >= 5:
   print("You've reached the trying limit!")
elif guess == 6: 
  print ("Correct!")
  
  
   
