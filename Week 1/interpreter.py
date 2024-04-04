# format x y z to be in one line
x, y, z = input("Enter expression: ").split(" ")

# set x and z to floats
x = float(x)
z = float(z)

# perform calculation and print the result to one decimal point
if y == "+":
    sum = x + z
    print(f"{sum:.1f}")

elif y == "*":
    product = x * z
    print(f"{product:.1f}")

elif y == "/":
    division = x / z
    print(f"{division:.1f}")

elif y == "-":
    subtraction = x - z
    print(f"{subtraction:.1f}")
