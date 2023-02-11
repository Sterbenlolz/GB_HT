time = int(input('Please input time in seconds:'))
days = time // (60 * 60 * 24)
hours = time // (60 * 60)
minutes = time // 60
seconds = time % 60
if time >= 60 * 60:
    minutes = (time % (60 * 60)) // 60
if time >= 60 * 60 * 24:
    hours = (time % (60 * 60 * 24)) // (60 * 60)
seconds_str = f'{seconds} seconds'
minutes_str = f'{minutes} minutes'
hours_str = f'{hours} hours'
days_str = f'{days} days'
if days % 10 == 1 and days != 11:
    days_str = f'{days} day'
if hours % 10 == 1 and hours != 11:
    hours_str = f'{hours} hour'
if minutes % 10 == 1 and minutes != 11:
    minutes_str = f'{minutes} minute'
if seconds % 10 == 1 and seconds != 11:
    seconds_str = f'{seconds} second'
time_list = [days_str, hours_str, minutes_str, seconds_str]
if days == 0:
    time_list.remove(days_str)
if hours == 0:
    time_list.remove(hours_str)
if minutes == 0:
    time_list.remove(minutes_str)
if seconds == 0:
    time_list.remove(seconds_str)
TIME_STR = " ".join(time_list)
print(TIME_STR)
