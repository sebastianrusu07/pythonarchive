line = input().split()
inventory, items = int(line[0]), int(line[1])

original = []
for i in range(inventory):
    original.append(input())

current = []
for i in range(items):
    current.append(input())

position = {}
for i in range(len(current)):
    position[current[i]] = i + 1

for name in original:
    if name in position:
        print(position[name])
    else:
        print("stolen!")