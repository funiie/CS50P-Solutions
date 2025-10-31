# Check if the user knows the Answer to the Great Question

# Ask the user for the answer
answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

# Clean up the input: remove extra spaces and ignore case
normalized = answer.strip().lower()

# Print Yes if the answer is 42 (as a number or word), otherwise No
if normalized == "42" or normalized == "forty-two" or normalized == "forty two":
    print("Yes")
else:
    print("No")

