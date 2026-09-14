def CifMax(nr):
    maxim = 0
    while nr>0:
        c = int(nr%10)
        maxim = max(maxim, c)
        nr /= 10
    return maxim