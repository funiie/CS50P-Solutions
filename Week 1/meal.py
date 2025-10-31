# Tells you if it's time for breakfast, lunch, or dinner

def main():
    # Ask the user for a time
    time_str = input("What time is it? ").strip()
    
    # Convert input to float hours
    time = convert(time_str)
    
    # Check meal times
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time_str):
    # Split the time into hours and minutes
    hours, minutes = time_str.split(":")
    hours = int(hours)
    minutes = int(minutes)
    
    # Convert minutes to fraction of an hour
    return hours + minutes / 60

if __name__ == "__main__":
    main()
