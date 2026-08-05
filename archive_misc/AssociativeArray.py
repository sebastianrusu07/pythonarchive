import sys

if __name__ == "__main__":
    dictionary = {}
    output = []

    skipFirst = True
    for lineIterator in sys.stdin:
        if skipFirst:
            skipFirst = False
            continue
        line = list(lineIterator.split())
        if line[0] == '0':
            dictionary[line[1]] = line[2]
        else:
            output.append(dictionary[line[1]] if line[1] in dictionary else 0)

print(*output,sep="\n")