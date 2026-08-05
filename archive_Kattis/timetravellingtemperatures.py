import sys
x,y = map(int, input().split())

if y == 1 and x != 0:
    print("IMPOSSIBLE")
    sys.exit()

if y == 1 and x == 0:
    print("ALL GOOD")
    sys.exit()

print(f"{x/(1-y):.7f}")


