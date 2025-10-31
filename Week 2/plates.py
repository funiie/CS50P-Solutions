#  Checks if a vanity plate is valid

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check for allowed characters only (letters or digits)
    if not s.isalnum():
        return False

    # Check numbers rules
    number_started = False
    for i, char in enumerate(s):
        if char.isdigit():
            # First number cannot be '0'
            if not number_started and char == "0":
                return False
            number_started = True
        elif number_started and char.isalpha():
            # Letter after number is not allowed
            return False

    return True


main()
