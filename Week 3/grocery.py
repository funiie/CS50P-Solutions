#  Track grocery items and their counts

items = {}  # Dictionary to store items and their counts

try:
    while True:
        item = input("Item: ").lower()  # Convert input to lowercase for case-insensitive counting
        if item in items:
            items[item] += 1
        else:
            items[item] = 1
except EOFError:
    pass  # End input when user presses Control-D

# Sort items alphabetically and print counts in uppercase
for item in sorted(items):
    print(f"{items[item]} {item.upper()}")
