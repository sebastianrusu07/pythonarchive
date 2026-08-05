def ctoi(c):
    if c==' ':
        return 0

    return ord(c)-ord('a')+1

def itoc(i):
    if i==0:
        return " "

    return chr(ord('a')+i-1)


def encrypt(seq):
    encrypted = list(map(ctoi, list(seq)))

    sum = encrypted[0]
    for i in range(1, len(seq)):
        sum += encrypted[i]
        encrypted[i] = sum % 27

    encrypted = list(map(itoc, encrypted))
    s = "".join(encrypted)

    return s

def decrypt(seq):
    decrypted = list(map(ctoi, list(seq)))
    decryptedCopy = decrypted.copy()

    for i in range(1, len(seq)):
        decrypted[i] = (decryptedCopy[i]-decryptedCopy[i-1]+27)%27

    decrypted = list(map(itoc, decrypted))
    s = "".join(decrypted)

    return s


n = int(input())

for i in range(n):
    line = input()
    dir = line[0]
    seq = line[2:]

    print(encrypt(seq) if dir=="e" else decrypt(seq))
