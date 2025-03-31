#The_Sorting_Hat.py

G= 0
S= 0
R= 0
H= 0

q1 = int(input("Q1) Do you like Dawn or Dusk?\n 1) Dawn\n 2) Dusk\n Answer: "))
if q1 == 1: 
 G += 1
 R += 1
elif q1 == 2:
  H += 1
  S += 1  
else:
 print("Wrong Input.")

q2 = int(input("Q2) When I'm dead, I want to people to remember me as:\n 1) The Good\n 2) The Great\n 3) The Wise\n 4) The Bold\n Answer: "))
if q2 == 1:
  H += 2
elif q2 == 2:
  S += 2
elif q2 == 3:
  R += 2
elif q2 == 4:
  G += 2
else:
 print("Wrong Input.")

q3 = int(input("Q3) Which kinf of instrument most pleases your ear? \n 1) The violin\n 2) The trumpet\n 3) The piano\n 4) The drum\n Answer: "))
 
if q3 == 1:
  S += 4
elif q3 == 2:
  H += 4
elif q3 == 3:
  R += 4
elif q3 == 4:
  G += 4
else:
  print("Wrong Input.") 

print('\nGryffindor House Point:', G)

print("\nSlytherin House Point: ", S)

print("\nRavenclaw House Point: ", R)

print("\nHufflepuff House Point: ", H)

if G >= S and G >= R and G >= H:
 print("\nYour House is 🦁 Gryffindor!!")
elif S >= R and S >= H:
  print("\nYour House is 🐍 Slytherin!")
elif R >= H:
  print("\nYour House is 🦅 Ravenclaw!")
else:
  print("\nYour House is 🦡 Hufflepuff!")
