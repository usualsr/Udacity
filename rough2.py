def delta_days(day):
    week=day//7
    days=day%7
    print(str('the {} week and {} days').format(week,days))   ##  .. is very important
delta_days(11)