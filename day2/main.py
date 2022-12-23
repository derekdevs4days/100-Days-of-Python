#num_char = len (input("What is your name?"))
#print("Your name has " + str(num_char) + " characters.")

# num = "69"
# (int(num))
"""
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.

Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

input: 56
output: "You have 12410 days, 1768 weeks, and 408 months left."
"""
age = input("What is your current age? ")

left = 90 - int(age)
days = left * 365
weeks = left * 52
months = left * 12

print ( f"You have {days} days, {weeks} weeks, and {months} months left.")