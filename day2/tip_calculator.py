welcome = "Welcome to the tip calculator."
print(welcome)

total = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? "))
people = int(input("How many people to spilt the bill? "))

final = round((total + (total * (tip / 100))), 2)
split = round(final / people, 2)

message = f"The total is ${total}. With a {int(tip)}% tip it will be ${final}. Each person should pay ${split}"

print(message)