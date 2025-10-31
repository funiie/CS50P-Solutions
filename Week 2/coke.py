# Simulates a Coke vending machine

amount_due = 50  # Coke costs 50 cents

while amount_due > 0:
    coin = int(input("Insert Coin: "))
    
    # Accept only 25, 10, or 5 cent coins
    if coin in [25, 10, 5]:
        amount_due -= coin
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
    else:
        # Ignore invalid coins
        continue

# If the user inserted more than 50 cents, calculate change
change = abs(amount_due)
print(f"Change Owed: {change}")
