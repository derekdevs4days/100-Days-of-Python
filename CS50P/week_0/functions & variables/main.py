# Ask user for their name
#name = input("What is your name? ")
name = "johnson ligma"

# How do you remove whitespace from str? Like trim() in JS
name = name.strip()

# Capitalize 
print(name.capitalize()) # This will capitalize only the first char
print(name.title()) # caps first char of every word
print(name.upper()) # caps all char of string

# Spliting name into first and last names
first, last = name.split(" ")

print(first)
print(last)
# Say hello to user
#print(f"Hello {name}")

#Rounding
x = float(input("What is X? "))
y = float(input("What is Y? "))

z = round(x / y, 2) #round with a second arguement is the number of decimals to use when rounding the number
print(z)