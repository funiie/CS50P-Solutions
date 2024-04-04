
x, y, z = input("Fraction: ")

x = int(x)
y = "/"
z = int(z)

try:
    fuel = int(x) / int(z) * 100

    if fuel == 100:
        print("F")
    elif fuel <= 0:
        print("E")
    else:
        print(f"{fuel:.0f}%")


except (ZeroDivisionError, ValueError):
    pass
