import sys

name = "pails"

sys.stdin = open("{}.in".format(name), "r")
sys.stdout = open("{}.out".format(name), "w")


small,big,maximum=map(int,input().split())

maximumBigs = maximum//big

maximumPossible = -1
for i in range(maximumBigs+1):
    fromBigs = i*big
    rem = maximum-fromBigs
    maximumSmalls = rem//small
    fromSmalls = maximumSmalls*small
    possible = fromBigs+fromSmalls
    maximumPossible = max(possible,maximumPossible)

print(maximumPossible)