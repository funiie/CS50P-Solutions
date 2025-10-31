# Decides how much Kramer gets based on his greeting

# Ask the user for a greeting
greeting = input("Greeting: ")

# Clean up input: remove leading spaces and ignore case
cleaned = greeting.lstrip().lower()

# Decide the payout 
if len(cleaned) >= 5 and cleaned[0:5] == "hello":
    print("$0")
elif len(cleaned) >= 1 and cleaned[0] == "h":
    print("$20")
else:
    print("$100")
