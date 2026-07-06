line = input().split()
green,red = int(line[0]),int(line[1])

maxHeal = 0
maxHeal += min(green,red) * 10
green -= min(green,red)
red -= min(green,red)

maxHeal += green//3 * 10
green%=3

maxHeal += green//2 * 3
green%=2

maxHeal += green

print(maxHeal)
