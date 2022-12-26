def main():
    name = input("What is your name? ")
    hello(name)

# def is short for define. use to crate function
def hello(to="Stranger"):
    print("Hello " + to)

main()