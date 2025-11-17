
from datetime import date

halloween = date(2023, 10, 31)
day = halloween.day # 31
mon = halloween.month # 10
yr = halloween.year # 2023



from datetime import timedelta 

now = date.today() # 2023-09-16
one_day = timedelta(days=1)
tomorrow = now + one_day # 2023-09-17
day_1 = date(2023, 4, 6) # 2023-04-06
day_3 = day_1 + (3 * one_day)  # 2023-04-09



from datetime import time 
noon = time(12, 0, 0) # 12:00, hour, minute, second
a = noon.hour # 12
b = noon.minute # 0
c = noon.second # 0
d = noon.microsecond # 0



from datetime import datetime

something = datetime.strptime('10/31/23 13:23', '%m/%d/%y %H:%S') # give a string and the format it's in, "2023-10-31 13:00:23"
selse = something.strftime("%B %p") # October PM
sother = something.timetuple() # returns a struct_time
import time as ti
sother_secs = ti.mktime(sother) # convert struct_time to seconds since epoch
print('** *', sother_secs) 
print('* **', datetime.fromtimestamp(sother_secs)) # convert seconds since epoch to datetime, "2023-10-31 13:00:23"
seconds = 1536472051807 / 1000.0
dt = datetime.fromtimestamp(seconds).strftime('%Y-%m-%d %H:%M:%S.%f')
print('Datetime is:', dt)


e = datetime(2023, 9, 20, 12, 31, 0) # 2023-09-20 12:31:00
f = datetime.now() # 2023-09-16 00:17:847511
g = e.strftime("%B %X %p") # method for formatting date objects into readable strings, prints 'September 12:31:00 PM'
# %a	weekday, short. 'Wed'
# %A	weekda,y full. 'Wednesday
# %w	weekday as a number 0-6, 0 is Sunday
# %d	day of month 01-31
# %B	month, full. 'September'
# %m	month as a number, 01-12
# %y	year short, without century. 23
# %Y	year, full. 2023
# %H	hour 00-23
# %I	hour 00-12
# %p	AM/PM
# %M	minute, 00-59
# %S	second, 00-59
# %f	microsecond 000000-999999
# %z 	UTC offset. '+0100'
# %Z	Timezone, 'EST'
# %j	day number of year 001-366
# %U	weeknumber of year, Sunday as the first day of week, 00-53
# %W	weeknumbero fyear, Monday as first da of week 00-53
# %c	local version of date and time. 'Mon Dec 31 17:41:00 2023'
# %C	century, '20'
# %x	local version of date. '12/31/23'
# %X	local version of time. '17:41:00'
# %G	ISO 8601 year. '2018'
# %u	ISO 8601 weekday, 1-7
# %V	ISO 8601 weeknumber, 01-53



time_1 = time(12)
today_1 = date.today()
time_today = datetime.combine(today_1, time_1) # 2023-09-16 00:19:59.439077

date_1 = datetime.now() # 2023-09-16 00:23:27.757036
print(date_1.isoformat()) # 2023-09-16T00:29:18.575757
day_a = date_1.date()
time_a = date_1.time()
print(day_a) # split the date from datetime, '2023-09-16'
print(time_a) # split the time from datetime, '00:23:27.757036'




import time

### most commonly used functions of the time module
# time.time() # gives the seconds of the current local time since epoc
# time.sleep(<sec>) # delay in seconds
# time.ctime(<second since epoc>) # takes second since epoc or result of time() as an arg and returns a string of current local time, 'Sat Feb 29 15:24:32 2020'
# time.localtime() # returns a struct_time object with many attributes including: tm_year, tm_hour, tm_mday, tm_wday
# time.mktime(<struc_time>) # inveser of localtime(), takes a struct_time as an arg and returns time in seconds since epoc
# time.gmtime() # returns the current time in struct_time class in UTC
# time.strptime() # 
# time.strftime()
# time.asctime()
print(dir(time)) # print all methods in time module
curr_1 = time.time() # current time in seconds since epoc, '1694841474.869589'
curr_2 = time.ctime(1694841474.869589) # convert seconds since epoc into local time, 'Sat Sep 16 01:17:54 2023'
now_2 = time.localtime() # prints 'time.struct_time(tm_year=2023, tm_mon=9, tm_mday=16, tm_hour=1, tm_min=25, tm_sec=47, tm_wday=5, tm_yday=259, tm_isdst=1)'
print(now_2[0], now_2[2]) # prints '2023 16'
time.sleep(1) # sleep 1 second
print('sdf')




