# Converts emoticons :) and :( to emoji

# Prompt the user for input
text = input("TYPE SOMETHING: ")

# Replace :) with 🙂 and :( with 🙁
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")

# Print the result
print(text)

