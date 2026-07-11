health,arrows = map(int,input().split())

damages = []
line = input().split()
for arrowDmg in range(4):
    damages.append(int(line[arrowDmg]))

for shot in range(arrows):
    arrow = input()

    if arrow == 'standard':
        health -= damages[0]
    elif arrow == 'fire':
        health -= damages[1]
    elif arrow == 'ice':
        health -= damages[2]
    elif arrow == 'light':
        health -= damages[3]

print("dead" if health <= 0 else health)




