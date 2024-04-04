# prompts the user for greeting
greeting = input("greet someone: ")

# output $0 if greeting start with "hello"
if greeting [:5] =="Hello" or greeting [:5] =="hello":
    print("$0")

# output $20 if greeting starts with "h" but not "hello"
elif greeting [0] =="H" or greeting [0] =="h":
    print("$20")

# output $100 if neither
else:
    print("$100")
