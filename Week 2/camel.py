# Converts camelCase variable names to snake_case

# Prompt the user for a camelCase variable name
camel = input("Enter a camelCase variable name: ").strip()

# Initialize an empty string for the snake_case result
snake = ""

# Loop through each character in the input
for char in camel:
    if char.isupper():
        # If the character is uppercase, add '_' and the lowercase version
        snake += "_" + char.lower()
    else:
        # Otherwise, just add the character
        snake += char

# Output the snake_case variable name
print(snake)
