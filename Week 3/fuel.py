
#  Outputs fuel level as a percentage or E/F

while True:
    fraction = input("Fraction: ").strip()  # Prompt user for input
    try:
        # Split input into numerator and denominator
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)

        # Validate fraction
        if y == 0 or x < 0 or y < 0 or x > y:
            continue

        percent = round((x / y) * 100)  # Convert fraction to percentage

        # Output based on percentage
        if percent <= 1:
            print("E")
        elif percent >= 99:
            print("F")
        else:
            print(f"{percent}%")
        break  # Exit loop after valid input and output

    except (ValueError, ZeroDivisionError):
        continue  # Prompt user again on invalid input
