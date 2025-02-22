import datetime

year_1 = int(input("Input ur year: "))
month_1 = int(input("input ur month: "))
day_1 = int(input("Input ur day: "))
hour_1 = int(input("Input ur hour: "))
min_1 = int(input("Input ur minute: "))
sec_1 = int(input("Input ur second: "))


year_2 = int(input("Input ur year: "))
month_2 = int(input("input ur month: "))
day_2 = int(input("Input ur day: "))
hour_2 = int(input("Input ur hour: "))
min_2 = int(input("Input ur minute: "))
sec_2 = int(input("Input ur second: "))


time1 = datetime.datetime(year_1, month_1, day_1, hour_1, min_1, sec_1 )
time2 = datetime.datetime(year_2, month_2, day_2, hour_2, min_2, sec_2)

time_diff = abs(time1 - time2)

print(time_diff.total_seconds())