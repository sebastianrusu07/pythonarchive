city = input()
maxPlasticPerc = float(input())
composition = int(input())

notPlastic = 0
total = 0
for i in range(composition):
    item = input()
    if item == "ekki plast":
        notPlastic += 1
    total += 1

perc = notPlastic / total

print("Neibb" if perc > maxPlasticPerc else "Jebb")
