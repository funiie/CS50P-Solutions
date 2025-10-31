# Simple program to show file media type

# Ask the user for a filename
filename = input("Enter the file name: ").strip().lower()

# Get the part after the last dot
parts = filename.split(".")
ext = parts[-1] if len(parts) > 1 else ""

# Check the last 3 characters for jpg/jpeg
last3 = ext[-3:] if len(ext) >= 3 else ext

# Decide and print media type
if ext == "gif":
    print("image/gif")
elif last3 == "jpg" or ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
