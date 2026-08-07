if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))

    maximum = max(numbers)
    sumOfOthers = sum(numbers)-maximum
    output = 2*maximum if maximum > sumOfOthers else sumOfOthers+maximum
    print(output)