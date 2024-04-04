def main():
    # asking for meal price and percent tip
    dollars = dollars_to_float(input("How much was your meal? "))
    percent = percent_to_float(input("What percent would you like to tip? "))
    # calculating tip and formatting it to 2 decimal point
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") 
    
# creating function to format price 
def dollars_to_float(dollars):
    dollar = float(dollars.strip().replace("$", " "))
    return dollar

# creating function to format percent    
def percent_to_float(percents): 
    percent = float(percents.strip().replace("%", " ")) / 100.0
    return percent

main() 
