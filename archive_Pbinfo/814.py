def triple(x):
    return x*3


[a,b] = input().split()
a=int(a)
b=int(b)

diff = triple(b) - a
print(diff)