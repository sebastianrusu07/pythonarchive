def winner(one,two):
    if one==two:
        return 0

    if (one == 'R' and two == 'S') or (one == 'S' and two == 'P') or (one == 'P' and two == 'R'):
        return 1

    return 2

player1 = input()
player2 = input()

while player1 != "E" and player2 != "E":
    player1Score = 0
    player2Score = 0

    for i in range(len(player1)):
        res = winner(player1[i],player2[i])
        if res == 1:
            player1Score += 1
        elif res == 2:
            player2Score += 1

    print("P1: {}\nP2: {}".format(player1Score,player2Score)) #first time ever using format and half of it got auto completed
    player1 = input()
    player2 = input()

