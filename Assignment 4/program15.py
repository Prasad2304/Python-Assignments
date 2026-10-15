import re
from datetime import datetime

# Accept a block of text from the user
text = input("Enter a block of text: ")

# Regular expression patterns for different date formats
patterns = [
    r'\b\d{2}/\d{2}/\d{4}\b',                  # DD/MM/YYYY
    r'\b\d{2}-\d{2}-\d{4}\b',                  # MM-DD-YYYY
    r'\b\d{4}\.\d{2}\.\d{2}\b',                # YYYY.MM.DD
    r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)'
    r'\s+\d{1,2},\s+\d{4}\b'                   # Month Day, Year
]

# Extract dates
dates = []

for pattern in patterns:
    dates.extend(re.findall(pattern, text))

# Convert dates to YYYY-MM-DD format
converted_dates = []

for date in dates:
    try:
        if "/" in date:
            new_date = datetime.strptime(date, "%d/%m/%Y")

        elif "-" in date:
            new_date = datetime.strptime(date, "%m-%d-%Y")

        elif "." in date:
            new_date = datetime.strptime(date, "%Y.%m.%d")

        else:
            new_date = datetime.strptime(date, "%B %d, %Y")

        converted_dates.append(new_date.strftime("%Y-%m-%d"))

    except ValueError:
        pass

# Display results
print("\nExtracted Dates:")
print(dates)

print("\nConverted Dates:")
print(converted_dates)