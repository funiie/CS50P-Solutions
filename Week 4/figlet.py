import sys
import pyfiglet
import random

def main():
    # Determine font
    if len(sys.argv) == 1:
        font = random.choice(pyfiglet.getFonts())
    elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in pyfiglet.getFonts():
            font = sys.argv[2]
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

    # Prompt for input
    text = input("Input: ")

    # Render and print ASCII art without extra newlines
    print(pyfiglet.figlet_format(text, font=font).rstrip())

if __name__ == "__main__":
    main()
