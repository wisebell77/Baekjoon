import sys

input = sys.stdin.readline

while True:
    side = []
    side = list(map(int, input().split()))
    side.sort()
    if side[0] == side[1] == side[2] == 0:
        quit()
    else:
        if side[2]**2 == side[1]**2 + side[0]**2:
            print("right")
        else:
            print("wrong")