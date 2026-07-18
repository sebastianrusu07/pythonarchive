names,orders = map(int,input().split())

initials = {}
for i in range(names):
    name = input()
    first,last = name.split()
    initial = first[0] + last[0]

    if initial not in initials:
        initials[initial] = name
    else:
        initials[initial] = "ambiguous"

for i in range(orders):
    initial = input()
    if initial not in initials:
        print("nobody")
    else:
        print(initials[initial])