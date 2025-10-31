# Felipe's Taqueria order calculator

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0.0  # Keep track of total cost

try:
    while True:
        item = input("Item: ").title()  # Convert input to title case
        if item in menu:  # Check if item is on the menu
            total += menu[item]
            print(f"Total: ${total:.2f}")
        # Ignore invalid items
except EOFError:
    pass  # End input when user presses Control-D
