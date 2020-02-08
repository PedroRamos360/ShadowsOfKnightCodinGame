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

# Criar dicionário para contar direções aqui
contadorDirecoes = {
    "U": 0,
    "D": 0,
    "R": 0,
    "L": 0,
    "UL": 0,
    "UR": 0,
    "DL": 0,
    "DR": 0,
}

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
            janelaDirecao = janelas[i]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] == janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    if bomb_dir == "D":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] == janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    # X axis
    if bomb_dir == "R":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    if bomb_dir == "L":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    # XY axis
    if bomb_dir == "UR":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    if bomb_dir == "UL":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    if bomb_dir == "DR":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    if bomb_dir == "DL":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)

    janela = janelasNovas[int(len(janelasNovas) / 2)]

    print(janela[0], janela[1])
    janelaBatman = janela

