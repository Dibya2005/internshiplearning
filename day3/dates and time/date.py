import datetime
date=datetime.date(2025,1,2)
print(date)
date1=datetime.date.today()
print(date1)
time=datetime.time(12,30,00)
print(time)
now=datetime.datetime.now()
print(now)
now=now.strftime("%H :%M :%S %d-%m-%Y") #now formet specify
print(now)
target_datetime=datetime.datetime(2023,1,2,12,30,1)
current_datetime=datetime.datetime.now()
if target_datetime<current_datetime:
  print("target date has passed")
else:
  print("target date has not passed")
