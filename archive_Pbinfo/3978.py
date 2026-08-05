def gauss(a,b):
    sumA = (a-1)*a/2
    sumB = b*(b+1)/2
    return int(sumB-sumA)

[a,b,c] = input().split()

a=int(a)
b=int(b)
c=int(c)

print(gauss(a,b),gauss(b,c),gauss(a,c),sep=" ")

