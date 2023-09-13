from datetime import datetime, timedelta

# Write a Python program to add 5 seconds to the current time.

now = datetime.now()
plus_5seconds = now + timedelta(seconds = 5)

print('Current time:', now.time(), '\nAfter adding 5 seconds:', plus_5seconds.time())





# reform = now.strftime('%H:%M:%S.%f')
# reform_5second = now.strftime('%H:%M:%S.%f')