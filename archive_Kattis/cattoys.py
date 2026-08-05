inputs = input().split()

days = int(inputs[0])
lostPerDay = int(inputs[1])

fullDays = days/lostPerDay
partialDay = days%lostPerDay!=0

print(int(fullDays + partialDay))