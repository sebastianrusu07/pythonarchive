string = input()

uniqueChars = []
good = True

for j in range(len(string)):
    if string[j] in uniqueChars:
        good = False
    else:
        uniqueChars.append(string[j])

print(int(good))