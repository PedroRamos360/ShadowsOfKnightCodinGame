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

    for i in range(forcaPulo):
        if bomb_dir == "U" and forcaPulo < h:
            y0 -= forcaPulo
            print(x0, y0)
        elif bomb_dir == "U":
            forcaPulo -= 1

        if bomb_dir == "UR" and forcaPulo < h:
            y0 -= forcaPulo
            x0 += forcaPulo
            print(x0, y0)
        elif bomb_dir == "UR":
            forcaPulo -= 1

        if bomb_dir == "R" and forcaPulo < h:
            x0 += forcaPulo
            print(x0, y0)
        elif bomb_dir == "R":
            forcaPulo -= 1

        if bomb_dir == "DR" and forcaPulo < h:
            y0 += forcaPulo
            x0 += forcaPulo
            print(x0, y0)
        elif bomb_dir == "DR":
            forcaPulo -= 1

        if bomb_dir == "D" and forcaPulo < h:
            y0 += forcaPulo
            print(x0, y0)
        elif bomb_dir == "D":
            forcaPulo -= 1

        if bomb_dir == "DL" and forcaPulo < w:
            x0 -= forcaPulo
            y0 += forcaPulo
            print(x0, y0)
        elif bomb_dir == "DL":
            forcaPulo -= 1

        if bomb_dir == "L" and forcaPulo < w:
            x0 -= forcaPulo
            print(x0, y0)
        elif bomb_dir == "L":
            forcaPulo -= 1

        if bomb_dir == "UL" and forcaPulo < w:
            x0 -= forcaPulo
            y0 -= forcaPulo
            print(x0, y0)
        elif bomb_dir == "UL":
            forcaPulo -= 1