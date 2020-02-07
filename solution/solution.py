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

# game loop
while True:
    bomb_dir = input()
    janelas = []
    janelax = 0
    janelay = 0

    for i in range((w - 1) * (h - 1)):
        janelas.append((janelax, janelay))
        if janelax < w - 1:
            janelax += 1
        else:
            janelay += 1
            janelax = 0

    for i in range(len(janelas)):
        # Pega a direção e mostra todas as janelas naquela direção
        pass

    janela = random.choice(janelas)
    print(janela[0], janela[1])