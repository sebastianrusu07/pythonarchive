line = input()
dir, code = line.split()

if dir == "D":
    i=0
    decoded = ""
    while i < len(code):
        decoded += code[i] * int(code[i+1])
        i+=2;
    print(decoded)
else:
    encoded = ""
    cnt = 1
    lastChar = code[0]
    i = 1
    while i < len(code):
        if code[i] == lastChar:
            cnt += 1
        else:
            encoded += lastChar
            encoded += str(cnt)
            lastChar = code[i]
            cnt=1
        i+=1
    encoded += lastChar
    encoded += str(cnt)
    print(encoded)