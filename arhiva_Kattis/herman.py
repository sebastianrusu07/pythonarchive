import math

radius = int(input())

areaEuclidean = float(math.pi * (radius ** 2))
areaTaxi = float(((radius*2) * radius))

print("{:.7f}\n{:.7f}".format(areaEuclidean, areaTaxi))