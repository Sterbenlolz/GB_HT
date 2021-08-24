time = int(input('Please input time in seconds:'))
days = time // (60 * 60 * 24)
hours = time // (60 * 60)
minutes = time // 60
seconds = time % 60
if time >= 60 * 60: minutes = (time % (60 * 60)) // 60
if time >= 60 * 60 * 24: hours = (time % (60 * 60 * 24)) // (60 * 60)
seconds_str = '{} seconds'.format(seconds)
minutes_str = '{} minutes'.format(minutes)
hours_str = '{} hours'.format(hours)
days_str = '{} days'.format(days)
if days % 10 == 1 and days != 11: days_str = '{} day'.format(days)
if hours % 10 == 1 and hours != 11: hours_str = '{} hour'.format(hours)
if minutes % 10 == 1 and minutes != 11: minutes_str = '{} minute'.format(minutes)
if seconds % 10 == 1 and seconds != 11: seconds_str = '{} second'.format(seconds)
time_list = [days_str, hours_str, minutes_str, seconds_str]
if days == 0: time_list.remove(days_str)
if hours == 0: time_list.remove(hours_str)
if minutes == 0: time_list.remove(minutes_str)
if seconds == 0: time_list.remove(seconds_str)
time_str = " ".join(time_list)
print(time_str)
