class AC:
    def __init__(self, begin,end,power,cost):
        self.begin = begin
        self.end = end
        self.power = power
        self.cost = cost


if __name__ == "__main__":
    n,m = map(int,input().split())
    stalls = [0]*101
    for i in range(n):
        start,end,req = map(int,input().split())
        stalls[start:end+1] = [max(x,req) for x in stalls[start:end+1]]

    machines = []
    for i in range(m):
        b,e,p,c = map(int,input().split())
        aircon = AC(b, e, p, c)
        machines.append(aircon)

    optimal = float("inf")
    for mask in range(1 << m):
        outcome = stalls[:]
        totalCost = 0
        for machineIndex in range(m):
            if mask & (1 << machineIndex):
                aircon = machines[machineIndex]
                outcome[aircon.begin:aircon.end+1] = [x-aircon.power for x in outcome[aircon.begin:aircon.end+1]]
                totalCost += aircon.cost

        ok = True
        for stall in outcome:
            if stall > 0:
                ok = False
                break
        if ok:
            optimal = min(totalCost, optimal)
    print(optimal)






