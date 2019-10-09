import datetime

date = datetime.datetime.today()

hour = date.strftime("%H")
minute = date.strftime("%M")
print(hour, minute)