# A simple math interpreter

# Prompt the user for input
expression = input("Enter an expression (x y z): ").strip()

# Split the input into parts
x, op, z = expression.split()

# Convert numbers to integers
x = int(x)
z = int(z)

# Perform the calculation
if op == "+":
    result = x + z
elif op == "-":
    result = x - z
elif op == "*":
    result = x * z
elif op == "/":
    result = x / z

# Print the result formatted to one decimal place
print(f"{result:.1f}")
