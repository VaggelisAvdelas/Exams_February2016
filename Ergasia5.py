def date(d, m, y):
    if m < 3:
        x = y-1
    else:
        x = y
#formula that calculates how many days to given date
    days = (23*m//9 + d + 4 + y + x//4 - x//100 + x//400)
    if m >= 3:
        days -= 2
    week_day = days % 7
    return week_day
    
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#input from user
given_date = str(raw_input("Give a date of this format dd/mm/yyyy(e.g.:05/09/2005):"))
d = int(given_date[:2])
m = int(given_date[3:5])
y = int(given_date[6:10])

week_day = days_of_week[date(d, m, y)-1]
print week_day
