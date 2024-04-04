
def main():
    # prompt user to input time
    time = input("What time is it? ")
    time = convert(time)

    # if statements
    if time >= 7 and time <= 8:
        print("breakfast time")

    if time >= 12 and time <= 13:
       print("lunch time")

    if time >= 18 and time <= 19:
        print("dinner time")

# function to convert str time to int and format time
def convert(time):
    hours, minutes = time.split(":")
    hrs = float(hours)
    mins = float(minutes) / 60
    return float(hrs) + mins

main()

