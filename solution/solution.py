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

janelas = []
janelax = 0
janelay = 0
janelasRetiradas = 0

for i in range(w * h):
    janelas.append((janelax, janelay))
    if janelax < w - 1:
        janelax += 1
    else:
        janelay += 1
        janelax = 0

# game loop
while True:
    bomb_dir = input()
    janelasNovas = []

    # Pega a direção e mostra todas as janelas naquela direção
    # Y axis
    if bomb_dir == "U":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] == janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    if bomb_dir == "D":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] == janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1
    # X axis
    if bomb_dir == "R":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    if bomb_dir == "L":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    # XY axis
    if bomb_dir == "UR":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    if bomb_dir == "UL":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    if bomb_dir == "DR":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    if bomb_dir == "DL":
        for i in range(w * h):
            janelaDirecao = janelas[i - janelasRetiradas]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
                janelas.remove(janelaDirecao)
                janelasRetiradas += 1

    try:
        janela = janelasNovas[int(len(janelas) / 2)]

    except IndexError:
        janela = janelaBatman

    print(janela[0], janela[1])
    janelaBatman = janela

# Erros:
# 1 Se mover na diagonal o batman para
# 2 Se mover muitas vezes da Index Error na linha 37 (ou outras linhas com esse código)
#
