# Simple tip calculator

def main():
    # Prompt user for meal cost and tip percentage
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate tip
    tip = dollars * percent
    
    # Print tip formatted to 2 decimal places
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Convert a string like "$50.00" to float 50.0
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Convert a string like "15%" to float 0.15
    return float(p.replace("%", "")) / 100


# Run the program
main()

