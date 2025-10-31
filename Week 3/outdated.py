# Convert US-style dates to ISO 8601 (YYYY-MM-DD)

months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    date_input = input("Date: ").strip()

    # Try numeric format MM/DD/YYYY
    try:
        if "/" in date_input:
            parts = date_input.split("/")
            if len(parts) != 3:
                continue
            month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
    except ValueError:
        continue

    # Try written format Month D, YYYY
    try:
        if "," in date_input:
            month_day, year = date_input.split(",")
            year = int(year.strip())
            parts = month_day.strip().split()
            if len(parts) != 2:
                continue
            month_str, day = parts[0], int(parts[1])
            if month_str in months and 1 <= day <= 31:
                month = months.index(month_str) + 1
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
    except ValueError:
        continue
