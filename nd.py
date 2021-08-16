day=int(input("Enter date "))
month=int(input("Enter month "))
year=int(input("Enter year "))
next_month=month
next_year=year
invalid=False
def checkmonth(d,m):
    if((month==4 or month==6 or month==9 or month==11) and day==31):
        return True
    else:
        return False
def isleap(year):
    if((year%4==0 and year%100!=0) or year%400==0):
        return True
    else:
        return False
if(day<1 or day>31):
    invalid=True
    print("date not in range 1-31")
elif(month<1 or month>12):
    invalid=True
    print("month not in range 1-12")
elif(checkmonth(day,month)):
    invalid=True
    print("month ",month," cannot have ",day)
elif(year<1812 or year>2013):
    invalid=True
    print("year not in range 1812-2013")
elif(month==2):
    if(isleap(year) and day>29):
        invalid=True
        print("Leap year cannot have date greater than 29 in february")
if(invalid==False):
    if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10):
        if(day<31):
            next_day=day+1
        else:
            next_day=1
            next_month=month+1
    elif(month==4 or month==6 or month==9 or month==11):
        if(day<30):
            next_day=day+1
        else:
            next_month=month+1
            next_day=1
    elif(month==2):
        if(day<28):
            next_day=day+1
        elif(isleap(year) and day==28):
            next_day=day+1
        elif(day==28 or day==29):
            next_day=1
            next_month=3
        elif(day>29):
            invalid=True
            print("Febrauary cannot have ",day)
    elif(month==12):
        if(day<31):
            next_day=day+1
        else:
            next_day=next_month=1
            if(year==2013):
                print("next day is out of range")
                invalid=True
            else:
                next_year=year+1
if(not invalid):
    print("next date is dd/mm/yyyy:",next_day,"/",next_month,"/",next_year)