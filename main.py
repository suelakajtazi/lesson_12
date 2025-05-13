import datetime

time = datetime.datetime.now()

print(time)

print("year :", time.year)
print("month :", time.month)
print("day :", time.day)
print("hour :", time.hour)
print("minute :", time.minute)
print("second :", time.second)
print("microsecond :", time.microsecond)

current_datetime1 = datetime.datetime.now().date()
print(current_datetime1)
current_datetime2 = datetime.datetime.now().time()
print(current_datetime2)

tome_object = datetime.time(1 , 2, 3, 42434)
print(tome_object)

duration = datetime.timedelta(days = 3 , hours = 7)
print(duration)

new_date = time + duration
print(new_date)