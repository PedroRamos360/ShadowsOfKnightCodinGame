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

def search(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return True
    return False

janelasErradas = []
janelas = []
janelax = 0
janelay = 0

# Criar dicionário para contar direções aqui
contadorDirecoes = [
    0, #"U"[0]
    0, #"D"[1]
    0, #"R"[2]
    0, #"L":[3]
    0, #"UR":[4]
    0, #"UL":[5]
    0, #"DR":[6]
    0, #"DL":[7]
]

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
        contadorDirecoes[0] += 1
    if bomb_dir == "D":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] == janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[1] += 1
    # X axis
    if bomb_dir == "R":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[2] += 1
    if bomb_dir == "L":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] == janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[3] += 1
    # XY axis
    if bomb_dir == "UR":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[4] += 1
    if bomb_dir == "UL":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] < janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[5] += 1
    if bomb_dir == "DR":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] > janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[6] += 1
    if bomb_dir == "DL":
        for i in range(w * h):
            janelaDirecao = janelas[i]
            if janelaDirecao[1] > janelaBatman[1] and janelaDirecao[0] < janelaBatman[0]:
                janelasNovas.append(janelaDirecao)
        contadorDirecoes[7] += 1

    janela = janelasNovas[int(len(janelasNovas) / 2)]
    index = 0
    while search(janelasErradas, janela):
        index += 1
        janela = janelasNovas[int(len(janelasNovas) / 2) - index]

    # Output
    print(janela[0], janela[1])

    # Debug Output
    print(contadorDirecoes)

    # Atualiza a janela do Batman
    janelaBatman = janela
    janelasErradas.append(janelaBatman)

