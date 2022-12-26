"""
if condition:
  do this
elif condition:
  do this
else:
  do this
"""
height = float(input("What is your height in cm? "))

if height > 120:
  print("You can ride")
  age = int(input("How old are you? "))
  if age > 18:
    print("Your ticket will be $12")
  elif age >= 12:
    print("Your ticket will be $7")
  else:
    print("Your ticket will be $5")
else:
  print("Not tall enough")