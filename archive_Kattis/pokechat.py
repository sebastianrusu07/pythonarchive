encoded = input()
key = input()

decoded = []
for i in range(int(len(key)/3)):
    segment = key[i*3:(i+1)*3]
    intSegment = int(segment)-1
    decoded.append(encoded[intSegment])

print("".join(decoded)) #neat trick