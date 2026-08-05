def twoFriendlyHorsesOnNSizedBoard(n):
    return (n**4-9*(n**2)+24*n-16)//2

k = int(input())

for i in range(1,k+1):
    print(twoFriendlyHorsesOnNSizedBoard(i))