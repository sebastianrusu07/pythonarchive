def nextCollatz(number):
    return number//2 if number%2==0 else number*3+1

nr = int(input())
print(nr,end=" ")
while nr > 1:
    nr = nextCollatz(nr)
    print(nr,end=" ")