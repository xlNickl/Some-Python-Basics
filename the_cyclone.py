#the_cyclone.py
H = int(input("Heigth: "))
C = int(input("Credits: "))

if H > 150 and C >= 5:
  print("Enjoy the ride!")
elif H < 150 and C >= 5:
  print("You are not tall enough to ride.")
elif H > 150 and C < 5:
  print("You don't have enough credits.")
elif H <= 150 and C < 5:
  print("You have not met either requirement.")
