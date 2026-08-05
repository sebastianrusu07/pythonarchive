navi = input()

repaired = ""
for i in range(int(len(navi))):
    if navi[i]=='B':
        repaired += "(ooo)"
    else:
        repaired += navi[i]

print(repaired)