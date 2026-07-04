bigDiam = int(input())
smallDiam = int(input())

smallCnt = int(input())

pi = 3.14159265358979323846
bigArea = (bigDiam/2) ** 2 * pi
smallArea = (smallDiam/2) ** 2 * pi

print("Jebb" if bigArea <= smallArea*smallCnt else "Neibb")