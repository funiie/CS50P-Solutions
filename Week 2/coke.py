print("Amount due: 50")

# iitialisig values
coin = 0
total_due = 50
money = [5, 10, 25]

if coin == 50:
    print("Change Owed: 0")
    
# ask user input and do calculations
while coin < 50:
    coin = int(input("Insert coin: "))

    # if input is 5, 10 or 25
    if coin in money:
        total_due = total_due - coin
        print("Amount Due:", total_due)
    else:
        print("Amount Due:", total_due)

# clculate change
    if total_due <= 0:
        print("change Owed:", abs(total_due))
        break
