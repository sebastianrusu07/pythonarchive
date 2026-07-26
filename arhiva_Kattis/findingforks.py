n = int(input())
numbers = list(map(int, input().split()))

smallest = float("inf")
secondSmallest = float("inf")
for number in numbers:
    if number <= smallest:
        secondSmallest = smallest
        smallest = number
    elif number < secondSmallest:
        secondSmallest = number

print(int(smallest+secondSmallest))