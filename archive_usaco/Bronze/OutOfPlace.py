import sys

name = "outofplace"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

if __name__ == "__main__":
    n = int(input())
    numbers = []

    for i in range(n):
        numbers.append(int(input()))

    sortedNumbers = sorted(numbers)

    left = 0
    while left < n and numbers[left] == sortedNumbers[left]:
        left += 1

    right = n - 1
    while right >= 0 and numbers[right] == sortedNumbers[right]:
        right -= 1

    swapsNeeded = set(numbers[left:right])
    print(len(swapsNeeded))