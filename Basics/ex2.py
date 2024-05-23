import time

# Define a specific hour (noon) for comparison
noon = time.strptime('12:00:00', '%H:%M:%S')

# Get current time in a similar format
current_time = time.localtime()

# Compare hours and minutes to determine morning or afternoon
if (current_time.tm_hour < noon.tm_hour) or (current_time.tm_hour == noon.tm_hour and current_time.tm_min < noon.tm_min):
    print("good morning")
else:
    print("good afternoon")
