def SumCif(nr):
    sum = 0
    while nr>0:
        sum = sum + nr%10
        nr=nr//10
    return sum

num = int(input())
print(SumCif(num))