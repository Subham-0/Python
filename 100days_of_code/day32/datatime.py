import datetime as dt 
 
now = dt.datetime.now()
print(now)
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

data_of_birth = dt.datetime(year=2001,month=1,day=1,hour=6)
print(data_of_birth)