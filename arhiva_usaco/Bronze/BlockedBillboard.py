import sys

name = "billboard"
sys.stdin = open(f"{name}.in", "r")
sys.stdout = open(f"{name}.out", "w")

def area(board):
    return (board[1][0]-board[0][0]) * (board[1][1]-board[0][1])

def intersectionArea(board, cover):
    xOverlap = max(0, min(board[1][0],cover[1][0]) - max(board[0][0],cover[0][0]))
    yOverlap = max(0, min(board[1][1],cover[1][1]) - max(board[0][1],cover[0][1]))
    return xOverlap * yOverlap


if __name__ == "__main__":
    line1 = list(map(int,input().split()))
    board1 = (tuple(line1[:2]), tuple(line1[2:]))
    line2 = list(map(int, input().split()))
    board2 = (tuple(line2[:2]), tuple(line2[2:]))
    line3 = list(map(int, input().split()))
    cover = (tuple(line3[:2]), tuple(line3[2:]))

    totalArea = area(board1) + area(board2) - intersectionArea(board1, cover) - intersectionArea(board2, cover)
    print(totalArea)
