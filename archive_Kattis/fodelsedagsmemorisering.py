birthdaysToAttend = {}
priorityOfPerson = {}

people = int(input())
for i in range(people):
    name,priority,date = input().split()
    priority = int(priority)

    priorityOfPerson[name] = priority

    if date not in birthdaysToAttend:
        birthdaysToAttend[date] = name
        priorityOfPerson[name] = priority
    elif priorityOfPerson[birthdaysToAttend[date]] < priority:
        birthdaysToAttend[date] = name
        priorityOfPerson[name] = priority


print(len(birthdaysToAttend))
sortingList = []
for entry in birthdaysToAttend:
    sortingList.append(birthdaysToAttend[entry])

sortingList.sort()
for name in sortingList:
    print(name)






