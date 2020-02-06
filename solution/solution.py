import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# game loop
while True:
    bomb_dir = input()  # direção
    forcaPulo = int((w + h) / 2)
    print(forcaPulo, file=sys.stderr)

    for i in range(forcaPulo):
        if forcaPulo < (w - x0):
            if bomb_dir == "U":
                y0 -= forcaPulo
                print(x0, y0)

            if bomb_dir == "UR":
                y0 -= forcaPulo
                x0 += forcaPulo
                print(x0, y0)

            if bomb_dir == "R":
                x0 += forcaPulo
                print(x0, y0)

            if bomb_dir == "DR":
                y0 += forcaPulo
                x0 += forcaPulo
                print(x0, y0)

            if bomb_dir == "D":
                y0 += forcaPulo
                print(x0, y0)

            if bomb_dir == "DL":
                x0 -= forcaPulo
                y0 += forcaPulo
                print(x0, y0)

            if bomb_dir == "L":
                x0 -= forcaPulo
                print(x0, y0)

            if bomb_dir == "UL":
                x0 -= forcaPulo
                y0 -= forcaPulo
                print(x0, y0)
        else:
            forcaPulo -= 1