import datetime as dt

def subtr5days(date_s):
    date = dt.datetime.strptime(date_s, '%d.%m.%Y')
    return date - dt.timedelta(days=5)

def near_time():
    t = dt.datetime.now()
    day1 = dt.timedelta(days=1)
    y = t - day1
    tm = t + day1
    print("Yesterday was {}".format(y.date()),
    "Today is {}".format(t.date()),
    "Tomorrow will be {}".format(tm.date()),
    sep='\n', end='\n\n')

def drop_msec(date):
    return date - dt.timedelta(microseconds=date.microsecond)

def sec_diff(date1, date2):
    if date1 > date2:
        a, b = date1, date2
    else:
        a,b = date2, date1
    return (a-b).total_seconds()

current_date = '05.01.2023' # input("Your date (dd.mm.YY): ")
print(f"{current_date} - 5 days =", subtr5days(current_date).strftime('%d.%m.%Y'), '\n')
near_time()
print(drop_msec(dt.datetime.now()))
print(sec_diff(dt.datetime.now(), dt.datetime.now() + dt.timedelta(minutes=1, seconds=30)))