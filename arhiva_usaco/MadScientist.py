import sys

fin = "breedflip.in"
fout = "breedflip.out"

sys.stdin = open(fin, "r")
sys.stdout = open(fout, "w")

length = int(input())

got = input()
need = input()

i = 0
substrings = 0
while i < length:
    if got[i] != need[i]:
        substrings += 1
        while got[i] != need[i]:
            i+=1
        i-=1
    i+=1

print(substrings)