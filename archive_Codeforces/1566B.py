if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        line = input() + '1'
        print(min(line.count("01"),2))