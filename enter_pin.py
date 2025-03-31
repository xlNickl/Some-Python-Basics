#enter_pin.py

print("***USER CONFIRMATION***\n")

pin = int(input("Enter Your Password: "))

while pin != 1234:
  pin = int(input("Incorrect PIN: Enter Your PIN Again: "))

if pin == 1234:
  (print("PIN Accepted!"))
