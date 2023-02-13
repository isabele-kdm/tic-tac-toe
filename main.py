def print_matriz(matriz):
    for i in range(0, 3):
        print(matriz[i])


def placar(matriz, jogador1, jogador2):
    if matriz[0][0] == jogador1 and matriz[0][1] == jogador1 and matriz[0][2] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][0] == jogador2 and matriz[0][1] == jogador2 and matriz[0][2] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[1][0] == jogador1 and matriz[1][1] == jogador1 and matriz[1][2] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[1][0] == jogador2 and matriz[1][1] == jogador2 and matriz[1][2] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[2][0] == jogador1 and matriz[2][1] == jogador1 and matriz[2][2] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[2][0] == jogador2 and matriz[2][1] == jogador2 and matriz[2][2] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[0][0] == jogador1 and matriz[1][0] == jogador1 and matriz[2][0] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][0] == jogador2 and matriz[1][0] == jogador2 and matriz[2][0] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[0][1] == jogador1 and matriz[1][1] == jogador1 and matriz[2][1] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][1] == jogador2 and matriz[1][1] == jogador2 and matriz[2][1] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[0][2] == jogador1 and matriz[1][2] == jogador1 and matriz[2][2] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][2] == jogador2 and matriz[1][2] == jogador2 and matriz[2][2] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[0][0] == jogador1 and matriz[1][1] == jogador1 and matriz[2][2] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][0] == jogador2 and matriz[1][1] == jogador2 and matriz[2][2] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()
    elif matriz[0][2] == jogador1 and matriz[1][1] == jogador1 and matriz[2][0] == jogador1:
        print('\nO jogador 1 venceu!')
        exit()
    elif matriz[0][2] == jogador2 and matriz[1][1] == jogador2 and matriz[2][0] == jogador2:
        print('\nO jogador 2 venceu!')
        exit()


jogador1 = 'X'
jogador2 = 'O'
matriz = []
posicao = 0
jogadas = 0

for i in range(0, 3):
    matriz.append([0] * 3)

matriz[0][0] = 1
matriz[0][1] = 2
matriz[0][2] = 3
matriz[1][0] = 4
matriz[1][1] = 5
matriz[1][2] = 6
matriz[2][0] = 7
matriz[2][1] = 8
matriz[2][2] = 9

print_matriz(matriz)

while jogadas <= 9:
    posicao = int(input('\nJogador 1, digite a posição que deseja marcar: '))

    for i in range(0, 3):
        for j in range(0, 3):
            if matriz[i][j] == posicao:
                matriz[i][j] = jogador1
    print_matriz(matriz)

    placar(matriz, jogador1, jogador2)

    posicao = int(input('\nJogador 2, digite a posição que deseja marcar: '))

    for i in range(0, 3):
            for j in range(0, 3):
                if matriz[i][j] == posicao:
                    matriz[i][j] = jogador2
    print_matriz(matriz)

    placar(matriz, jogador1, jogador2)

    jogadas += 1

print('Deu velha!')
