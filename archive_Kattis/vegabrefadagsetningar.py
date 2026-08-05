passport = input().split()

months = [
    "JAN",
    "FEB",
    "MAR",
    "APR",
    "MAY",
    "JUN",
    "JUL",
    "AUG",
    "SEP",
    "OCT",
    "NOV",
    "DEC",
]

day,junk,month,year =  passport[0],passport[1],passport[2],passport[3]

intDay = int(day)
intMonth = months.index(month[1:])+1
intYear = int("20"+year)

outputMonth = intMonth
if(intMonth<10):
    outputMonth = "0"+str(intMonth)

print(intYear,outputMonth,day,sep="-")

#This code is garbage, but I can't be bothered.