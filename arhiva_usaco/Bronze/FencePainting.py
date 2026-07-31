import sys

name = "paint"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")


a,b = map(int,input().split())
c,d = map(int,input().split())

paintedByJohn = set(range(a,b))
paintedByBessie = set(range(c,d))

totalPainted = paintedByJohn | paintedByBessie
print(len(totalPainted))