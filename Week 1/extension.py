# prompting user to enter file name
ext = input("enter file name: ")

# describing extension
if ext [-4:] == ".gif":
    print("image/gif")
elif ext [-4:] == ".jpg":
    print("image/jpeg")
elif ext [-5:] == ".jpeg":
    print("image/jpeg")
elif ext [-4:] == ".png":
    print("image/png")
elif ext [-4:] == ".pdf" or ext [-4:] == ".PDF":
    print("application/pdf")
elif ext [-4:] == ".txt":
    print("text/plain")
elif ext [-4:] == ".zip":
    print("application/zip")
else:
    print("application/octet-stream")
