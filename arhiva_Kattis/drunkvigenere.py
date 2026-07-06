encrypted = input()
key = input()

decrypted = ""
for i in range(len(encrypted)):
    e = ord(encrypted[i]) - ord('A')
    k = ord(key[i]) - ord('A')
    if i%2 == 0:
        decrypted += chr((e - k)%26 + ord('A'))
    else:
        decrypted += chr((e + k)%26 + ord('A'))

print(decrypted)