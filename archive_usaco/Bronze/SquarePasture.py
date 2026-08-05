import sys

name = "square"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

if __name__ == "__main__":
    pasture1 = list(map(int, input().split()))
    pasture2 = list(map(int, input().split()))

    print(int(max(max(pasture2[2],pasture1[2]) - min(pasture1[0],pasture2[0]) , max(pasture2[3],pasture1[3])-min(pasture1[1],pasture2[1]))) ** 2)