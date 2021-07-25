import time
# epoch = a date and time from which a computer measures system time

print()
print( time.ctime(0)) # convert a time expressed in seconds since epoch to a readable string 
#                       epoch = when your computer thinks time began ( reference point )

print()
print(time.time())      # return current seconds since epoch 

print()
print(time.ctime(time.time()))  # now time 


print()
time_object = time.localtime()
print(time_object)


print()
local_time = time.strftime("%B %d %Y %H : %M : %S", time_object)        # show what we want to show
print(local_time)


print()
time_string = "20 April, 2020"
time_object2 = time.strptime(time_string , "%d %B, %Y")
print(time_object2)


print()
# (year , month , day , hours , minutes , secs , # day of the week , #day of the year , dst)
time_tuple = (2020 ,4 , 20 ,4, 20 , 0, 0, 0, 0)
time_string = time.asctime(time_tuple)
print(time_string)

time_tuple = (2020 ,4 , 20 ,4, 20 , 0, 0, 0, 0)
time_string = time.mktime(time_tuple)
print(time_string)






# date time practice 
import datetime


today = datetime.date.today()
print(today)                                    # today date

birthday = datetime.date(1999, 10, 11)          # set a date
print(birthday)

days_since_birth = today - birthday             # date can monus to find how many days
print(days_since_birth)

time_delt = datetime.timedelta(days = 10)       # if you want to forward or backward days use datetime.timedelta(days)

print(today - time_delt)
print(today + time_delt)


print(today.month)
print(today.day)
print(today.weekday())      # Monday =0,1,2,3,4,5,6 = Sunday


# time to set and show
print(datetime.time(7,8,8,52))                  # show the set Time
# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)

hour_delta = datetime.timedelta(hours= 30)
hours30_time = datetime.datetime.now() + hour_delta     # datetime.datetime.now() is now time
print(hours30_time)


# print(datetime.datetime.now(tz= pytz.UTC))  we dont have pytz



#string formatting with dates
# 2019-03-09 -> March 3, 2019
#strftime (f = formatting)
datetime_today = datetime.datetime.now()
print()
print("Change format:")
print(datetime_today.strftime('%B %d, %Y'))
print()

# March 09, 2019 -> datetime(2019,3,9)
#strptime (p = porsing) 
datetime_thing = datetime_today.strptime('March 09, 2019','%B %d, %Y')
print(repr(datetime_thing))


# Test the time to minus always use datetime.timedelta()
print(datetime.datetime.now()-datetime.timedelta(minutes= 15))