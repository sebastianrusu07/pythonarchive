import sys

def cons(a,b,c):
    if b==a+1 and c==b+1:
        return True
    return False

name = "herding"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")


a,b,c = map(int,input().split())
a,b,c = sorted([a,b,c])

if cons(a,b,c):
    print(0,0,sep="\n")
    sys.exit()

minimum = 1 if abs(a-b)==2 or abs(b-c)==2 else 2
maximum = max(abs(a-b),abs(b-c))-1

print(minimum,maximum,sep="\n")