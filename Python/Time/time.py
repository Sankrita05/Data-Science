import time

# Get the current local time
current_time = time.localtime()
print(current_time, "\n")

# Format the time as YYYY-MM-DD HH:MM:SS
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
print(formatted_time, "\n")

# Format the time as DD-MM-YYYY HH:MM
formatted_time = time.strftime("%d-%m-%Y %H:%M", current_time)
print(formatted_time, "\n")

# Function to get the day suffix
def get_day_suffix(day):
    if 10 <= day % 100 <= 20:
        return "th"
    else:
        suffixes = {1: "st", 2: "nd", 3: "rd"}
        return suffixes.get(day % 10, "th")

# Format the time as "07th March 2024, 03:50 PM"
formatted_time = time.strftime(f"%d{get_day_suffix(current_time.tm_mday)} %B %Y, %I:%M %p", current_time)
print(formatted_time, "\n")
