import sys

name = "billboard"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

if __name__ == "__main__":
    bad = list(map(int, input().split()))
    good = list(map(int, input().split()))

    tarpNeeded = (bad[2]-bad[0]) * (bad[3]-bad[1])
    if bad[1] >= good[1] and bad[3] <= good[3]:
        if good[0] <= bad[0]:
            tarpNeeded -= (bad[3]-bad[1]) * (min(good[2], bad[2])-bad[0])
        else:
            tarpNeeded -= (bad[3]-bad[1]) * (bad[2]-max(good[0], bad[0]))
    elif good[0] <= bad[0] and good[2] >= bad[2]:
        if good[3] <= bad[3]:
            tarpNeeded -= (bad[2]-bad[0]) * (min(good[3], bad[3]) - bad[1])
        else:
            tarpNeeded -= (bad[2]-bad[0]) * (bad[3] - max(good[1], bad[1]))

    print(tarpNeeded)