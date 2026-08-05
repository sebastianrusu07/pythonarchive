def nextPermutation(stringBefore):
    string = list(stringBefore)
    pivot = len(string)-2
    while pivot >= 0 and string[pivot] >= string[pivot+1]:
        pivot -= 1

    if pivot <= -1:
        return None

    pos = len(string)-1
    while pos > pivot and string[pos] <= string[pivot]:
        pos -= 1
    string[pos],string[pivot] = string[pivot],string[pos]

    string[pivot+1:] = string[pivot+1:][::-1]

    return "".join(string)

stringS = input()
stringL = list(stringS)
stringL.sort()
string = "".join(stringL)

permutations = []
while string != None:
    permutations.append(string)
    string = nextPermutation(string)

print(len(permutations))
print(*permutations,sep='\n')