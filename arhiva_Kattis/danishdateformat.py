months = [
    "januar",
    "februar",
    "marts",
    "april",
    "maj",
    "juni",
    "juli",
    "august",
    "september",
    "oktober",
    "november",
    "december"
]

date = input()
print(int(date[3:5]),'.',sep="",end=" ")
print(months[int(date[:2])-1],end=" ")
print(date[6:],end=" ")