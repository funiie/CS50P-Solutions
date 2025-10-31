# Convert emoticons :) and :( to emoji

def convert(text):
    # Replace :) with 🙂 and :( with 🙁 in the input text.
  
    # Replace happy face 
    text = text.replace(":)", "🙂")
    # Replace sad face
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("TYPE SOMETHING: ")
  
    # Convert emoticons to emoji and print
    print(convert(user_input))

# Call main when the program runs
if __name__ == "__main__":
    main()
