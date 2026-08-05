m,t = map(int,input().split())

monday = list(map(int,input().split()))
tuesday = list(map(int,input().split()))

tuesday_set = set(tuesday)
monday_set = set(monday)

only_monday = [x for x in monday if x not in tuesday_set]
only_tuesday = [x for x in tuesday if x not in monday_set]

print(*only_monday)
print(*only_tuesday)