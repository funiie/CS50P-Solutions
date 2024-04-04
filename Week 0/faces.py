def convert():
    # prompt user to enter text
    text = str(input("Enter your text: "))
    # convert frown emoticon to emoji
    print(text.replace(":)", "🙂").replace(":(", "☹️" ))      
convert()     
