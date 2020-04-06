import sys
import math
import random

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]

n = int(input())  # maximum number of turns before game over.

x0, y0 = [int(i) for i in input().split()]

janelaBatman = [x0, y0]

x1 = 0
y1 = 0
x2 = w - 1
y2 = h - 1

# game loop
while True:
    bomb_dir = input()

    if bomb_dir.find('U'):
        y2 = y0 - 1
    elif bomb_dir.find('D'):
        y1 = y0 + 1

    if bomb_dir.find('L'):
        x2 = x0 - 1
    elif bomb_dir.find('R'):
        x1 = x0 + 1

    x0 = x1 + (x2 - x1) / 2
    y0 = y1 + (y2 - y1) / 2

    print(x0, y0)